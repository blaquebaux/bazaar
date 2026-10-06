# Blaque Baux Bazaar

**EM debt & FX carry — a distinct carry premium, or a short-dollar bet (vs brics) in a bond wrapper?**

> **Not investment advice.** Educational/research software. See [DISCLAIMER](DISCLAIMER.md) and [LICENSE](LICENSE).

```bash
python3 research/bazaar_1.py   # needs Alpaca data keys in the environment
```

EM USD debt (EMB), local debt (EMLC), EM-FX carry (CEW) — distinct from the *equity* regionals (apac/emea/latam).

## Finding (conditional)
- **A real carry stream:** +3.5%/yr, Sharpe +0.42; EMB (USD) is the cleaner carry.
- **But partly a short-dollar bet:** β to USD **−0.62**, skew −1.87, and it bled in 2022's strong dollar (−21%) and gapped in March-2020 (−21%) — crash-correlated, overlapping `brics`' dollar regime.

## Verdict
**CONDITIONAL.** The USD-debt leg (EMB) is the keeper; the local/FX leg *is* a short-dollar bet. Size small, gate on the dollar regime, respect the tail. `bazaar_2` = per-country sovereign curves + an explicit high-minus-low-yield carry rank.

## Status
**Research.** Honest white-space study — verdict falls where it falls, proxy limits named, `bazaar_2` path noted. Fat-tail scorecard, causal, Alpaca SIP daily total return. No live capital.
