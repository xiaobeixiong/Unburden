# Expected findings

## Comparison review

```text
Mode: Comparison review
Base: base/ (repository snapshot)
Candidate: candidate/ (repository snapshot)
Scope: changed introduction in article.md, with its page purpose and output definition.
```

1. Remove the irrelevant product-category exclusions from the opening.
   - **Dimension:** Redundant Logic and Rules.
   - **Location:** `article.md:9`.
   - **Evidence:** Line 5 assigns this opening the job of describing inputs, size limit, and output, and places product-category comparisons on a separate page. Candidate adds "not an image editor, not an asset manager, and not a creative suite" before the retained compression description. The positive clause on line 9 and output definition on line 10 already provide every specified detail; the added negatives distinguish no method, processing boundary, limitation, or uncertainty relevant to this opening.
   - **Consequence:** The new preamble introduces and dismisses three product categories outside this opening's declared purpose before providing the same capability description.
   - **Minimal suggestion:** Replace line 9 with "A utility that compresses an existing JPEG or PNG image to a requested file-size limit." Keep line 10 and the page purpose.

## Snapshot review

```text
Mode: Snapshot review
Candidate: candidate/ (repository snapshot)
Scope: article.md, including its page purpose and introduction.
```

1. Remove the irrelevant product-category exclusions from the opening.
   - **Dimension:** Redundant Logic and Rules.
   - **Location:** `article.md:9`.
   - **Evidence:** Line 5 defines the opening's purpose and places product-category comparisons elsewhere. Line 9 introduces and rejects three categories before stating the compression capability. Its positive clause and line 10 already provide the specified input, size limit, and output details. The negatives add no substantive distinction within this purpose.
   - **Consequence:** The opening contains a removable detour through unrelated categories. This snapshot does not establish who wrote it or why those categories were mentioned.
   - **Minimal suggestion:** Retain the positive description as "A utility that compresses an existing JPEG or PNG image to a requested file-size limit." Preserve the output sentence.

[improved.md](improved.md) illustrates the minimal change. In [non_finding.md](non_finding.md), "not uploaded to a server" conveys the processing boundary and should stay. Neither report infers a prior correction or treats negative phrasing itself as a defect.
