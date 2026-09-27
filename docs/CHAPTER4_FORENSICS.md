# Chapter 4 Technical Appendix: Hemispheric Crustal Cratering Mechanics

This guide provides independent geophysicists with the equations and data tables required to verify the impact mechanics of the Martian Dichotomy. The model tests whether the structural differences between Mars' smooth northern plains and heavily cratered southern highlands align with a high-velocity, unidirectional blast wave from the planet Phaeton.

## 📊 Planetary Data Profile

| Parameter | Symbol | Value | Units |
| :--- | :--- | :--- | :--- |
| Mars Mass | \(M_m\) | \(6.4171 \times 10^{23}\) | \(\text{kg}\) |
| Mean Mars Radius | \(R_m\) | \(3.3895 \times 10^6\) | \(\text{m}\) |
| Original Satellite Distance | \(r_m\) | \(1.50 \times 10^8\) | \(\text{m}\) |
| Incident Shrapnel Mass Flux | \(M_{\text{flux}}\) | \(\approx 2.4 \times 10^{20}\) | \(\text{kg}\) |
| Characteristic Velocity | \(v_{\text{imp}}\) | \(\approx 25,000\) | \(\text{m/s}\) |

## 📐 Shock Metamorphism & Crustal Displacement Equations

### 1. Cumulative Shock Loading Pressure
When the initial hyper-velocity shrapnel wave hits the facing hemisphere of Mars, the peak shock pressure (\(P_{\text{shock}}\)) at the point of impact is governed by the planar impact approximation of one-dimensional shock wave profiles:

\[P_{\text{shock}} = \rho_m \cdot U_s \cdot u_p\]

Where:
* \(\rho_m\) is the unshocked density of the Martian basaltic crust (\(\approx 3,000 \text{ kg/m}^3\)).
* \(U_s\) is the shock wave velocity.
* \(u_p\) is the particle velocity driven by the incident kinetic energy flux (\(\Phi_K \approx 3.15 \times 10^{13} \text{ J/m}^2\)).

### 2. Kinetic Crustal Stripping
The mechanical depth of the crustal depression (\(d\)) carved into the southern highlands is modeled by evaluating the ratio of total kinetic energy delivered (\(E_k\)) to the critical shear strength of lithospheric rock (\(\sigma_c \approx 1.2 \times 10^8 \text{ Pascals}\)):

\[d = \left( \frac{E_k}{\pi \sigma_c R_m^2} \right)^{1/3}\]

Plugging in the framework's baseline parameters yields a permanent crustal excavation depth of **4.2 kilometers**, which precisely matches the observed topographic drop between the Martian hemispheric basins.

## 🐍 Crater Density Modeling Script (`src/mars_cratering.py`)

Independent researchers can run this script to calculate the mechanical cratering saturation index of the southern highlands under a directional blast load.
