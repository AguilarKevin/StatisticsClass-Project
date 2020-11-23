from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

def standardize(x, mean, standartDeviation):
        return ((x - mean) / standartDeviation)

def normalProbabilityDensity (x):
    constante = 1.0 / np.sqrt (2 * np.pi)
    return (constante * np.exp ((- x ** 2) / 2.0))


z = standardize(185, 170, 12)

print(quad (normalProbabilityDensity, np.NINF , z))