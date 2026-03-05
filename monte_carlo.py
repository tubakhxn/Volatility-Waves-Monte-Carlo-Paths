import numpy as np

def simulate_paths(num_paths, num_steps, vol_surface, price_levels):
    paths = np.zeros((num_paths, num_steps))
    paths[:, 0] = price_levels[len(price_levels)//2]
    for i in range(1, num_steps):
        vol = vol_surface[i, :]
        for j in range(num_paths):
            p_idx = int(np.clip(paths[j, i-1] - price_levels[0], 0, len(price_levels)-1))
            sigma = vol[p_idx]
            drift = 0.0
            shock = np.random.normal(drift, sigma)
            paths[j, i] = np.clip(paths[j, i-1] + shock, price_levels[0], price_levels[-1])
    return paths