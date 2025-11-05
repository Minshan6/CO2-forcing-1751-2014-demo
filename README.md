# CO₂ Forcing Attribution Demo (1751–2014)

This repository provides a reproducible demonstration of how fossil-fuel and land-use CO₂ emissions have contributed to the historical evolution of global radiative forcing from 1751 to 2014.
The workflow combines GEMS fossil-fuel CO₂ emissions with OSCAR-based land-use change (ELUC) data to compute and visualize the total and source-specific CO₂ radiative forcing.

## Overview

1. **Input data**
   - `data/gems_co2_1751_2014.csv` — fossil fuel and cement CO₂ emissions (GEMS)
   - `data/oscar_eluc_1751_2014.csv` — land-use change (ELUC) CO₂ emissions (OSCAR)

2. **Computation**
   - `src/compute_co2_forcing.py` — integrates emissions → concentration → forcing → source attribution

3. **Visualization**
   - `src/plot_outputs.py` — stacked-area and relative-share figures

## Installation

```bash
pip install numpy pandas matplotlib pyyaml openpyxl
```

## Usage

### Step 1: Compute forcing
```bash
python src/compute_co2_forcing.py --config config.yaml
```

### Step 2: Plot results
```bash
python src/plot_outputs.py --config config.yaml
```

## Outputs

- `out/co2_abs_contrib_timeseries.xlsx` — absolute RF contributions (FF, ELUC, total)
- `out/co2_share_timeseries.xlsx` — relative contributions (%)
- `out/fig_RF_stacked.png` — stacked forcing evolution
- `out/fig_RF_shares.png` — relative contribution trends

## Method Summary

Based on Joos et al. (2013) impulse response function and Myhre et al. (1998) forcing equation:
RF = 5.35 × ln(C / C₀), where C₀ = 278 ppm.

## Contact

Author: **Min Shan**  
Affiliation: College of Urban and Environmental Sciences, Peking University  
Email: minshan@stu.pku.edu.cn
