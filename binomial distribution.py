import numpy as np

# Parametres
n = 10      # nombre d'essais
p = 0.5      # probabilité de succès
size = 1000     # nombre d'expériences

# Simulation(Monte Carlo)
samples = np.random.binomial(n, p, size)

print(samples[:10])  # 10 premiers résultats

import matplotlib.pyplot as plt

plt.hist(samples, bins=range(n+2), density=True, edgecolor='black')
plt.xlabel("Nombre de succés")
plt.ylabel("Probabilité")
plt.title("simulation du la distribution binomial")
plt.show()


from scipy.stats import binom
#calcule la probabilité exact
x = np.arange(0, n+1)
theoretical = binom.pmf(x, n, p)

plt.hist(samples, bins=range(n+2), density=True, alpha=0.6, label="Simulation")
plt.plot(x, theoretical, 'o-', label="valeur theorique")
plt.xlabel("Nombre de succés")
plt.ylabel("Probabilité")
plt.legend()
plt.show()


trials = np.random.rand(size, n) < p
manual_samples = trials.sum(axis=1)
