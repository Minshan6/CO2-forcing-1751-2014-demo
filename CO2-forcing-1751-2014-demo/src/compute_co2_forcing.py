from __future__ import annotations
import os, argparse, yaml, csv
import numpy as np
import pandas as pd
from .io_load import load_inputs
from .utils_irf import emissions_to_concentration_ppm, rf_myhre


def main(config_path: str):
    # === 1. Load configuration ===
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)

    y0 = cfg["period"]["start_year"]
    y1 = cfg["period"]["end_year"]
    ff_csv = cfg["paths"]["ff_csv"]
    eluc_csv = cfg["paths"]["eluc_csv"]
    out_dir  = cfg["paths"]["out_dir"]
    os.makedirs(out_dir, exist_ok=True)

    ppm_per_GtC = cfg["carbon_cycle"]["ppm_per_GtC"]
    C0_ppm      = cfg["carbon_cycle"]["C0_ppm"]
    a           = cfg["carbon_cycle"]["a"]
    tau         = cfg["carbon_cycle"]["tau"]
    k_myhre     = cfg["forcing"]["myhre_k"]
    shock       = cfg["attribution"]["shock_frac"]

    # === 2. Load emission inputs ===
    df = load_inputs(ff_csv, eluc_csv, y0, y1)
    years = df["year"].astype(int).values
    FF   = df["FF_GtC"].astype(float).values
    ELUC = df["ELUC_GtC"].astype(float).values
    TOT  = FF + ELUC

    # === 3. Baseline forcing ===
    C_baseline = emissions_to_concentration_ppm(years, TOT, ppm_per_GtC, C0_ppm, a, tau)
    RF_baseline = rf_myhre(C_baseline, C0_ppm, k_myhre)

    # === 4. Perturbations (–20%) ===
    TOT_FFshock   = (1 - shock) * FF + ELUC
    TOT_ELUCshock = FF + (1 - shock) * ELUC

    C_ffshock   = emissions_to_concentration_ppm(years, TOT_FFshock, ppm_per_GtC, C0_ppm, a, tau)
    C_elucshock = emissions_to_concentration_ppm(years, TOT_ELUCshock, ppm_per_GtC, C0_ppm, a, tau)

    RF_ffshock   = rf_myhre(C_ffshock,   C0_ppm, k_myhre)
    RF_elucshock = rf_myhre(C_elucshock, C0_ppm, k_myhre)

    # === 5. Marginal contributions (ΔRF) ===
    dRF_FF   = RF_baseline - RF_ffshock
    dRF_ELUC = RF_baseline - RF_elucshock

    RF_FF_abs   = dRF_FF
    RF_ELUC_abs = dRF_ELUC
    RF_total    = RF_FF_abs + RF_ELUC_abs

    share_FF   = RF_FF_abs / np.maximum(RF_total, 1e-12)
    share_ELUC = RF_ELUC_abs / np.maximum(RF_total, 1e-12)

    # === 6. Write absolute contributions ===
    abs_df = pd.DataFrame({
        "year": years,
        "RF_total_Wm2": RF_total,
        "RF_FF_abs_Wm2": RF_FF_abs,
        "RF_ELUC_abs_Wm2": RF_ELUC_abs,
    })
    abs_df.to_excel(os.path.join(out_dir, "co2_abs_contrib_timeseries.xlsx"), index=False)

    # === 7. Write relative contributions ===
    share_df = pd.DataFrame({
        "year": years,
        "FF_share": share_FF,
        "ELUC_share": share_ELUC,
    })
    share_df.to_excel(os.path.join(out_dir, "co2_share_timeseries.xlsx"), index=False)

    print("✅ Wrote numeric outputs: out/co2_abs_contrib_timeseries.xlsx, out/co2_share_timeseries.xlsx")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Compute global CO₂ forcing and source attribution (1751–2014)"
    )
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    main(args.config)
