# -*- coding: utf-8 -*-
"""
Planetary Motion Question 7

Description: This module multiplies the position and velocity vectors through the angles omega, i and Omega,
transforming it to the heliocentric form. 

Example:
        
    
Attributes:
    Inputs: 
        Semi Major Axis a:
        Eccentricity e: 
        True Anomaly f:
            radians
        Standard Gravitational Parameter \mu:
            G(m1 + m2)
        Arguement of periapsis omega: float in radians
        Inclination i: float radians
        Longitude of ascending node Omega: float in radians
    
    
TODO:
    -  plot the orbits of the planets and pluto on the heliocentric celiptic 
    using the given orbital elements
    - plot themm at intervals of 1 degree in true anomaly
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Question3 as Q3
import Question4 as Q4
import Question5 as Q5
import Question6 as Q6


### Table of planetary data
## with halley and ceres
planetary_data = {
    'Planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Halley', 'Ceres'],
    'a (AU)': [0.38709893, 0.72333199, 1.00000011, 1.52366231, 5.20336301, 9.53707032, 19.19126393, 30.06896348, 39.48168677, 17.87, 2.7658],
    'e': [0.20563069, 0.00677323, 0.01671022, 0.09341233, 0.04839266, 0.05415060, 0.04716771, 0.00858587, 0.24880766, 0.967125, 0.078],
    'i (deg)': [7.00487, 3.39471, 0.00005, 1.85061, 1.30530, 2.48446, 0.76986, 1.76917, 17.14175, 162, 10.607],
    'Omega (deg)': [48.33167, 76.68069, -11.26064, 49.57854, 100.55615, 113.71504, 74.22988, 131.72169, 110.30347, 59.70, 80.7],
    'omega (deg)': [77.45645, 131.53298, 102.94719, 336.04084, 14.75385, 92.43194, 170.96424, 44.97135, 224.06676,112.61, 73.1],
    'L (deg)': [252.25084, 181.97973, 100.46435, 355.45332, 34.40438, 49.94432, 313.23218, 304.88003, 238.92881,0, 0]
}
## without halley and ceres
planetary_data1 = {
    'Planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'],
    'a (AU)': [0.38709893, 0.72333199, 1.00000011, 1.52366231, 5.20336301, 9.53707032, 19.19126393, 30.06896348, 39.48168677],
    'e': [0.20563069, 0.00677323, 0.01671022, 0.09341233, 0.04839266, 0.05415060, 0.04716771, 0.00858587, 0.24880766],
    'i (deg)': [7.00487, 3.39471, 0.00005, 1.85061, 1.30530, 2.48446, 0.76986, 1.76917, 17.14175],
    'Omega (deg)': [48.33167, 76.68069, -11.26064, 49.57854, 100.55615, 113.71504, 74.22988, 131.72169, 110.30347],
    'omega (deg)': [77.45645, 131.53298, 102.94719, 336.04084, 14.75385, 92.43194, 170.96424, 44.97135, 224.06676],
    'L (deg)': [252.25084, 181.97973, 100.46435, 355.45332, 34.40438, 49.94432, 313.23218, 304.88003, 238.92881]
}

df = pd.DataFrame(planetary_data1)

## take all planets as zero mass
mu_s = 4*np.pi**2

### for all planets each planets
plt.figure(figsize=(10,10))
for _, row in df.iterrows():
    a = row['a (AU)']
    e = row['e']
    i = np.radians(row['i (deg)'])
    Omega = np.radians(row['Omega (deg)'])
    omega = np.radians(row['omega (deg)'])
    f_values = np.linspace(0, 2 * np.pi, 360)
    x_orbit = []
    y_orbit = []
    for f in f_values:
        state = Q6.calculatecartesian(a, e, i, Omega, omega, f, mu_s)
        x_orbit.append(state['position'][0])
        y_orbit.append(state['position'][1])
        # if f % (np.pi / 180) == 0:  # Add ticks at every 1 degree (in radians)
        #     plt.plot(state['position'][0], state['position'][1], 'o', markersize=90, color='red')
    plt.scatter(x_orbit, y_orbit, label=row['Planet'])
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')

plt.legend()
plt.grid(True)
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.show()

df = pd.DataFrame(planetary_data)

## take all planets as zero mass
mu_s = 4*np.pi**2

### for all planets each planets
plt.figure(figsize=(10,10))
for col, row in df.iterrows():
    a = row['a (AU)']
    e = row['e']
    i = np.radians(row['i (deg)'])
    Omega = np.radians(row['Omega (deg)'])
    omega = np.radians(row['omega (deg)'])
    f_values = np.linspace(0, 2 * np.pi, 360)
    x_orbit = []
    y_orbit = []
    for f in f_values:
        state = Q6.calculatecartesian(a, e, i, Omega, omega, f, mu_s)
        x_orbit.append(state['position'][0])
        y_orbit.append(state['position'][1])
        # if f % (np.pi / 180) == 0:  # Add ticks at every 1 degree (in radians)
        #     plt.plot(state['position'][0], state['position'][1], 'o', markersize=90, color='red')
    # plt.plot(x_orbit, y_orbit, label=row['Planet'])
    plt.scatter(x_orbit, y_orbit, label=row['Planet'])
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.legend()
plt.grid(True)
# plt.xlim(-5,5)
# plt.ylim(-5,5)
plt.show()