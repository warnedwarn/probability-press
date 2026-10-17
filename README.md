# Probability Press

## A forecast should leave a bruise when it misses

Probability Press is a public calibration desk. It freezes a probability before an event resolves, binds the complete forecast source by SHA-256, and later asks GenLayer validators to apply a precommitted resolution rule to a separately hosted outcome record. Contract code computes the Brier score; the model cannot write or improve it.

### Plate sequence

1. `open_forecast` verifies that the source explicitly anchors the event and integer probability, then locks the claim, criteria, source origin, digest, and resolution time.
2. `resolve_forecast` re-fetches the forecast, rejects a changed digest, retrieves an outcome from a different host, and reaches `OCCURRED`, `DID_NOT_OCCUR`, or `INDETERMINATE`.
3. A determinate outcome becomes `SCORED`; an incomplete or conflicting record becomes `UNRESOLVED` with no invented score.

The integer score is `(prediction_millis - outcome_millis)^2 / 1000`, producing 0 (perfect) through 1000 (worst). A lower number is better.

### Interface

The browser is a forensic light table, not a contract-argument dashboard. Forecast and outcome sit as documentary plates; the score appears under a magnifying lens. The public page reads without a wallet and requests a wallet only for writes. `SUBMITTED`, `ACCEPTED`, and `FINALIZED` are distinct states.

### Verify locally

```text
python -m pytest -q
set PYTHONUTF8=1
genvm-lint contracts/contract.py
```

Fixtures are operator-controlled technical records. Different hosts demonstrate origin and digest enforcement; they are not represented as independent publishers.

### Verified StudioNet plate

- Contract: [`0xFEeBE219B47E08D814Ab24Ad73193FF646113196`](https://explorer-studio.genlayer.com/address/0xFEeBE219B47E08D814Ab24Ad73193FF646113196)
- Live forecast: `PRESS-1792250613`, final state `SCORED`, outcome `OCCURRED`, Brier score `0.090`
- Open forecast: [`0x679e…b0e5`](https://explorer-studio.genlayer.com/transactions/0x679eb38e07c6a50e0cb4256f452505060d086270cf39617f04dbc4245b85b0e5)
- Duplicate-ID rejection: [`0xd204…31c1`](https://explorer-studio.genlayer.com/transactions/0xd204cbf1606aed3f55ca565c63579e23027ced3d5ac0bc0800e033cd63b031c1)
- Final resolution: [`0x86b7…2542`](https://explorer-studio.genlayer.com/transactions/0x86b7a91b68829455ec91fbacf8a9b23438f80bf0f726d58f1310598515612542)

Exact source digest, deployment transaction, and stored readback live in `deployment.json` and `evidence/live-run.json`.
