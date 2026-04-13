import os
from pathlib import Path


def test_basic_math():
    assert 1 + 1 == 2


def test_readme_exists():
    root = Path(__file__).resolve().parent.parent
    assert (root / "README.md").exists()
    assert "delivery-time-prediction" in (root / "README.md").read_text(encoding="utf-8")