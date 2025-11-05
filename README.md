# 🌍 CO₂ Radiative Forcing Attribution Demo

A lightweight Python workflow for **computing global CO₂ radiative forcing** (1751–2014)  
and **attributing contributions** between **fossil fuel** and **land-use change** sources.

This mini-pipeline implements a simplified carbon-cycle–climate chain:
emissions → concentration → radiative forcing → attribution → visualization.

---

## 🧩 Repository Structure

```
.
├── compute_co2_forcing.py     # Main driver: compute CO₂ forcing and attribution
├── io_load.py                 # Load emission inputs (from CSV or synthetic data)
├── utils_irf.py               # Bern IRF kernel & forcing formulae
├── plot_outputs.py            # Visualization of outputs (stacked forcing & shares)
├── co2_ff_demo_1751_2014.csv  # Demo fossil fuel CO₂ emissions (GtC yr⁻¹)
├── co2_eluc_demo_1751_2014.csv# Demo land-use CO₂ emissions (GtC yr⁻¹)
└── config_demo.yaml           # Example configuration file (to be created by user)
```

---

## ⚙️ Workflow Overview

1. **`compute_co2_forcing.py`**  
   Loads inputs → computes atmospheric CO₂ concentrations using a Bern IRF →  
   evaluates radiative forcing (Myhre et al.) → separates marginal forcing of FF vs ELUC.

2. **`plot_outputs.py`**  
   Visualizes stacked radiative forcing and relative source contributions.

3. **`io_load.py`**  
   Handles emission inputs.  
   - If CSV files are present, reads real data.  
   - If missing, generates synthetic time series via `_toy_series()`.

4. **`utils_irf.py`**  
   Contains core numerical routines:  
   - `bern_irf_kernel()` — impulse response of the carbon cycle  
   - `emissions_to_concentration_ppm()` — convolution of emissions to CO₂ ppm  
   - `rf_myhre()` — standard logarithmic radiative forcing relationship  

---

## 📦 Dependencies

| Package | Minimum Version | Used For |
|----------|----------------|-----------|
| Python   | 3.9+           | Core language |
| NumPy    | 1.20+          | Numerical arrays |
| Pandas   | 1.4+           | Data handling |
| Matplotlib | 3.6+         | Plotting |
| PyYAML   | 6.0+           | Config file reading |
| OpenPyXL | 3.1+           | Excel export |

Install dependencies:
```bash
pip install numpy pandas matplotlib pyyaml openpyxl
```

---

## 🧠 Example Configuration (`config_demo.yaml`)

```yaml
period:
  start_year: 1751
  end_year: 2014

paths:
  ff_csv: co2_ff_demo_1751_2014.csv
  eluc_csv: co2_eluc_demo_1751_2014.csv
  out_dir: out/

carbon_cycle:
  ppm_per_GtC: 0.47
  C0_ppm: 278.0
  a: [0.217, 0.259, 0.338, 0.186]
  tau: ["inf", 172.9, 18.51, 1.186]

forcing:
  myhre_k: 5.35

attribution:
  shock_frac: 0.2   # 20% perturbation for attribution test
```

---

## 🚀 Run the Pipeline

### Step 1 – Compute Radiative Forcing

```bash
python compute_co2_forcing.py --config config_demo.yaml
```

**Outputs (Excel):**
```
out/co2_abs_contrib_timeseries.xlsx   # Absolute forcing (W m⁻²)
out/co2_share_timeseries.xlsx         # Relative shares (FF vs ELUC)
```

### Step 2 – Generate Plots

```bash
python plot_outputs.py --config config_demo.yaml
```

**Outputs (PNG):**
```
out/fig_RF_stacked.png   # Stacked FF + ELUC forcing
out/fig_RF_shares.png    # Relative contributions (%)
```

---

## 📊 Output Example

**Stacked Forcing (1751–2014):**
- Total CO₂ forcing grows quasi-logarithmically from ~0 → +2.0 W m⁻²  
- Fossil fuels dominate after 1950, reaching > 85 % share by 2014  
- Land-use forcing peaks mid-20ᵗʰ century then stabilizes  

**Relative Contributions:**
| Year | FF Share | ELUC Share |
|------|-----------|------------|
| 1850 | ~35 % | ~65 % |
| 1950 | ~70 % | ~30 % |
| 2014 | ~88 % | ~12 % |

---

## 🧪 Notes

- Designed for clarity and reproducibility, not exact GCB replication.  
- Can be extended with multi-gas forcing, time-varying IRF, or uncertainty analysis.  
- Compatible with GitHub Actions / Binder for quick demos.

---

## 📄 Citation

If used in academic work, please cite the underlying conceptual sources:

> *Myhre et al. (1998, 2001): CO₂ radiative forcing parameterization.*  
> *Joos et al. (2013): Carbon cycle response functions (Bern model).*  

---

## 🧰 Author

**Min Shan (敏)**  
Ph.D. Candidate, Peking University – College of Urban and Environmental Sciences  
Research focus: global emission inventories and aerosol–climate interactions.
