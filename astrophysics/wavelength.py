import matplotlib.pyplot as plt
import numpy as np
from numpy import e

c = 299792458 # m/s
v = input("starting velocity:/t") # m/s

def redshift(v, wavelength):
	return (v/c + 1)* wavelength

old_wavelength = input("starting wavelength:\t")  # in nm

wavelength = redshift(v, old_wavelength)
print(f'redshifted wavelength:\t{wavelength}\ndelta:\t\t\t\t\t{old_wavelength-wavelength}')


# Mostra il colore RGB
def campana(x, a, b):
	exponent = e ** (-((x - a) ** 2) / (2 * b ** 2))
	exponent = int(exponent*255)
	if exponent > 255: exponent = 255
	elif exponent < 0: exponent = 0
	return exponent

x = (wavelength/1000)*255

color = [
	campana(x, 255, 63),
	campana(x, 127, 63),
	campana(x, 0, 63),
]
print(color)
plt.imshow([[np.array(color)]])
plt.axis('off')
plt.show()
