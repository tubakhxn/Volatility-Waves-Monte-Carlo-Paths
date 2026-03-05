import numpy as np

def generate_vol_surface(price_levels, times, shocks):
    # Simulate volatility surface as waves with shocks
    base_vol = 0.2 + 0.1 * np.sin(np.outer(times, price_levels/10))
    for shock in shocks:
        t_idx, p_idx, intensity = shock
        base_vol[t_idx, :] += intensity * np.exp(-0.1 * (price_levels - price_levels[p_idx])**2)
    return np.clip(base_vol, 0.05, 2.0)

def generate_vol_shocks(num_times, num_prices):
    # Generate clustered volatility shocks
    shocks = []
    for t in range(0, num_times, np.random.randint(40, 80)):
        p = np.random.randint(0, num_prices)
        intensity = np.random.uniform(0.3, 1.2)
        shocks.append((t, p, intensity))
        # Clustered events
        if np.random.rand() < 0.5:
            for dt in range(1, np.random.randint(2, 5)):
                shocks.append((min(t+dt, num_times-1), p, intensity * np.random.uniform(0.5, 0.9)))
    return shocks