import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from stochastic_model import generate_vol_surface, generate_vol_shocks
from monte_carlo import simulate_paths

PRICE_LEVELS = np.linspace(80, 120, 40)
NUM_TIMES = 400
NUM_PATHS = 30

TIMES = np.arange(NUM_TIMES)

SHOCKS = generate_vol_shocks(NUM_TIMES, len(PRICE_LEVELS))
VOL_SURFACE = generate_vol_surface(PRICE_LEVELS, TIMES, SHOCKS)

PATHS = simulate_paths(NUM_PATHS, NUM_TIMES, VOL_SURFACE, PRICE_LEVELS)

fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

surf = [None]
lines = []

# Color map for volatility
cmap = plt.get_cmap('plasma')

# Initial surface
def init_surface():
    ax1.clear()
    X, Y = np.meshgrid(PRICE_LEVELS, TIMES)
    Z = VOL_SURFACE
    surf[0] = ax1.plot_surface(X, Y, Z, cmap=cmap, edgecolor='none', alpha=0.9)
    ax1.set_xlabel('Price Level')
    ax1.set_ylabel('Time')
    ax1.set_zlabel('Volatility')
    ax1.set_title('Stochastic Volatility Surface')
    ax1.view_init(elev=30, azim=45)

# Initial paths
def init_paths():
    ax2.clear()
    for i in range(NUM_PATHS):
        line, = ax2.plot([], [], lw=2, alpha=0.7)
        lines.append(line)
    ax2.set_xlim(0, NUM_TIMES)
    ax2.set_ylim(PRICE_LEVELS[0], PRICE_LEVELS[-1])
    ax2.set_title('Monte Carlo Price Paths')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Price')

init_surface()
init_paths()

# Animation update

def update(frame):
    # Animate surface
    if surf[0] is not None:
        surf[0].remove()
    X, Y = np.meshgrid(PRICE_LEVELS, TIMES)
    Z = VOL_SURFACE.copy()
    # Add ripples for shocks
    for shock in SHOCKS:
        t_idx, p_idx, intensity = shock
        if t_idx <= frame:
            Z[t_idx, :] += intensity * np.exp(-0.1 * (PRICE_LEVELS - PRICE_LEVELS[p_idx])**2)
    surf[0] = ax1.plot_surface(X, Y, Z, cmap=cmap, edgecolor='none', alpha=0.9)
    ax1.view_init(elev=30, azim=45 + frame * 0.2)
    # Animate paths
    for i, line in enumerate(lines):
        line.set_data(np.arange(frame), PATHS[i, :frame])
        # Color gradient by volatility
        if frame < NUM_TIMES:
            p_idx = int(np.clip(PATHS[i, frame-1] - PRICE_LEVELS[0], 0, len(PRICE_LEVELS)-1))
            color = cmap(np.clip(VOL_SURFACE[frame-1, p_idx]/2.0, 0, 1))
            line.set_color(color)
    return [surf[0]] + lines

def animate_surfaces():
    anim = FuncAnimation(fig, update, frames=NUM_TIMES, interval=30, blit=False)
    plt.tight_layout()
    plt.show()
