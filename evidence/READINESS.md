# Readiness matrix

| Mandatory proof | Code path | Test or network proof | Status |
|---|---|---|---|
| Complete source anchoring | `_anchor` | deployment source digest + live open transaction | PASS |
| Changed forecast rejection | `_resolve` digest equality | source guard asserted in test suite | PASS |
| Different outcome host | `resolve_forecast` | stored forecast and outcome URLs | PASS |
| Deterministic score | integer score formula | executable Brier tests + score `90` readback | PASS |
| Duplicate ID cannot overwrite | `open_forecast` | ERROR transaction and unchanged readback | PASS |
| Final browser uses deployed address | `docs/index.html` | canonical Pages build loaded live score; no console errors or horizontal overflow | PASS |
