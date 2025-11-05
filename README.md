# CO₂ Forcing Demo (1751–2014)

This repository provides a minimal, transparent example of computing **global CO₂ radiative forcing (1751–2014)** based on fossil-fuel and land-use emissions, using a reduced-form impulse response model.  
It is designed for reproducibility and demonstration purposes only.

---

## 📁 Repository Structure

```
CO2-forcing-demo-1751-2014/
│
├── data/
│   ├── co2_ff_demo_1751_2014.csv      ← fossil fuel CO₂ emissions (GtC yr⁻¹)
│   └── co2_eluc_demo_1751_2014.csv    ← land-use CO₂ emissions (GtC yr⁻¹)
│
├── src/
│   ├── io_load.py                     ← input data loader
│   ├── utils_irf.py                   ← Bern IRF and radiative forcing functions
│   ├── compute_co2_forcing.py         ← main script: compute forcing & attribution
│   └── plot_outputs.py                ← plotting: stacked & relative contribution figures
│
├── config.yaml                        ← configuration file
└── README.md
```

---

## ⚙️ How to Run

### 1️⃣ Install dependencies
```bash
pip install numpy pandas matplotlib pyyaml openpyxl
```

### 2️⃣ Run the forcing computation
```bash
python -m src.compute_co2_forcing --config config.yaml
```

Outputs (in `out/`):
- **co2_abs_contrib_timeseries.xlsx** — absolute contributions (W m⁻²)
- **co2_share_timeseries.xlsx** — relative shares (%)

### 3️⃣ Plot results
```bash
python -m src.plot_outputs --config config.yaml
```

Outputs (in `out/`):
- **fig_RF_stacked.png** — stacked area plot (FF + ELUC → Total RF)
- **fig_RF_shares.png** — relative contribution trends

---

## 🧠 Model Description

The demo implements a **Bern-type impulse response function (IRF)** for the carbon cycle and the **Myhre et al. (1998)** logarithmic radiative forcing equation:

\[
RF = k \times \ln \left(\frac{C}{C_0}\right)
\]

with parameters:
- `a` and `tau` for multi-timescale carbon retention,
- `ppm_per_GtC = 0.4716981`,
- `k_myhre = 5.35`.

The scripts compute baseline CO₂ concentration and forcing, apply ±20 % emission perturbations for fossil fuel and land-use sectors, and estimate their **absolute and relative contributions** to total forcing.

---

## 📜 License & Citation

MIT License.  
If you reuse or reference this code, please cite as:

> Shan, M. (2025). *CO₂ Forcing Demo (1751–2014)*. GitHub Repository: [https://github.com/Minshan6/CO2-forcing-demo-1751-2014](https://github.com/Minshan6/CO2-forcing-demo-1751-2014)

---

## 👤 Author

**Min Shan**  
Ph.D. Candidate, Peking University  
Email: minshan@stu.pku.edu.cn  
Research interests: global emission modeling, aerosol–climate interactions, reduced-form Earth system models.
