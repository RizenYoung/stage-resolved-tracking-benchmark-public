# Increment Covariance Structure

The available per-track CSV stores `terminal_txy` but not the component residuals `delta t_x` and `delta t_y`. The 3x3 covariance below is therefore a symbolic design target, while the empirical table reports only the reduced `(delta t_xy, delta q/p)` covariance.

```latex
\Sigma_{\Delta} =
\begin{bmatrix}
\Sigma_{t_x t_x} & \Sigma_{t_x t_y} & \rho_{xq}\sqrt{\Sigma_{t_x t_x}\Sigma_{qq}}\\
\Sigma_{t_x t_y} & \Sigma_{t_y t_y} & \rho_{yq}\sqrt{\Sigma_{t_y t_y}\Sigma_{qq}}\\
\rho_{xq}\sqrt{\Sigma_{t_x t_x}\Sigma_{qq}} & \rho_{yq}\sqrt{\Sigma_{t_y t_y}\Sigma_{qq}} & \Sigma_{qq}
\end{bmatrix},
\qquad \rho_{\cdot q}=\mathcal{O}(\omega\Delta z).
```

The slope block inherits the sec^4(theta) amplification in the z-chart, while the slope-q/p entries are left as rho-parameterized couplings. No numeric value is assigned to those unavailable entries.

## Empirical 2x2 Reduction

| sample | method | n | cov(delta txy, delta q/p) | Pearson r | Spearman rho |
|---|---:|---:|---:|---:|---:|
| all_tracks | baseline | 1488 | -0.010198 | -0.00260739 | 0.0751157 |
| all_tracks | replacement | 1488 | -0.180542 | -0.125091 | -0.128375 |
| near_window_truth_txy_ge4 | baseline | 357 | 0.255878 | 0.0392568 | 0.00201631 |
| near_window_truth_txy_ge4 | replacement | 357 | -0.657367 | -0.248634 | -0.374453 |
