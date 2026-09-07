# Review materials

This snapshot accompanies *Auditable Cross-Chain Fund Tracing from Public Records:
Payout Reconciliation and Termination Diagnostics*.

## Complete revision package

The complete ZIP is 146,333,570 bytes and includes the unchanged original evidence,
the new experiments, and the anonymous returned-execution supplement. It is provided
as two valid ZIP parts because each file in a regular GitHub repository must be
under its file-size limit. Download these three files to the same new directory:

- [Part 1](VCA_review_v5_part1.zip)
- [Part 2](VCA_review_v5_part2.zip)
- [Offline assembler](assemble_review.py)

Run `python -B assemble_review.py` with Python 3.12. This performs no network access
and verifies both parts before writing the complete ZIP. Extract that complete ZIP
to a short, new path and follow its README for installation and offline checks.
Do not try to run experiments from the individual part archives.

Complete ZIP SHA-256: `1a474cf43851d37bd8740671af7c2755d41190ff476ffc5437b11910afc2c1dc`.
The [download manifest](DOWNLOAD_MANIFEST.json) also records all part digests.
The [checksums](SHA256SUMS) cover the files provided here. Obtain the complete ZIP
digest through the review channel as well; a self-supplied manifest alone cannot
authenticate its publisher.

## What changed

- The frozen decoder and original June 40-swap result (9 complete) are preserved.
- A separately selected temporal sample completes 46/96 swaps with the same
  decoder; 49 are unsupported and one is rejected for a 2-wei amount discrepancy.
- Same-evidence payment calculations, output-identity controls, 132 historical
  payer checks, four full policy variants and one targeted hub completion are
  included with their inputs, outputs and offline recalculation commands.
- The returned Windows execution is included. Operator affiliation remains
  unconfirmed; this is not presented as confirmed independent-team reproduction.

The original [revision 4 archive](VCA_anonymous_review_v4r2_20260907.zip) remains
available unchanged for historical comparison. Use revision 5 for the new tables.
The package README distinguishes fresh recalculation from recounting saved full
traces and supplies optional full-trace commands. Failures and missing data remain
in the reported denominators. No general tracing accuracy or tool superiority is
claimed. Review mirrors should pin the intended version and be checked at submission.
