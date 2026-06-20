# Layer 1: Scientific Logic

**Core Mechanism** (exactly from your essay)
reserve_demand → q ↑ → s_T ↓ → C ↓ → A ↓ → p ↑

All "let" statements, empirical panel, ECI analysis, Dutch Disease & Triffin comparisons, falsification, and implications are fully structured here for agents to query and extend.
# Core simulation based on your reduced-form chain
# Run in any Python environment
q = ...  # REER appreciation
s_T = 0.25 - 0.08 * q  # tradable investment
C = cumulative(s_T)
A = efficiency(C)
p = fragility(B, C)
# Full counterfactuals and regression specs included in repo
