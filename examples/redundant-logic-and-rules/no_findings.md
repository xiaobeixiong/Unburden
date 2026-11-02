# Expected report with no findings

This snapshot example reuses [non_finding.py](non_finding.py). The Candidate is the Unburden repository working tree, with scope limited to that file. The file's allowlist and docstring establish the supported ingredients and output contract; no Base or alternative implementation is needed as evidence.

Replace `/absolute/path/to/unburden` with the actual checkout path when using this request:

```text
Use Unburden to review:
Candidate: /absolute/path/to/unburden
Scope: examples/redundant-logic-and-rules/non_finding.py
```

The expected report below uses the same path placeholder. This document is explanatory material outside the selected review scope.

## Expected snapshot report

```text
Mode: Snapshot review
Candidate: /absolute/path/to/unburden (working tree)
Scope: examples/redundant-logic-and-rules/non_finding.py;
       existing Code: the allowlist, describe_dish, validation, and output.

Static inspection considered all seven Unburden dimensions within this scope.
The allowlist defines the supported ingredients, the validation rejects
unsupported names, and the return value follows the documented joined-name
format. The validation enforces the contract and should be retained.

No evidence-backed Unburden findings.

This snapshot review cannot establish whether issues were introduced by a
change. The result applies only to the selected file and does not constitute
a comprehensive correctness review or overall repository approval.
```
