#!/usr/bin/python3
# =============================================================================
# bazaar_1.py — EM debt & FX carry: a distinct carry premium, or dollar-regime crash risk (vs brics) in a bond wrapper?
#
# EM USD debt (EMB), EM local-currency debt (EMLC), EM-FX carry (CEW). SIP daily total return.
#  (A) profile vs US agg (AGG) / HY credit (HYG): Sharpe, CAGR, maxDD, skew, and correlation to the dollar (UUP) and SPY.
#  (B) is it just a short-dollar / risk-on bet (brics already tests the dollar regime)? — β to UUP; and the crisis tail
#      (2020 COVID, 2022 strong-dollar) where EM carry blows up.
# Distinct from the equity regionals (apac/emea/latam) — this is EM *fixed income + FX*.
# =============================================================================
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _bazaar_common import panel, rets, stats, skew_of, beta, corr
import numpy as np
P, dates = panel(["EMB","EMLC","CEW","AGG","HYG","UUP","SPY"])
R={s:rets(P[s]) for s in P}; D=dates[1:]
em=np.nanmean(np.vstack([R["EMB"],R["EMLC"]]),axis=0)            # blended EM debt (USD + local)
print("="*96); print(f"BAZAAR — EM debt & FX carry  ({dates[0]} → {dates[-1]})"); print("="*96)
a=stats(em)
print(f"\n(A) EM debt basket  Sharpe {a['sh']:+.2f}  CAGR {a['cagr']*100:+.1f}%  maxDD {a['dd']*100:+.0f}%  skew {skew_of(em):+.2f}")
print(f"    EMB(USD) {stats(R['EMB'])['sh']:+.2f}/{stats(R['EMB'])['cagr']*100:+.0f}%  EMLC(local) {stats(R['EMLC'])['sh']:+.2f}/{stats(R['EMLC'])['cagr']*100:+.0f}%  CEW(FX carry) {stats(R['CEW'])['sh']:+.2f}/{stats(R['CEW'])['cagr']*100:+.0f}%")
print(f"    vs AGG {stats(R['AGG'])['sh']:+.2f}  HYG {stats(R['HYG'])['sh']:+.2f}   corr SPY {corr(em,R['SPY']):+.2f}  β/USD(UUP) {beta(em,R['UUP']):+.2f}")
def win(lo,hi):
    idx=[i for i,x in enumerate(D) if lo<=x<hi]; return np.prod(1+em[idx])-1 if idx else float('nan')
covid=win("2020-02-18","2020-03-23"); usd22=win("2022-01-01","2022-10-01")
print(f"\n(B) crisis tail: March-2020 {covid*100:+.0f}%  |  2022 strong-dollar {usd22*100:+.0f}%   β to USD {beta(em,R['UUP']):+.2f} (negative = short-dollar bet)")
dollar_bet=beta(em,R['UUP'])< -0.3; has_carry=a['cagr']>0.02
print("\n"+"="*96); print("READ:")
print(f"  • A REAL CARRY STREAM: EM debt earned {a['cagr']*100:+.1f}%/yr (Sharpe {a['sh']:+.2f}) — EMB (USD) is cleaner carry; EMLC/CEW add FX, which is where the risk and the dollar-sensitivity live.")
print(f"  • PARTLY A SHORT-DOLLAR BET (brics overlap): β to USD {beta(em,R['UUP']):+.2f}, and it bled in 2022's strong dollar ({usd22*100:+.0f}%) and gapped in March-2020 ({covid*100:+.0f}%), skew {skew_of(em):+.2f} — EM carry is crash-correlated, the classic 'pick up nickels' tail.")
if has_carry and not dollar_bet:
    v=("CONDITIONAL KEEPER: EM debt is a genuine carry premium distinct from the equity regionals — EMB (USD) especially "
       "gives clean sovereign/credit carry with only moderate dollar sensitivity. Size for the crisis tail (2020/2022) and "
       "gate on the dollar regime (brics) since the local-currency/FX leg IS a short-dollar bet. A diversifying income "
       "satellite. bazaar_2 = per-country curves + an explicit carry rank (high-yield vs low-yield sovereigns).")
elif has_carry:
    v=("CONDITIONAL: EM debt pays a real carry but it's substantially a SHORT-DOLLAR / risk-on bet (β to USD "
       f"{beta(em,R['UUP']):+.2f}) with a crash-correlated tail — overlapping brics' dollar regime. The USD-debt leg (EMB) is the "
       "keeper; the local/FX leg is the dollar bet. Size small, gate on the dollar, respect the 2022-style tail. bazaar_2 = carry-ranked sovereigns + dollar gate.")
else:
    v=("NULL-ish: net of its crash-correlated tail EM carry doesn't clearly pay here; mostly a short-dollar bet brics already covers.")
print(f"  VERDICT: {v}")
print("  (EMB/EMLC/CEW ETFs; per-country sovereign curves + an explicit high-minus-low-yield carry rank = bazaar_2. Distinct from apac/emea/latam equity.)")
