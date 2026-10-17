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

Deployment coordinates and finalized transactions are written to `deployment.json` and `evidence/live-run.json` after StudioNet verification.
