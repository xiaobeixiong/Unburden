"""Use tools/evaluate.py, the only evaluator shipped in this snapshot."""
from pathlib import Path
import sys


EPOCH_END_EVALUATOR = "tools/evaluate.py"


def evaluation_command(split):
    root = Path(__file__).resolve().parent
    return [sys.executable, str(root / EPOCH_END_EVALUATOR), "--split", split]
