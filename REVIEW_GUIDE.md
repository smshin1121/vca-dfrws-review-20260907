# Review guide: results, archives and replay commands

This guide accompanies *Auditable Cross-Chain Fund Tracing from Public Records: Payout Reconciliation and Termination Diagnostics*. Start with revision 9 to check the edge-count correction and the raw 2-wei discrepancy. The earlier archives provide the full experiments. Revision 9 audits existing records; it is not another scientific sample or a decoder update.

The anonymous entry point is <https://anonymous.4open.science/r/vca-dfrws-review-20260907-B38E/>. The revision-5 distribution parts and revision-6 through revision-8 ZIPs have been downloaded without authentication and checked against preserved bytes. This guide makes no anonymous-availability claim for revision 9. Check the actual release files and download manifest before reporting access.

## 1. Which material supports each result?

Section and table numbers refer to the accompanying English manuscript. Commands below are identified by their archive version.

| Paper location | Evaluation unit and denominator | Archive and expected result |
| --- | --- | --- |
| Sections 2–3; Tables 1–2 | Prior-work comparison and study-defined categories; no experimental denominator | v5 source, `PROCEDURE_NOTES.md` and listed references explain the method. These tables are not additional accuracy experiments. |
| Sections 4.1–4.3; Tables 3–5 | Two development incidents; all 153 decoded THORChain hops: 87 KelpDAO and 66 Bybit | v5: 132 referenced BTC transactions available and consistent; 21 unavailable. Full-replay commands separately generate each incident twice. Measure new execution times; do not expect identical wall-clock durations. |
| Section 4.4; Table 6 | Paired in-memory controls on reused records | v5: 617 targeted inconsistencies rejected; 153 repeated-output cases preserve totals; 923 unchanged copies pass; 153 date changes pass because that field is unchecked. Another 24 constructed boundary controls are separate from these counts. |
| Section 4.4; real-output paragraph | Three selected Bitcoin transactions from eight fixed blocks: 18,401 transactions, 215 candidate transactions | v7r2: each selected equal-output pair retains 1,200 satoshi by output index versus 600 under the four-field projection. There are 24 primary and six separate-verifier controls. These are derived Bitcoin rows, not observed Midgard actions. |
| Section 4.5; Table 7 | Same-evidence accounting on 87 KelpDAO and 45 available Bybit hops | v5: KelpDAO naive sum 491.30830301 BTC; VCA/reference sum 389.46136346 BTC; excess 101.84693955 BTC. All three covered Bybit sums are 233.98485498 BTC. Its 21 unavailable transactions remain outside these sums. |
| Sections 4.6–4.7; Tables 8–9 | Bybit graph rows/addresses; 1,919 original stop markers; four policy variants and one targeted hub completion | v5: 1,894 expansion errors and 25 window stops; error-history groups 1,890/2/2. v9: no-overrides graph has 2,142 common rows, 985 removed and six added: 3,127 − 985 + 6 = 2,148. Other variant deltas are unchanged. |
| Section 4.8; Table 10 | The same 153 deposits, searched at three time windows | v5: both 6-hour and 24-hour windows rediscover 132 unique candidates and leave 21 without candidates. Historical protocol records and Bitcoin input scripts agree for the covered 132. |
| Section 4.9; Table 11 | Separate decoder-evaluation sets of 40 and 96 swaps | v5: 9/40 and 46/96 complete; ETH partitions agree for 24/40 and 84/96; all 40 and 96 protocol-referenced BTC outputs agree. These latter checks include undecoded inputs. v9 explains the one 2-wei guard rejection in the 96-set without changing its result. |
| Section 4.10; Table 12 | Eleven selected refund cases, including three partial refunds with BTC claims | v6: naive BTC sum 9.49019624 versus 4.74509812 BTC from recipient outputs; excess 4.74509812 BTC. Eleven ETH refunds agree. The other eight cases do not establish zero BTC payments. |
| Section 4.11 | One selected Litecoin deposit with two BTC payments, from 166 records in nine Thor25M files | v8: 10,326 + 16,752 = 27,078 satoshi under both accounting methods. This is output accounting, not Litecoin input-decoder coverage. |
| Section 5; Table 13 | Interpretation of the preceding results; no new observations | The evidence and limits above apply. Do not pool swaps, graph rows, control executions, selected Bitcoin transactions and deposits into one accuracy denominator. |

The frozen v5 comparator reports **984 distinct complete records removed** for the no-overrides variant. Revision 9 reports **985 removed rows** because one baseline record occurs twice. Preserve that historical v5 result; do not edit it to force the new wording. The final row totals remain unchanged.

## 2. Files and SHA-256

Keep each archive in a separate new extraction. The two v5 parts are distribution containers, not independently runnable packages. Their archive digests differ from the digest of the complete ZIP they reconstruct.

| File | SHA-256 |
| --- | --- |
| `VCA_review_v5_part1.zip` | `09c1bb67a27531661acb40f09cc4a160ef8b609127ad1bf04d26917ef63f3585` |
| `VCA_review_v5_part2.zip` | `2d30ec5dbd7c4d63ce51705c31252be852080753daea048096f62a002aaaf7e0` |
| `assemble_review.py` | `82fbeef70ef30ab31addb0f7a632bedd1a809f5ad63f9381d50512eca2b18329` |
| Reconstructed `VCA_anonymous_review_v5_20260908.zip` | `1a474cf43851d37bd8740671af7c2755d41190ff476ffc5437b11910afc2c1dc` |
| `VCA_refund_supplement_v6_20260908.zip` | `855bcdc6eabaafbe6d2ee995ab3a3f52606995ac350bccb560a4671d746eacbc` |
| `VCA_equal_outputs_supplement_v7r2_20260908.zip` | `db6457da4e327b6af13cd928ebc9f31300d99e0b61be10d9743a55e6fcd7909a` |
| `VCA_protocol_multiplicity_supplement_v8_20260908.zip` | `730a6d7695eb134bf1a022251bd26ee5bc7262f204ceb5883f7d7c6cb5976240` |

For `VCA_integrity_supplement_v9_20260908.zip`, use the final archive digest supplied separately with its release (`DOWNLOAD_MANIFEST.json` and `SHA256SUMS`). An archive cannot meaningfully authenticate itself using a checksum supplied only inside that same archive; retain the checksum received through the review channel.

For example, PowerShell computes a downloaded file's digest with `Get-FileHash -Algorithm SHA256 -LiteralPath VCA_review_v5_part1.zip`. Compare the complete hexadecimal value before continuing. Put both v5 parts and the assembler together; from that download directory run:

```text
python -B assemble_review.py
```

Expected complete ZIP size: **146,333,570 bytes**. Verify its digest above, then extract it. Never run experiments directly from a part ZIP.

## 3. Fast integrity review: v9

Working directory: the extracted **`VCA_integrity_review`** root. Standard-library Python **3.11+** is sufficient for the default checks; no dependency installation or chain request is needed.

```text
python -B run_checks.py --output-dir review_run
```

Use a new output directory. Expected findings:

- The five graph comparisons satisfy row and distinct-record accounting separately. Normal controls: 5 accepted; altered-total/dropped-duplicate controls: 10 rejected. The no-overrides row identity is **3,127 − 985 + 6 = 2,148**.
- The saved RPC calldata's third ABI word is **26,710,257,243,351,728 wei**; saved transaction `value` is **26,710,257,243,351,726 wei**. Their hexadecimal endings are `6ab0` and `6aae`. The 2-wei difference is already in the archived response, before VCA normalization.
- Recorded value and calldata agree with the preserved RPC fields for all **96** predictions. No change is observed between those saved bytes and recorded inputs. This does not determine the upstream cause of the two different values.

The detailed reports identify the input paths, raw field offsets, digests and integer conversions. The archive also carries the frozen-runtime result; the default command's recorded-input audit is not a fresh invocation of that runtime. To invoke it as well, first prepare the v5 Python environment below. In the same PowerShell session, from the v9 root use:

```powershell
python -B run_checks.py --output-dir review_run_with_runtime --with-runtime --python $VcaFrozenPython
```

Here `$VcaFrozenPython` is the resolved executable created in the next section. Expected runtime result: **96** integer values and calldata strings remain unchanged, and the original strict guard rejects the recorded 2-wei discrepancy. This is a data-path check, not a new evaluation of decoder coverage.

## 4. Base calculations: v5

Working directory: the extracted **`VCA_anonymous_review`** root. Use PowerShell for the commands with `$VcaFrozenPython`. Run one command at a time and stop on a nonzero exit code. Installing the locked environment needs network access; the research checks use saved records.

```powershell
python -B experiments/reproduction/verify_package_files.py
uv sync --frozen --extra dev --project source --python 3.12.13 --link-mode copy
$VcaFrozenPython = (Resolve-Path 'source/.venv/Scripts/python.exe').Path
& $VcaFrozenPython -X utf8 -B tools/recheck_new_experiments.py
& $VcaFrozenPython -X utf8 -B tools/recheck_revision_v1.py
```

Expected: **11,423** package files pass the hash check, then `_rechecks/RESULT.json` and `_revision_checks/RESULT.json` report `PASS`. The first checker recalculates the 40-swap, recipient-history and stop-diagnosis results; the second recalculates the 96-swap and added accounting/protocol checks and recounts saved policy/hub runs. **Recounting a saved graph is not a fresh full trace.**

For Table 6's original paired controls, still from the v5 root:

```powershell
& $VcaFrozenPython -B experiments/reproduction/check_midgard_controls_v2.py --source source --output review/reviewer_midgard_controls.json
```

Expected counts are in the mapping table above. These wrappers require their output directories to be absent. Preserve a failed directory and use a new extraction for another attempt. Keep Python optimization disabled; do not use `-O` or `-OO`.

To perform the two incidents' full traces twice, still from the v5 root, use four new run directories:

```powershell
& $VcaFrozenPython -B experiments/reproduction/replay_case.py --source source --case kelpdao --run-dir runs/kelpdao_1
& $VcaFrozenPython -B experiments/reproduction/replay_case.py --source source --case bybit --run-dir runs/bybit_1
& $VcaFrozenPython -B experiments/reproduction/replay_case.py --source source --case kelpdao --run-dir runs/kelpdao_2
& $VcaFrozenPython -B experiments/reproduction/replay_case.py --source source --case bybit --run-dir runs/bybit_2
& $VcaFrozenPython -B experiments/reproduction/verify_bundle.py --source source --runs runs --snapshot-manifest provenance/snapshot_manifest.json --output review/reviewer_full_replay.json
```

Check each `summary.json`, exit code, actual outputs and network-monitor records before the next run. The expected case outputs match the frozen references. The v5 README separately documents optional full policy/hub reruns; the default calculation commands above do not perform them.

## 5. Separate added-case archives: v6, v7r2 and v8

Keep the v5 executable variable in the same PowerShell session. Change the working directory, not the frozen Python environment, for v6 and v7r2.

| Working directory | Command | Expected fresh report |
| --- | --- | --- |
| Extracted `VCA_refund_review` root | `& $VcaFrozenPython -X utf8 -B tools/recheck_refunds.py` | `_checks/RESULT.json`: `PASS`; 237 file hashes; 11 cases/3 partial refunds; eight controls; 4.74509812 BTC overcount. |
| Extracted `VCA_equal_output_review` root | `& $VcaFrozenPython -X utf8 -B tools/recheck_real_outputs.py` | `_checks/RESULT.json`: `PASS`; 112 file hashes; three real cases; 24 primary/six separate controls; 1,200 versus 600 satoshi per selected pair. |

The v8 archive has no enclosing `VCA_*` directory. Work from its extraction root containing `reproducibility/`. It uses standard-library Python **3.11+** with RIPEMD-160 support, without the v5 environment:

```text
python -B reproducibility/protocol_multiplicity_20260908/verify_package.py
python -B reproducibility/protocol_multiplicity_20260908/replay_offline.py --work-dir ../v8-replay
```

The work directory must be new and outside the extracted package. Expected `../v8-replay/REPLAY_RESULT.json`: `PASS`, 171 package files, three successful calculations, four matching report comparisons and zero network events. The separate control groups contain 23, seven and 24 controls. The selected two payments total **27,078 satoshi**. Retain the distinction between 166 actual source rows and the pinned dataset README's historical claim of 156.

## 6. Table 6 units and reporting the run

`check_midgard_controls_v2.py` changes the **first `ETH.ETH` inbound coin amount** by one stored Midgard unit. Its amount field uses eight decimal places, so the perturbation is **10^-8 ETH**, not one wei. The metadata control changes **`actions[0].date`** by one numeric unit, which is **one nanosecond**. These units are specified by the project's generated [Coin schema](https://pkg.go.dev/gitlab.com/thorchain/midgard/openapi/generated/oapigen#Coin) and [Action schema](https://pkg.go.dev/gitlab.com/thorchain/midgard/openapi/generated/oapigen#Action), checked on 8 September 2026. The controls change in-memory copies; archived hashes remain unchanged.

Record archive digests, OS/Python versions, commands, exit codes, elapsed times and actual output paths. Preserve failures and state which optional steps were skipped. Record the operator's development participation and author assistance separately: another PC or AI session alone does not establish independent-team reproduction. Do not run archived capture scripts or alter expected results to obtain a pass.
