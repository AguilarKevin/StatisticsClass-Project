from calc.confidence_interval import ConfidenceInterval
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as st

x1, x2 = ConfidenceInterval.calc(6,100,12.05, 0.1)
print(x1,x2)

z_x1, z_x2 = ConfidenceInterval.calcZValues(95)
mu, sigma = 0, 1 # media y desvio estandar

normal = st.norm(mu, sigma)
x = np.linspace(normal.ppf(0.01),
                normal.ppf(0.99), 100)
fp = normal.pdf(x) # Función de Probabilidad
plt.plot(x, fp)

f = np.linspace(normal.ppf(z_x1),
                normal.ppf(z_x2), 100)
fp = normal.pdf(f) # Función de Probabilidad

y1 = np.sin(2 * np.pi * x)
plt.fill_between(f, 0,fp , facecolor='orange', alpha=0.5)

plt.title('Intervalo de confianza')
plt.show()