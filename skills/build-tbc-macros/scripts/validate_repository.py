#!/usr/bin/env python3
"""Validate paired English and Simplified Chinese TBC class pages."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


CLASS_NAMES_ZHCN = {
    "druid": "德鲁伊",
    "hunter": "猎人",
    "mage": "法师",
    "paladin": "圣骑士",
    "priest": "牧师",
    "rogue": "潜行者",
    "shaman": "萨满祭司",
    "warlock": "术士",
    "warrior": "战士",
}

PAGE_SCHEMAS = {
    "enUS": {
        "filename": "README.md",
        "sections": (
            "Player profile",
            "Rotation and talent model",
            "Macro set",
            "Imported reference backlog",
            "Verification log",
        ),
        "profile_fields": (
            "Game version",
            "Class",
            "Level",
            "Talent build",
            "Key talents",
            "Role / content",
            "Rotation source",
            "Client locale",
            "Last updated",
            "Overall status",
        ),
        "rotation_headings": (
            "Player rotation",
            "Macro opportunities",
            "Deliberately not macroed",
        ),
        "macro_fields": ("ID", "Status", "Derived from", "Use case", "Targeting", "Limitations"),
        "status_field": "Status",
        "link": "[简体中文](README_zhCN.md)",
        "log_header": "| Macro ID | Status | enUS | zhCN | Client build | Date | Notes |",
    },
    "zhCN": {
        "filename": "README_zhCN.md",
        "sections": ("玩家配置", "技能循环与天赋模型", "宏组合", "导入参考资料", "验证记录"),
        "profile_fields": (
            "游戏版本",
            "职业",
            "等级",
            "天赋配置",
            "关键天赋",
            "职责 / 玩法",
            "循环来源",
            "客户端语言",
            "最后更新",
            "总体状态",
        ),
        "rotation_headings": ("玩家循环", "宏设计机会", "明确保留手动操作"),
        "macro_fields": ("ID", "状态", "来源", "用途", "目标", "限制"),
        "status_field": "状态",
        "link": "[English](README.md)",
        "log_header": "| 宏 ID | 状态 | enUS | zhCN | 客户端版本 | 日期 | 备注 |",
    },
}

ALLOWED_MACRO_STATUSES = {"verified", "ready-for-client-test"}


@dataclass(frozen=True)
class MacroEntry:
    status: str
    code: str
    label: str


def section(text: str, heading: str, next_heading: str | None) -> str:
    start_match = re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE)
    if not start_match:
        return ""
    start = start_match.end()
    if next_heading is None:
        return text[start:]
    end_match = re.search(rf"^## {re.escape(next_heading)}\s*$", text[start:], re.MULTILINE)
    return text[start : start + end_match.start()] if end_match else text[start:]


def macro_signature(code: str) -> tuple[tuple[object, ...], ...]:
    signature: list[tuple[object, ...]] = []
    for raw_line in code.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        command = line.split(maxsplit=1)[0].lower()
        conditionals = tuple(re.findall(r"\[[^\]]+\]", line))
        resets = tuple(re.findall(r"\breset=[^\s]+", line, re.IGNORECASE))
        numbers = tuple(re.findall(r"(?<![A-Za-z])\d+(?![A-Za-z])", line))
        payload = line[len(line.split(maxsplit=1)[0]) :].lstrip()
        signature.append((command, conditionals, resets, numbers, payload.startswith("!")))
    return tuple(signature)


def extract_entries(
    path: Path, text: str, locale: str, errors: list[str]
) -> dict[str, MacroEntry]:
    schema = PAGE_SCHEMAS[locale]
    macro_heading = schema["sections"][2]
    backlog_heading = schema["sections"][3]
    macro_set = section(text, macro_heading, backlog_heading)
    headings = list(re.finditer(r"^### (.+)$", macro_set, re.MULTILINE))
    entries: dict[str, MacroEntry] = {}

    for index, match in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(macro_set)
        entry = macro_set[match.end() : end]
        if "```lua" not in entry:
            continue
        label = match.group(1).strip()
        for field in schema["macro_fields"]:
            if not re.search(rf"^- {re.escape(field)}:", entry, re.MULTILINE):
                errors.append(f"{path}: macro '{label}' missing '{field}'")

        id_match = re.search(r"^- ID: `([^`]+)`", entry, re.MULTILINE)
        status_match = re.search(
            rf"^- {re.escape(schema['status_field'])}: `([^`]+)`", entry, re.MULTILINE
        )
        code_matches = re.findall(r"```lua\s*\n(.*?)```", entry, re.DOTALL)
        if not id_match:
            errors.append(f"{path}: macro '{label}' has no stable ID")
            continue
        macro_id = id_match.group(1)
        if macro_id in entries:
            errors.append(f"{path}: duplicate macro ID '{macro_id}'")
            continue
        if not status_match or status_match.group(1) not in ALLOWED_MACRO_STATUSES:
            errors.append(f"{path}: macro '{label}' has an invalid status")
            continue
        if len(code_matches) != 1:
            errors.append(f"{path}: macro '{label}' must contain exactly one Lua block")
            continue
        entries[macro_id] = MacroEntry(status_match.group(1), code_matches[0].strip(), label)
    return entries


def extract_log(path: Path, text: str, locale: str, errors: list[str]) -> dict[str, str]:
    schema = PAGE_SCHEMAS[locale]
    verification = section(text, schema["sections"][4], None)
    if schema["log_header"] not in verification:
        errors.append(f"{path}: verification log header is missing or malformed")
    rows: dict[str, str] = {}
    for macro_id, status in re.findall(r"^\| `([^`]+)` \| `([^`]+)` \|", verification, re.MULTILINE):
        if macro_id in rows:
            errors.append(f"{path}: duplicate verification row for '{macro_id}'")
        rows[macro_id] = status
    return rows


def validate_page(path: Path, class_slug: str, locale: str) -> tuple[list[str], dict[str, MacroEntry]]:
    errors: list[str] = []
    schema = PAGE_SCHEMAS[locale]
    text = path.read_text(encoding="utf-8")
    english_name = class_slug.replace("-", " ").title()
    expected_title = f"# {english_name} macros" if locale == "enUS" else f"# {CLASS_NAMES_ZHCN[class_slug]}宏"

    if not re.search(rf"^{re.escape(expected_title)}\s*$", text, re.MULTILINE):
        errors.append(f"{path}: expected '{expected_title}'")
    if schema["link"] not in "\n".join(text.splitlines()[:8]):
        errors.append(f"{path}: reciprocal locale link must appear at the top")
    if locale == "enUS":
        without_locale_link = text.replace(schema["link"], "")
        if re.search(r"[\u3400-\u9fff]", without_locale_link):
            errors.append(f"{path}: Chinese text belongs in README_zhCN.md")

    positions: list[int] = []
    for heading in schema["sections"]:
        matches = list(re.finditer(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE))
        if len(matches) != 1:
            errors.append(f"{path}: expected exactly one '## {heading}'")
        else:
            positions.append(matches[0].start())
    if len(positions) == len(schema["sections"]) and positions != sorted(positions):
        errors.append(f"{path}: required sections are out of order")

    profile = section(text, schema["sections"][0], schema["sections"][1])
    for field in schema["profile_fields"]:
        if not re.search(rf"^\| {re.escape(field)} \|", profile, re.MULTILINE):
            errors.append(f"{path}: player profile missing '{field}'")

    rotation = section(text, schema["sections"][1], schema["sections"][2])
    for heading in schema["rotation_headings"]:
        if not re.search(rf"^### {re.escape(heading)}\s*$", rotation, re.MULTILINE):
            errors.append(f"{path}: rotation model missing '### {heading}'")

    entries = extract_entries(path, text, locale, errors)
    log = extract_log(path, text, locale, errors)
    if set(log) != set(entries):
        errors.append(f"{path}: verification rows must match macro-set IDs")
    for macro_id, entry in entries.items():
        if log.get(macro_id) != entry.status:
            errors.append(f"{path}: verification status differs for '{macro_id}'")
    return errors, entries


def validate_pair(class_dir: Path) -> list[str]:
    errors: list[str] = []
    pages: dict[str, dict[str, MacroEntry]] = {}
    for locale, schema in PAGE_SCHEMAS.items():
        path = class_dir / schema["filename"]
        if not path.is_file():
            errors.append(f"{class_dir}: {schema['filename']} not found")
            pages[locale] = {}
            continue
        page_errors, entries = validate_page(path, class_dir.name, locale)
        errors.extend(page_errors)
        pages[locale] = entries

    if set(pages.get("enUS", {})) != set(pages.get("zhCN", {})):
        errors.append(f"{class_dir}: enUS and zhCN macro IDs do not match")
    for macro_id in sorted(set(pages.get("enUS", {})) & set(pages.get("zhCN", {}))):
        english = pages["enUS"][macro_id]
        chinese = pages["zhCN"][macro_id]
        if english.status != chinese.status:
            errors.append(f"{class_dir}: status differs across locales for '{macro_id}'")
        if macro_signature(english.code) != macro_signature(chinese.code):
            errors.append(f"{class_dir}: Lua structure differs across locales for '{macro_id}'")
    return errors


def validate_links(root: Path) -> list[str]:
    errors: list[str] = []
    link_pattern = re.compile(r"(?<![!`])\[[^\]]*\]\(([^)]+)\)")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        if "skills" in path.parts and "assets" in path.parts:
            continue
        for raw_target in link_pattern.findall(path.read_text(encoding="utf-8")):
            target = raw_target.strip().split()[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            if not resolved.exists():
                errors.append(f"{path}: broken relative link '{target}'")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    classes_root = root / "tbc" / "classes"
    errors: list[str] = []

    if not classes_root.is_dir():
        errors.append(f"{classes_root}: class directory not found")
    else:
        class_dirs = sorted(path for path in classes_root.iterdir() if path.is_dir())
        if not class_dirs:
            errors.append(f"{classes_root}: no class directories found")
        for class_dir in class_dirs:
            if class_dir.name not in CLASS_NAMES_ZHCN:
                errors.append(f"{class_dir}: unknown TBC class directory")
                continue
            errors.extend(validate_pair(class_dir))
            for forbidden in ("macros", "context", "talents"):
                if (class_dir / forbidden).exists():
                    errors.append(f"{class_dir}: forbidden '{forbidden}' directory")
            if (class_dir / "macros.md").exists():
                errors.append(f"{class_dir}: use locale README files instead of macros.md")
            allowed = {"README.md", "README_zhCN.md"}
            for markdown in class_dir.glob("*.md"):
                if markdown.name not in allowed:
                    errors.append(f"{markdown}: unexpected class Markdown file")

    for macro_file in (root / "tbc").rglob("*.macro"):
        errors.append(f"{macro_file}: standalone macro files are not allowed")
    errors.extend(validate_links(root))

    if errors:
        print(f"FAIL: {len(errors)} error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: locale pages, macro pairs, schema, layout, and links are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
