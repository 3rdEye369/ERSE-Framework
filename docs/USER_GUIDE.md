# ERSE Core Engine: Customization & Parametric Analysis Guide

Welcome to the open verification engine for the Eruptive, Resonant Solar Engine (ERSE) Framework. Because this framework functions as a living document, independent researchers are encouraged to stress-test our equations by modifying input parameters to match varying astrophysical scenarios.

## 🛠 Variables You Should Modify

To experiment with different planetary scales or stellar environments, open `src/erse_core_engine.py` and modify the following localized parameters inside the class methods:

### 1. Solar Z-Pinch Modification (`run_chapter1_zpinch`)
*   `M_core`: Change this value to simulate different planetary core births (e.g., `M_core = 6.42e23` for a Mars-scale core or `M_core = 4.87e24` for a Venus-scale core).
*   `T_core`: Alter the exit core temperature based on different stellar layers (e.g., `T_core = 2.0e7` for deeper thermonuclear environments).

### 2. Ignition Shockwave Densities (`run_chapter2_jeans_collapse`)
*   `rho_0`: The ambient density of the primitive nebula. Increase this (`e.g., 5.0e-9`) to simulate high-mass stellar nurseries, which will dynamically lower the required Jeans Mass for gas giant creation.
*   `T_frost`: Adjust the temperature boundary of the system's volatile line to observe how it shifts the boundary of Jovian world collapse.

### 3. Fission Fuel Calculations (`run_chapter5_fission_storm`)
*   `M_anomalous_Xe129`: Adjust the target mass of Xenon-129 to model different atmospheric saturation levels across the inner rocky planets or moons.
*   `Y_xe129`: Change this based on alternative fissile models (e.g., `0.061` for Plutonium-239 fast-fission channels).

## 🖥 Running and Forking the Code
1. Ensure you have Python 3.8+ and NumPy installed (`pip install numpy`).
2. Run the script from your terminal: `python src/erse_core_engine.py`
3. If your structural parameters yield stable alternative configurations, commit your changes, update the data logs, and push a pull request to the decentralized network.
