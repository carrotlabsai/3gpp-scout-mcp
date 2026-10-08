#!/usr/bin/env python3
"""Validate Scout's submission fields and build a credential-free plugin ZIP."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import urlparse
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / "plugins" / "3gpp-scout"


def validate(root=ROOT):
    portable = json.loads((root / "plugin.json").read_text())
    compat = json.loads((root / ".codex-plugin/plugin.json").read_text())
    extension = portable["extensions"]["com.openai"]
    ui = extension["interface"]
    assert compat["interface"] == ui, "Portable and Codex listing metadata differ"
    assert portable["author"]["name"] == ui["developerName"] == "3gppscout"
    assert portable["version"] == compat["version"]
    for key, maximum in {"displayName": 30, "shortDescription": 30, "longDescription": 4000, "developerName": 80}.items():
        assert 0 < len(ui[key]) <= maximum, key
    for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        url = urlparse(ui[key])
        assert url.scheme == "https" and url.hostname and not url.username and not url.password, key
    assert len(ui["defaultPrompt"]) <= 3
    assert all(0 < len(p) <= 128 for p in ui["defaultPrompt"])
    for field in ("logo", "composerIcon"):
        path = ui[field]
        assert path.startswith("./")
        icon = (root / path).resolve()
        assert icon.is_relative_to(root.resolve()) and icon.is_file() and not icon.is_symlink()
        assert icon.stat().st_size <= 5 * 1024 * 1024
        svg = ET.fromstring(icon.read_text())
        assert float(svg.attrib["width"]) == float(svg.attrib["height"]) >= 48
    cases = extension["review"]["test_cases"]
    assert len(cases["positive"]) == 5 and len(cases["negative"]) == 3
    for kind, rows in cases.items():
        for row in rows:
            assert row["description"] and row["prompt"] and row["expected_behavior"]
            if kind == "positive":
                assert row["tools_triggered"]
    assert extension["review"]["commerce"] is False
    recording = extension["review"].get("demo_recording_url")
    if recording:
        assert urlparse(recording).scheme == "https"
    portable_mcp = json.loads((root / "mcp.json").read_text())["mcpServers"]
    assert len(portable_mcp) == 1
    compat_mcp = json.loads((root / ".mcp.json").read_text())["mcpServers"]
    assert {name: value["url"] for name, value in portable_mcp.items()} == {name: value["url"] for name, value in compat_mcp.items()}
    assert list(portable_mcp.values())[0]["url"] == "https://api.3gppscout.com/mcp/"
    return recording


def build(output):
    recording = validate()
    paths = [ROOT / p for p in ("plugin.json", "mcp.json", ".mcp.json", ".codex-plugin/plugin.json")]
    paths += sorted(p for sub in ("skills", "assets") for p in (ROOT / sub).rglob("*") if p.is_file())
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as bundle:
        for path in paths:
            assert not path.is_symlink() and path.resolve().is_relative_to(ROOT.resolve())
            text = path.read_text()
            assert not re.search(r'"(?:test_credentials|reviewer_instructions|client_secret|api_key|password)"\s*:', text)
            info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), (2026, 10, 7, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, text)
    print(f"Validated and built {len(paths)} files: {output}")
    print("Review recording: " + (recording or "not added yet; draft package only"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build(args.output.resolve())
