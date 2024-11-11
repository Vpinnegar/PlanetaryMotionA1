# -*- coding: utf-8 -*-
"""
Planetary Motion Question 3

Description: This module is directly related to the orbital elements of eccentricity
true anomaly, and eccentric anomaly. The purpose of this module is to take in either true anomaly
and eccentricity or eccentric anomaly and eccetricity and find the final parameter.

Attributes:
    Inputs: 
        Eccentricity e: float 
        True anomaly f: float units: radians
        
    
    
TODO:
    - Take in eccentricity and true anomaly in radians and convert to eccentric anomaly
    - Take in eccentricity and eccentric anomaly and output true anomaly

"""
import math
import numpy as np

def ta_to_eccentric_a(e,f):
    """Parameters:
        Input:
            f: True anomaly float Units: Radians
            e: Eccentricity float 
        Output:
            E: Eccentric Anomaly float Units: Radians
            """
    if f > 2*np.pi:
        raise ValueError(f"The value {f} exceeds the threshold for the True anomaly. This must be within range 0 < f < 2pi.")
    if not isinstance(e, (int, float)):
        raise TypeError(f"Error: The Eccentricity ({e}) is not numeric")
    if not isinstance(f, (int, float)):
        raise TypeError(f"Error: The True Anomaly ({f}) is not numeric")
    return 2 * math.atan(math.sqrt((1 - e) / (1 + e)) * math.tan(f / 2))

## Test
e = 0.1 
f = 2
print(ta_to_eccentric_a(e,f))

        
def eccentricity_to_ta(e, E):
    """Parameters:
        Input:
            E: Eccentric anomaly float Units: Radians
            e: Eccentricity float 
        Output:
            f: True Anomaly float Units: Radians
            """
    if not isinstance(e, (int, float)):
        raise TypeError(f"Error: The Eccentricity ({e}) is not numeric")
    if not isinstance(E, (int, float)):
        raise TypeError(f"Error: The Eccentric Anomaly ({E}) is not numeric")
    return 2 * math.atan(math.sqrt((1 + e) / (1 - e)) * math.tan(E / 2))
## Test
e = 0.1 
E = 1.90696691269126843427
print(eccentricity_to_ta(e,E))
