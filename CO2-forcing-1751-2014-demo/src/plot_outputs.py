from __future__ import annotations
import os, argparse, yaml
import pandas as pd
import matplotlib.pyplot as plt


def plot_stacked_forcing(abs_df, out_png):
    """Stacked-area plot: total RF = FF + ELUC"""
    plt.figure(figsize=(9, 4.5))
    x = abs_df["year"].values
    plt.stackplot(
        x,
        abs_df["RF_FF_abs_Wm2"],
        abs_df["RF_ELUC_abs_Wm2"],
        labels=["Fossil Fuel CO₂", "Land-Use CO₂"],
        alpha=0.85
    )
    plt.plot(x, abs_df["RF_total_Wm2"], "k-", lw=1.5, label="Total RF")
    plt.xlabel("Year")
    plt.ylabel("Radiative Forcing (W m$^{-2}$)")
    plt.title("Global CO₂ Radiative Forcing (1751–2014): FF + ELUC")
    plt.legend(loc="upper left", frameon=False)
    plt.tight_layout()
    plt.savefig(out_png, dpi=300)
    plt.close()


def plot_relative_shares(share_df, out_png):
    """Line plot of relative contributions"""
    plt.figure(figsize=(9, 4.5))
    x = share_df["year"].values
    plt.plot(x, 100 * share_df["FF_share"], lw=2.2, label="Fossil Fuel (%)")
    plt.plot(x, 100 * share_df["ELUC_share"], lw=2.2, label="Land-Use (%)")
    plt.xlabel("Year")
    plt.ylabel("Relative Contribution (%)")
    plt.title("Relative Contributions of FF vs Land-Use CO₂ to Total Forcing (1751–2014)")
    plt.ylim(0, 100)
    plt.grid(alpha=0.3)
    plt.legend(loc="best", frameon=False)
    plt.tight_layout()
    plt.savefig(out_png, dpi=300)
    plt.close()


def main(config_path):
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)
    out_dir = cfg["paths"]["out_dir"]

    # Read from XLSX files
    abs_df = pd.read_excel(os.path.join(out_dir, "co2_abs_contrib_timeseries.xlsx"))
    share_df = pd.read_excel(os.path.join(out_dir, "co2_share_timeseries.xlsx"))

    plot_stacked_forcing(abs_df, os.path.join(out_dir, "fig_RF_stacked.png"))
    plot_relative_shares(share_df, os.path.join(out_dir, "fig_RF_shares.png"))

    print("✅ Wrote: out/fig_RF_stacked.png, out/fig_RF_shares.png")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Plot CO₂ forcing and source attribution from XLSX outputs"
    )
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    main(args.config)
