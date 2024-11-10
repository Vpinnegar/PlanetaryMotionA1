# -*- coding: utf-8 -*-
"""

Planetary Motion Question 4

Description: This module...

Example:
        
    
Attributes:
    Inputs: 
        Semi Major Axis a:
        Eccentricity e: 
        True Anomaly f:
            radians
        Standard Gravitational Parameter \mu:
            G(m1 + m2)
    
    
TODO:
    - Given µ = G(m1 + m2), and the orbital elements a, e and the true anomaly f in radians,
use the equations below to construct a subroutine to calculate the x, y positions and velocities
of m2 relative to m1 (the central mass) in the orbital plane.

"""
import math
import numpy as np
import Question3
import numpy as np

def orbitposition_velocity(a, e, f, mu):
    #Check for error 
    if not isinstance(e, (int, float)):
        raise TypeError(f"Error: The Eccentricity ({e}) is not numeric")
    if not isinstance(f, (int, float)):
        raise TypeError(f"Error: The True Anomaly ({f}) is not numeric")
    if not isinstance(a, (int, float)):
        raise TypeError(f"Error: The Semi-Major Axis ({a}) is not numeric")
    if not isinstance(f, (int, float)):
        raise TypeError(f"Error: The Standard gravitational parameter ({mu}) is not numeric")
    if f > 2*(np.pi):
        raise ValueError(f"The value {f} exceeds the threshold for the True anomaly. This must be within range 0 < f < 2pi.")
    # mean motion
    n = np.sqrt(mu/ a**3)
    #Eccentric anomaly
    E = Question3.ta_to_eccentric_a(e, f)
    
    #postion calculations
    x = a*(np.cos(E)-e)
    y = a * np.sqrt(1 - e**2) * np.sin(E)
    z = 0
    
    #Velocities
    vx = -a * n * np.sin(E) / (1 - e * np.cos(E))
    vy = a * np.sqrt(1 - e**2) * n * np.cos(E) / (1 - e * np.cos(E))
    vz = 0
    return {
        'x': x,
        'y': y,
        'z': z,
        'vx': vx,
        'vy': vy,
        'vz': vz,
        'n':n,
        'E':E
    }

a = 1  # in AU
e = 0.1
f = np.radians(45)  # true anomaly in radians
mu = 4*np.pi**2  # gravitational parameter for Earth in km^3/s^2

result = orbitposition_velocity(a, e, f, mu)
print("Positions", result['x'], result['y'], result['z'])
print("Velocities ", result['vx'], result['vy'], result['vz'])













