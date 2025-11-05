# CO₂ Forcing Demo

This repository provides a simple Python workflow to calculate **CO₂ radiative forcing** from fossil fuel (FF) and land-use (ELUC) emissions between **1751–2014**.

## Purpose
It demonstrates how to convert emission time series into CO₂ concentration and radiative forcing, and to separate contributions from different sources.

## Files Overview

- **compute_co2_forcing.py** – Main script that reads emissions, computes concentrations and forcing, and outputs results to Excel files.
- **io_load.py** – Loads input emission data from CSV or generates toy data if missing.
- **utils_irf.py** – Provides Bern carbon-cycle impulse response and Myhre CO₂ forcing functions.
- **plot_outputs.py** – Generates plots for total CO₂ forcing and source contributions.

## Example Usage

1. Prepare configuration file `config_demo.yaml` (see repo or modify paths).
2. Run forcing calculation:
   ```bash
   python compute_co2_forcing.py --config config_demo.yaml
   ```
3. Plot outputs:
   ```bash
   python plot_outputs.py --config config_demo.yaml
   ```

Outputs (Excel + PNG) will appear in the directory defined by `out_dir` in the config file.
