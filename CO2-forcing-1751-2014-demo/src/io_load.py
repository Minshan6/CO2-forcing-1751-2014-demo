from __future__ import annotations
import os
import numpy as np
import pandas as pd

def _toy_series(years, start, end, noise=0.0, seed=0):
    rng = np.random.default_rng(seed)
    base = np.linspace(start, end, len(years))
    return np.clip(base + rng.normal(0, noise, len(years)), 0, None)

def load_inputs(ff_csv: str, eluc_csv: str, y0: int, y1: int) -> pd.DataFrame:
    """Load demo CO₂ emission inputs for fossil fuel (FF) and land-use (ELUC)."""
    years = np.arange(y0, y1 + 1)
    df = pd.DataFrame({"year": years})

    # --- Fossil fuel CO₂ (FF)
    if os.path.exists(ff_csv):
        ff = pd.read_csv(ff_csv)
        ff = ff[["year", "FF_GtC"]].dropna()
        df = df.merge(ff, on="year", how="left")
    else:
        df["FF_GtC"] = _toy_series(years, 0.02, 9.5, noise=0.1, seed=1)

    # --- Land-use CO₂ (ELUC)
    if os.path.exists(eluc_csv):
        lu = pd.read_csv(eluc_csv)
        lu = lu[["year", "ELUC_GtC"]].dropna()
        df = df.merge(lu, on="year", how="left")
    else:
        df["ELUC_GtC"] = _toy_series(years, 0.8, 1.2, noise=0.05, seed=2)

    # --- Clean and fill ---
    df["FF_GtC"] = df["FF_GtC"].interpolate().fillna(0.0).clip(lower=0)
    df["ELUC_GtC"] = df["ELUC_GtC"].interpolate().fillna(0.0).clip(lower=0)

    return df
