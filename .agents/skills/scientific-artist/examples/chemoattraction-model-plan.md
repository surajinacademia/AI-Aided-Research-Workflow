# Chemoattraction Model — Physics and Mathematics

## 1. Overview

All model variants implement the same core physical idea: each cell steers its orientation direction toward nearby neighbors. The mechanism is a discrete angular torque computed from the spatial configuration of neighboring cells. The cell orientation $\theta_i$ of cell $i$ evolves as a noisy angular random walk with a bias term $\tau_i$ that accumulates contributions from all neighbors within a sensing radius. There are $N$ cells with positions $\mathbf{r}_i=(x_i,y_i)$. Each cell has an orientation (heading) angle $\theta_i\in[0,2\pi)$. For any pair $(i,j)$ define relative components $\Delta x_{ij}=x_j-x_i$ and $\Delta y_{ij}=y_j-y_i$, separation distance $d_{ij}=\|\mathbf{r}_j-\mathbf{r}_i\|$, and the direction-from-$i$ angle $\theta_{ij}=\operatorname{atan2}(\Delta y_{ij},\Delta x_{ij})$. The angular noise is $\eta_i\sim\mathcal{N}(0,\sigma^2)$ at every timestep. Chemoattraction strength is $\kappa$, the sensing cutoff is $r_c$ (implemented as parameter `chemo_region` in the code), and $\nu$ is the distance-decay exponent.

## 2. Canonical Chemoattraction Kernel (production model)

The steering (torque) $\tau_i$ for cell $i$ is computed from neighbors within the sensing cutoff $r_c$ as

$$\tau_i = \sum_{\substack{j \neq i \\ d_{ij} \leq r_c}} \frac{\sin(\theta_{ij}-\theta_i)}{d_{ij}^{\nu}}.$$

The orientation updates via

$$\theta_i(t+1) = \left[\theta_i(t) + \eta_i + \kappa\,\tau_i\right] \bmod 2\pi,$$

where $\eta_i \sim \mathcal{N}(0,\sigma^2)$.

## 3. Physical Interpretation

### The $\sin(\theta_{ij} - \theta_i)$ coupling kernel

The argument $\theta_{ij} - \theta_i$ is the angular difference between the direction to neighbor $j$ and cell $i$'s current orientation. The sine function maps this to a signed torque:

- $\theta_{ij} - \theta_i = 0$ or $\pi$: neighbor is directly ahead or behind — **zero torque**, no steering.
- $\theta_{ij} - \theta_i = +\pi/2$: neighbor is $90°$ to the left — **maximum positive torque**, cell turns left.
- $\theta_{ij} - \theta_i = -\pi/2$: neighbor is $90°$ to the right — **maximum negative torque**, cell turns right.

### Distance weighting and the $\nu$ exponent

The factor $1/d_{ij}^\nu$ makes close neighbors dominate the steering signal. For $\nu = 1$ (the default), the influence decays as $1/d$; for $\nu > 1$, the sensing becomes increasingly local; for $\nu < 1$ distant neighbors retain more influence. Setting $\nu = 0$ gives uniform weighting over the sensing disk.

### Role within the full model

The chemoattraction term $\kappa \tau_i$ is additive in the heading update. It competes with angular noise $\eta_i \sim \mathcal{N}(0, \sigma^2)$. The dimensionless ratio $\kappa / \sigma$ controls whether cells coherently align (large $\kappa/\sigma$) or undergo essentially uncorrelated random walks (small $\kappa/\sigma$).

## 4. Physical Limitations of the Current Kernel

1. **Not an explicit chemoattractant-to-gradient response.** There is no chemical field; the "influence" of cell $j$ on cell $i$ is purely geometric.
2. **Torque grows with neighbor count.** A cell surrounded by $k$ equidistant neighbors receives torque $k/d_0^\nu$, whereas a gradient-based response gives torque bounded in $[-1, 1]$.
3. **No decay physics (except at $\nu = 1$).** For general $\nu$, the exponent has no mechanistic origin.
4. **Positional neighbor-alignment, not contact guidance.** The current model steers toward the weighted geometric centroid of all neighbors within $r_c$.

## 5. Physically Grounded Model — Cell-Secreted Chemoattractant Field

### 5.1 The chemical field

Each cell $j$ continuously secretes a chemoattractant (e.g., VEGF) at rate $c_0$. In the steady state:

$$D_c \nabla^2 C - k_d C = -c_0 \sum_{j} \delta(\mathbf{r} - \mathbf{r}_j)$$

The Green's function:

$$C(\mathbf{r}) = \frac{c_0}{2\pi D_c} \sum_{j} K_0\!\left(\frac{|\mathbf{r} - \mathbf{r}_j|}{\lambda}\right)$$

where $\lambda = \sqrt{D_c / k_d}$ is the diffusion length.

### 5.2 Gradient and steering torque

$$\nabla C_i(\mathbf{r}_i) = -\frac{c_0}{2\pi D_c \lambda} \sum_{j \neq i} K_1\!\left(\frac{d_{ij}}{\lambda}\right) \frac{\mathbf{r}_i - \mathbf{r}_j}{d_{ij}}$$

The angular torque:

$$\boxed{\tau_i = \sin\!\left(\phi_{\nabla C_i} - \theta_i\right)}$$

where $\phi_{\nabla C_i} = \operatorname{atan2}\!\left(\partial_y C_i,\, \partial_x C_i\right)$.

### 5.3 Heading update

$$\theta_i(t+1) = \left[\theta_i(t) + \eta_i + \kappa \sin\!\left(\phi_{\nabla C_i} - \theta_i\right)\right] \bmod 2\pi$$

### 5.4 Power-law approximation

For $r \ll \lambda$, $K_1(r/\lambda) \approx \lambda / r$, giving:

$$\nabla C_i^{\text{(approx)}} \approx -\frac{c_0}{2\pi D_c} \sum_{j \neq i} \frac{\mathbf{r}_i - \mathbf{r}_j}{d_{ij}^2}$$

### 5.5 Comparison

| Aspect | Canonical neighbor-torque | Secreted-field model |
|---|---|---|
| What cell $i$ processes | Each neighbor $j$ separately | Aggregate gradient $\nabla C_i$ |
| Torque expression | $\sum_j \sin(\theta_{ij} - \theta_i) / d_{ij}^\nu$ | $\sin(\phi_{\nabla C_i} - \theta_i)$ |
| Torque range | Unbounded (grows with neighbor count) | Always $\in [-1, 1]$ |
| Physical meaning | Geometry-directed sine alignment | Gradient chemotaxis |
| Decay physics | Ad hoc exponent $\nu$ | $K_1(r/\lambda)$ from diffusion equation |
| Free parameters | $\kappa$, $\nu$, $r_c$ | $\kappa$, $\lambda$ (or $\gamma$), $r_c$ |

### 5.6 Parameters

| Symbol | Name | Physical meaning | Default |
|---|---|---|---|
| $\lambda$ | `decay_length` | $\sqrt{D_c / k_d}$; spatial range of chemoattractant | 3.0 |
| $\gamma$ | `decay_exp` | Power-law approximation exponent; $\gamma=1$ is 2D near-field limit | 1 |
| $\kappa$ | `kappa` | Steering coupling strength | 0.01 |
| $r_c$ | `chemo_region` | Cutoff beyond which field contributions are ignored | 3.0 |
| $c_0$ | `secretion` | Per-cell secretion rate (can be absorbed into $\kappa$) | 1 |
