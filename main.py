import sys
import subprocess
import importlib

def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = importlib.import_module(package)

for pkg in ["numpy", "matplotlib"]:
    install_and_import(pkg)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

from stochastic_model import generate_vol_surface, generate_vol_shocks
from monte_carlo import simulate_paths
from surface_renderer import animate_surfaces

if __name__ == "__main__":
    animate_surfaces()