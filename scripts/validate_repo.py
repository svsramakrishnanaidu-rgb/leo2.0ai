"""Lightweight repository checks; no external packages or network calls."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md", "SECURITY.md", "CONTRIBUTING.md",
    "docs/SOURCES.md", "docs/PRODUCT_REQUIREMENTS.md",
    "docs/ARCHITECTURE.md", "docs/UI_UX.md", "docs/PERMISSIONS.md",
    "docs/PROVIDERS.md", "docs/DATA.md", "docs/MULTIMODAL.md",
    "docs/ROADMAP.md", "docs/WORKFLOWS.md", "docs/TEST_PLAN.md",
    "prompts/LEO_2_BUILD_INSTRUCTION.md",
    "resources/source_manifest.json",
    "resources/provider_catalog.example.json",
]

MD_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HTML_ASSET = re.compile(r"(?:src|href)=[\"']([^\"']+)[\"']")
SECRET_PATTERNS = [
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bgsk_[A-Za-z0-9]{25,}\b"),
    re.compile(r"\bAIza[A-Za-z0-9_\-]{30,}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def is_external(value: str) -> bool:
    return value.startswith(("#", "mailto:", "tel:", "//")) or bool(urlsplit(value).scheme)


def check_links(file: Path, errors: list[str]) -> None:
    contents = file.read_text(encoding="utf-8")
    values = MD_LINK.findall(contents) + HTML_ASSET.findall(contents)
    for link in values:
        link = link.strip().split(" ", 1)[0]
        if not link or is_external(link) or "{{" in link:
            continue
        path_part = unquote(link.split("#", 1)[0].split("?", 1)[0])
        if not path_part:
            continue
        target = (file.parent / path_part).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"{file.relative_to(ROOT)}: out-of-repo link: {link}")
            continue
        if not target.exists():
            errors.append(f"{file.relative_to(ROOT)}: missing file for link {link}")


def main() -> int:
    errors = []
    for name in REQUIRED:
        p = ROOT / name
        if not p.is_file() or p.stat().st_size == 0:
            errors.append(f"required file missing or empty: {name}")

    for path in ROOT.rglob("*.md"):
        if ".git" not in path.parts:
            check_links(path, errors)

    for dirname in ("leo_core", "scripts", "tests"):
        folder = ROOT / dirname
        if not folder.exists():
            continue
        for path in folder.rglob("*.py"):
            text = path.read_text(encoding="utf-8")
            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    errors.append(f"possible embedded credential in {path.relative_to(ROOT)}")

    for name in ("resources/source_manifest.json", "resources/provider_catalog.example.json"):
        try:
            record = json.loads((ROOT / name).read_text(encoding="utf-8"))
            if name.endswith("provider_catalog.example.json"):
                for provider in record.get("providers", []):
                    if provider.get("enabled") is not False or provider.get("status") != "UNVERIFIED":
                        errors.append(f"unverified provider must be disabled: {provider.get('id', 'unknown')}")
                    if provider.get("secret_ref") is not None:
                        errors.append(f"example provider contains secret reference: {provider.get('id', 'unknown')}")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON or missing file: {name}: {exc}")

    for error in errors:
        print("FAIL:", error)
    if errors:
        print(f"FAILED: {len(errors)} repository checks")
        return 1
    print(f"OK: {len(REQUIRED)} required files and local Markdown assets checked")
    print("NOTE: pattern checks are not a substitute for full secret scanning or policy review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
