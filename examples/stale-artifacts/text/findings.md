# Expected findings

## Comparison review

```text
Mode: Comparison review
Base: base/ (repository snapshot)
Candidate: candidate/ (repository snapshot)
Scope: changed Usage and attachment in GUIDE.md; added recovery_notes.md.
```

1. Update the usage command to the supported evaluator.
   - **Dimension:** Stale Artifacts.
   - **Location:** `GUIDE.md:10`.
   - **Evidence:** The Usage command changes to `tools/evaluate_legacy.py`. Lines 4-5 identify the current command and retirement of the legacy entry point; only `tools/evaluate.py` is shipped.
   - **Consequence:** The current-use section directs the reader to an absent entry point. No attempted execution or actual reader confusion is claimed.
   - **Minimal suggestion:** Use `python tools/evaluate.py --split test`.

2. Keep internal recovery notes out of this public bundle.
   - **Dimension:** Stale Artifacts.
   - **Location:** `GUIDE.md:12-13`.
   - **Evidence:** The new attachment links `recovery_notes.md`, added in Candidate. Its lines 1-4 describe internal notes for a discarded temporary trial. The guide's lines 6-7 say the whole directory is shipped but internal experiment and recovery records are outside the bundle's scope.
   - **Consequence:** The bundle includes and advertises an internal record outside its declared delivery scope.
   - **Minimal suggestion:** Exclude the notes from this public snapshot and remove the attachment; their retention in the internal research repository is a separate decision.

## Snapshot review

```text
Mode: Snapshot review
Candidate: candidate/ (repository snapshot)
Scope: GUIDE.md, its attachment, and shipped evaluator files.
```

1. Update the usage command to the supported evaluator.
   - **Dimension:** Stale Artifacts.
   - **Location:** `GUIDE.md:10`.
   - **Evidence:** The current contract at lines 4-5 identifies `tools/evaluate.py` and retires the legacy evaluator, but Usage names the absent legacy script.
   - **Consequence:** The operative guide points outside the shipped interface. Its introduction time is unknown in this mode.
   - **Minimal suggestion:** Replace the Usage command with the supported command.

2. Keep internal recovery notes out of this public bundle.
   - **Dimension:** Stale Artifacts.
   - **Location:** `GUIDE.md:12-13`.
   - **Evidence:** The attachment exposes a discarded-trial record; lines 6-7 define a full-directory public bundle that excludes this kind of material.
   - **Consequence:** A record outside the declared delivery scope is included and linked as part of the guide.
   - **Minimal suggestion:** Exclude this record and its link from the public bundle; do not infer that it should be deleted from every repository.

[improved.md](improved.md) shows the guide correction; excluding the record from the bundle is also required. [non_finding.md](non_finding.md) demonstrates a useful internal archive that is intentionally retained and not shipped. Do not flag that archive just because its records are historical.
