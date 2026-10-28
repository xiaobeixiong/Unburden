"""Both names are public: downstream clients still import evaluate_legacy."""


def evaluate(split):
    return {"split": split}


def evaluate_legacy(split):
    """Supported compatibility alias; forwards to the current implementation."""
    return evaluate(split)
