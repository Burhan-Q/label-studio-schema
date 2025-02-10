from pathlib import Path

ROOT = Path(__file__).parent
LS_REPO = ROOT.parent.parent / "ls-files/label-studio"

__all__ = "ROOT", "LS_REPO",