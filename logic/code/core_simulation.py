# Layer 2: Executable Code - From ctindale's essay
import numpy as np

def simulate_reserve_erosion(years=15, shock=0.15):
    q = np.cumsum(np.random.normal(0.01, 0.02, years)) + shock  # REER appreciation
    s_T = 0.25 - 0.08 * q                                       # tradable investment ↓
    C = np.cumsum(s_T * 0.6) + 1.5                              # complexity builds with lag
    A = 0.9 * (C / C.max())                                     # conversion efficiency
    p = 0.05 + 0.45 * (1 - A)                                   # fragility ↑
    return {"q": q, "tradable_inv": s_T, "complexity": C, "fragility": p}

print("Simulation ready. Agents can now run counterfactuals, change parameters, and extend the model.")
# Full regressions, ECI replication, and charts can be added here
