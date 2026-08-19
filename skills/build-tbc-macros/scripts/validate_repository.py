#!/usr/bin/env python3
"""Validate the scalable class README contract for this TBC macro repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = (
    "Player profile",
    "Rotation and talent model",
    "Macro set",
    "Imported reference backlog",
    "Verification log",
)

PROFILE_FIELDS = (
    "Game version",
    "Class",
    "Level",
    "Talent build",
    "Key talents",
    "Role / content",
    "Rotation source",
    "Client locales",
    "Last updated",
    "Overall status",
)

ROTATION_SUBSECTIONS = (
    "Player rotation",
    "Macro opportunities",
    "Deliberately not macroed",
)

ALLOWED_MACRO_STATUSES = {"verified", "ready-for-client-test"}


def section(text: str, heading: str, next_heading: str | None) -> str:
    start_match = re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE)
    if not start_match:
        return ""
    start = start_match.end()
    if next_heading is None:
        return text[start:]
    end_match = re.search(
        rf"^## {re.escape(next_heading)}\s*$", text[start:], re.MULTILINE
    )
    return text[start : start + end_match.start()] if end_match else text[start:]


def validate_class_page(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    class_name = path.parent.name.replace("-", " ").title()

    if not re.search(rf"^# {re.escape(class_name)} macros\s*$", text, re.MULTILINE):
        errors.append(f"{path}: expected '# {class_name} macros'")

    positions: list[int] = []
    for heading in REQUIRED_SECTIONS:
        matches = list(re.finditer(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE))
        if len(matches) != 1:
            errors.append(f"{path}: expected exactly one '## {heading}'")
        else:
            positions.append(matches[0].start())
    if len(positions) == len(REQUIRED_SECTIONS) and positions != sorted(positions):
        errors.append(f"{path}: required sections are out of order")

    profile = section(text, "Player profile", "Rotation and talent model")
    for field in PROFILE_FIELDS:
        if not re.search(rf"^\| {re.escape(field)} \|", profile, re.MULTILINE):
            errors.append(f"{path}: player profile missing '{field}'")

    rotation = section(text, "Rotation and talent model", "Macro set")
    for heading in ROTATION_SUBSECTIONS:
        if not re.search(rf"^### {re.escape(heading)}\s*$", rotation, re.MULTILINE):
            errors.append(f"{path}: rotation model missing '### {heading}'")

    macro_set = section(text, "Macro set", "Imported reference backlog")
    entries = list(re.finditer(r"^### (.+)$", macro_set, re.MULTILINE))
    for index, match in enumerate(entries):
        end = entries[index + 1].start() if index + 1 < len(entries) else len(macro_set)
        entry = macro_set[match.end() : end]
        if "```lua" not in entry:
            continue
        label = match.group(1)
        for field in ("ID", "Status", "Derived from", "Use case", "Targeting", "Limitations"):
            if not re.search(rf"^- {re.escape(field)}:", entry, re.MULTILINE):
                errors.append(f"{path}: macro '{label}' missing '{field}'")
        status_match = re.search(r"^- Status: `([^`]+)`", entry, re.MULTILINE)
        if not status_match or status_match.group(1) not in ALLOWED_MACRO_STATUSES:
            errors.append(f"{path}: macro '{label}' has an invalid status")
        if len(re.findall(r"^#### English \(`enUS`\)\s*$", entry, re.MULTILINE)) != 1:
            errors.append(f"{path}: macro '{label}' needs one enUS block")
        if len(re.findall(r"^#### 简体中文 \(`zhCN`\)\s*$", entry, re.MULTILINE)) != 1:
            errors.append(f"{path}: macro '{label}' needs one zhCN block")
        if len(re.findall(r"```lua", entry)) != 2:
            errors.append(f"{path}: macro '{label}' must contain exactly two Lua blocks")

    expected_log = "| Macro ID | Status | enUS | zhCN | Client build | Date | Notes |"
    verification = section(text, "Verification log", None)
    if expected_log not in verification:
        errors.append(f"{path}: verification log header is missing or malformed")

    return errors


def validate_links(root: Path) -> list[str]:
    errors: list[str] = []
    link_pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
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
            readme = class_dir / "README.md"
            if not readme.is_file():
                errors.append(f"{class_dir}: README.md not found")
            else:
                errors.extend(validate_class_page(readme))
            for forbidden in ("macros", "context", "talents"):
                if (class_dir / forbidden).exists():
                    errors.append(f"{class_dir}: forbidden '{forbidden}' directory")
            if (class_dir / "macros.md").exists():
                errors.append(f"{class_dir}: use README.md instead of macros.md")

    for macro_file in (root / "tbc").rglob("*.macro"):
        errors.append(f"{macro_file}: standalone macro files are not allowed")
    errors.extend(validate_links(root))

    if errors:
        print(f"FAIL: {len(errors)} error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: class schema, bilingual macro entries, layout, and links are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
