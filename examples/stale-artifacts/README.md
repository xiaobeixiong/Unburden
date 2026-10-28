# Stale Artifacts: a hook targets an absent legacy evaluator

**Contract:** The launcher returns a command for the shipped evaluator, `tools/evaluate.py`. Candidate instead names `tools/evaluate_legacy.py`, which is absent from its complete snapshot.

| Path | Role |
| --- | --- |
| [base/example.py](base/example.py) | Launcher using the shipped evaluator. |
| [candidate/example.py](candidate/example.py) | Launcher with a stale hook target. |
| [candidate/tools/evaluate.py](candidate/tools/evaluate.py) | Current evaluator; the corresponding file also exists in Base. |
| [findings.md](findings.md) | Comparison and snapshot reports. |
| [improved.py](improved.py) | Small correction to the hook target. |
| [non_finding.py](non_finding.py) | An old name retained as a supported public compatibility alias. |

Use only `base/` and `candidate/` as the repository endpoints, or only `candidate/` for snapshot review. Do not use the expected findings or alternatives as review evidence. These are fictional static source illustrations; do not execute the commands.

The finding is about a concrete stale reference, not the word `legacy`. No Git history or proof about external callers is needed to establish that this snapshot lacks the named script. Conversely, do not remove a supported alias merely because the repository has no internal caller. A concern about an apparently superseded asset with unknown external use should state the inspected consumers and suggest confirming retention, not assert universal disuse.

See the [Text counterpart](text/README.md) for outdated guidance and internal records included outside a declared public-bundle scope.
