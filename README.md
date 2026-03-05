
# Volatility Waves + Monte Carlo Paths

## Creator/Dev: tubakhxn

## What is this project about?
This Python project simulates a stochastic volatility model and visualizes it with animated 3D surfaces and multiple Monte Carlo price paths. It demonstrates:
- Evolving volatility surfaces with shocks and clustered events
- 30 animated Monte Carlo price paths
- Volatility spikes that create ripples and change path slopes
- Rotating 3D camera and strong color gradients
- Smooth animation for 400+ frames

## How to fork
1. Click the "Fork" button at the top right of the GitHub repository page.
2. Clone your forked repository to your local machine:
    ```
    git clone https://github.com/YOUR-USERNAME/Volatility-Waves-Monte-Carlo-Paths.git
    ```
3. Install Python 3.7+ if not already installed.
4. Run the simulation:
    ```
    python main.py
    ```
    Dependencies are installed automatically on first run.

## Project Structure
- `main.py` — Entry point, handles setup and animation
- `stochastic_model.py` — Volatility surface and shock generation
- `monte_carlo.py` — Monte Carlo price path simulation
- `surface_renderer.py` — Visualization and animation logic

## Output
A Python window will display two animated panels:
- **Left:** 3D volatility surface
- **Right:** Monte Carlo price paths

Enjoy exploring stochastic volatility dynamics!