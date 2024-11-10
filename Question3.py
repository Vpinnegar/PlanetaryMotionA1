# -*- coding: utf-8 -*-
"""
Planetary Motion Question 3

Description: This module...

Example:
        
    
Attributes:
    Inputs: 
        Eccentricity e: radians
        True anomaly f: radians
    
    
TODO:
    - Take in eccentricity and true anomaly in radians and convert to eccentric anomaly
    - Take in eccentricity and eccentric anomaly and output true anomaly

"""
import math
import numpy

def ta_to_eccentric_a(e,f):
    """Parameters:
            f: True anomaly in Radians
            e: Eccentricity in Radians """
    if f > 2*np.pi:
        raise ValueError(f"The value {f} exceeds the threshold for the True anomaly. This must be within range 0 < f < 2pi.")
    return 2 * math.atan(math.sqrt((1 - e) / (1 + e)) * math.tan(f / 2))
        
def eccentricity_to_ta(e, E):
    """ Paramters:
            e: Eccentricity in Radians
            E: Eccentric Anomaly in radians"""
    return 2 * math.atan(math.sqrt((1 + e) / (1 - e)) * math.tan(E / 2))
