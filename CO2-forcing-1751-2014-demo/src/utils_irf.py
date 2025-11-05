from __future__ import annotations
import numpy as np

def bern_irf_kernel(years: np.ndarray, a, tau) -> np.ndarray:
    """
    Discrete Bern IRF kernel g(t), length = len(years). years is ascending (e.g., 1751..2014).
    a: list of weights; tau: list of time constants (use string 'inf' for the constant term).
    """
    t = years - years[0]
    g = np.zeros_like(t, dtype=float)
    for ai, ti in zip(a, tau):
        if isinstance(ti, str) and ti.lower() == "inf":
            g += ai
        else:
            g += ai * np.exp(-t / float(ti))
    return g

def emissions_to_concentration_ppm(years: np.ndarray, E_GtC_yr: np.ndarray,
                                   ppm_per_GtC: float, C0_ppm: float,
                                   a, tau) -> np.ndarray:
    """
    Convolve annual emissions (GtC/yr) with IRF kernel and convert to ppm, then add C0.
    Returns CO2 concentration (ppm) for each year.
    """
    g = bern_irf_kernel(years, a, tau)
    T = len(years)
    excess = np.zeros(T, dtype=float)
    for t in range(T):
        k = np.arange(t+1)
        excess[t] = (E_GtC_yr[:t+1][::-1] * g[:t+1]).sum() * ppm_per_GtC
    return C0_ppm + excess

def rf_myhre(C_ppm: np.ndarray, C0_ppm: float, k: float) -> np.ndarray:
    """RF = k * ln(C/C0)"""
    return k * np.log(np.maximum(C_ppm, 1e-12) / C0_ppm)
