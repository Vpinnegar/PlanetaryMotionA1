# -*- coding: utf-8 -*-
"""
Planetary Motion Question 6

Description: This module multiplies the position and velocity vectors through the angles omega, i and Omega,
transforming it to the heliocentric form. 

Example:
        
    
Attributes:
    Inputs: 
        Semi Major Axis a: Units: AU
        Eccentricity e: Units: dimensionless
        True Anomaly f: Units: radians
            
        Standard Gravitational Parameter \mu: Units: AU^3 yr^-2 M_s^-1
            G(m1 + m2)
        Arguement of periapsis omega: float Units: radians
        Inclination i: float Units: radians
        Longitude of ascending node Omega: float Units:radians
    
    
TODO:
    -  uses the rotation matrix method to rotate both the position and
velocity vectors from the question above through the angles ω, i and Ω in that order around
the appropriate axes as discussed in class in Chapter 3. 
"""

import math
import numpy as np
import Question4 as Q4
import Question5 as Q5

def calculatecartesian(a, e, i, Omega, omega, f, mu):
    """ Input:
            a: Semi major axis float units: AU
            e: Eccentricty float units: dimensionless
            f: True Anomaly float units: radians
            mu: Standard gravitational constant float units:  AU^3 yr^-2 M_s^-1
            omega: float units: radians
            i: float untis: radians
            OMega: float units: radians
        Output:
            x: x position Units: AU
            y: y position Units: AU
            z: z position Units: AU
            vx: x velocty Units: AU/yr
            vy: y velocty Units: AU/yr
            vz: z velocty Units: AU/yr
            """
    pandv = Q4.orbitposition_velocity(a, e, f, mu)
    heliopandv = Q5.rotate_oiO(pandv['x'], pandv['y'], pandv['z'], pandv['vx'], pandv['vy'], pandv['vz'], omega, i, Omega)
    return {
        'position':np.array([heliopandv['x_rotated'], heliopandv['y_rotated'], heliopandv['z_rotated']]),
        'velocity':np.array([heliopandv['vx_rotated'], heliopandv['vy_rotated'], heliopandv['vz_rotated']])
    }
a = 10000  # in km
e = 0.1
i = np.radians(45)  # inclination in radians
Omega = np.radians(60)  # longitude of the ascending node in radians
omega = np.radians(30)  # argument of periapsis in radians
f = np.radians(45)  # true anomaly in radians
mu = 398600 

state = calculatecartesian(a, e, i, Omega, omega, f, mu)
print("Position Vector:", state['position'])
print("Velocity Vector:", state['velocity'])

