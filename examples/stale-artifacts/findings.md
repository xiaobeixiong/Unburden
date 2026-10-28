# Expected findings

## Comparison review

```text
Mode: Comparison review
Base: base/ (repository snapshot)
Candidate: candidate/ (repository snapshot)
Scope: changed evaluator hook and its shipped target.
```

1. Point the evaluation hook at the shipped evaluator.
   - **Dimension:** Stale Artifacts.
   - **Location:** `example.py:6`.
   - **Evidence:** Candidate changes the hook from `tools/evaluate.py` to `tools/evaluate_legacy.py`. The contract at `example.py:1` identifies the former as the only shipped evaluator, the current file is present, and the legacy script is absent from Candidate.
   - **Consequence:** The returned command targets a nonexistent script rather than the current evaluator. This is a static path mismatch, not a measured failed run.
   - **Minimal suggestion:** Restore the hook target to `tools/evaluate.py`; retain the split argument and the current evaluator.

## Snapshot review

```text
Mode: Snapshot review
Candidate: candidate/ (repository snapshot)
Scope: evaluator hook, command construction, and shipped evaluator files.
```

1. Point the evaluation hook at the shipped evaluator.
   - **Dimension:** Stale Artifacts.
   - **Location:** `example.py:6`.
   - **Evidence:** The hook names `tools/evaluate_legacy.py`, while the snapshot supplies only `tools/evaluate.py`, consistent with the contract on line 1. The command builder consumes the hook on line 11.
   - **Consequence:** The constructed command selects a missing file. This review does not establish when the mismatch appeared or claim to have executed it.
   - **Minimal suggestion:** Use `tools/evaluate.py`.

[improved.py](improved.py) illustrates that narrow change. [non_finding.py](non_finding.py) preserves an explicitly supported compatibility alias: an old name and no visible internal calls do not make it obsolete.
