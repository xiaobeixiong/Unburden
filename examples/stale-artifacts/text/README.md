# Stale Artifacts: superseded guidance and internal records in a public bundle

The snapshots contain a current evaluator and a guide declaring the supported command and public delivery scope. Candidate introduces an absent legacy command in its Usage section and attaches internal recovery notes, although the entire directory is copied into the public bundle.

| Path | Role |
| --- | --- |
| [base/GUIDE.md](base/GUIDE.md) | Current usage and delivery contract. |
| [candidate/GUIDE.md](candidate/GUIDE.md) | Contradictory legacy command and newly linked internal notes. |
| [candidate/recovery_notes.md](candidate/recovery_notes.md) | Internal record included outside the declared public scope. |
| [candidate/tools/evaluate.py](candidate/tools/evaluate.py) | Current entry point; also present in Base. |
| [findings.md](findings.md) | Expected comparison and snapshot reports. |
| [improved.md](improved.md) | Guide with current usage and no internal attachment. |
| [non_finding.md](non_finding.md) | Useful research archive explicitly excluded from the public package. |

Use only the snapshot directories as review inputs, with optional Base. No script execution, model scores, or development history is needed. The delivery finding does not mean the notes are worthless or should be deleted from the internal repository; exclude them from this bundle. The guide alternative alone does not remove the bundled notes, so packaging must also honor that scope.

The source files are fictional illustrations, not traces from an actual experiment. They do not demonstrate that a reader followed the stale guide or that any model behavior changed.
