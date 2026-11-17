#!/usr/bin/env python3
"""Validate local Blueprint structure/ordering (not a runtime or remote JSON-schema test)."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "playground" / "blueprints"
FREE = "/wpessential-cart-rules-inspector.zip"
PRO = "/wpessential-cart-rules-inspector-pro.zip"

def validate():
    cases = [("base", []), ("free", [FREE]), ("pro", [FREE, PRO]), ("compatibility", [FREE, PRO])]
    for label, expected in cases:
        blueprint = json.loads((BASE / label / "blueprint.json").read_text(encoding="utf-8"))
        assert blueprint.get("$schema") == "https://playground.wordpress.net/blueprint-schema.json"
        steps = blueprint["steps"]
        assert steps[0]["step"] == "login"
        installs = [s for s in steps if s.get("step") == "installPlugin"]
        assert installs[0]["pluginData"] == {"resource": "wordpress.org/plugins", "slug": "woocommerce"}
        assert all("pluginZipFile" not in s and s.get("options",{}).get("activate") is True for s in installs)
        actual = [s["pluginData"]["path"] for s in installs if s.get("pluginData",{}).get("resource") == "bundled"]
        assert actual == expected, (label, actual, expected)
        if label == "compatibility":
            assert installs[-1]["pluginData"]["slug"] == "advanced-dynamic-pricing-for-woocommerce"
        print(label, "JSON + structural references valid; live Playground NOT run")

if __name__ == "__main__": validate()
