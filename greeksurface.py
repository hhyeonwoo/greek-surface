import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.stats import norm

def gamma(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2)*T) / (sigma * np.sqrt(T))
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))


S = np.linspace(50, 150, 100)  
T = np.linspace(0.01, 1, 100)  
S, T = np.meshgrid(S, T)
K = 100
r = 0.01
sigmas = np.linspace(0.1, 0.8, 60)  

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = [ax.plot_surface(S, T, gamma(S, K, T, r, sigmas[0]), cmap="viridis")]

def update(i):
    ax.clear()
    ax.set_zlim(0, 0.03)
    ax.set_title(f"Gamma Surface at σ = {sigmas[i]:.2f}")
    ax.set_xlabel("Stock Price")
    ax.set_ylabel("Time to Maturity")
    ax.set_zlabel("Gamma")
    surf[0] = ax.plot_surface(S, T, gamma(S, K, T, r, sigmas[i]), cmap="viridis")

ani = FuncAnimation(fig, update, frames=len(sigmas), interval=100)
plt.show()
