# -*- coding: utf-8 -*-
"""
Planetary Motion Question 5

Description: This module multiplies the position and velocity vectors through the angles omega, i and Omega,
transforming it to the heliocentric form. 

    
Attributes:
    Inputs: 
        Positions components x , y, z: float  unit: AU
        Velocity Components , vy, vz: float Units: AU/yr
        Arguement of periapsis omega: float Units: radians
        Inclination i: float UNits: radians
        Longitude of ascending node Omega: float Units: radians
    
    
TODO:
    -  uses the rotation matrix method to rotate both the position and
velocity vectors from the question above through the angles ω, i and Ω in that order around
the appropriate axes as discussed in class in Chapter 3. 
"""

import math
import numpy as np
import Question4

def rotate_oiO(x, y, z, vx, vy, vz, omega, i, Omega):
    """ Input:
            x: float units: AU
            y: float units: AU
            z: float units: AU
            vx: float units: AU/yer
            vy: float units: AU/yr
            vz: float units: AU/yr
            omega: float units: radians
            i: float untis: radians
            OMega: float units: radians
        Output:
            Right Ascension:float degrees
            Declination: float degrees
        """
    #Error Check
    if not isinstance(x, (int, float)):
        raise TypeError(f"Error: The ({x}) is not numeric")
    if not isinstance(y, (int, float)):
        raise TypeError(f"Error: The ({y}) is not numeric")
    if not isinstance(z, (int, float)):
        raise TypeError(f"Error: The ({z}) is not numeric")
    if not isinstance(vx, (int, float)):
        raise TypeError(f"Error: The ({vx}) is not numeric")
    if not isinstance(vy, (int, float)):
        raise TypeError(f"Error: The ({vy}) is not numeric")
    if not isinstance(vz, (int, float)):
        raise TypeError(f"Error: The ({vz}) is not numeric")
    if not isinstance(omega, (int, float)):
        raise TypeError(f"Error: The ({omega}) is not numeric")
    if not isinstance(i, (int, float)):
        raise TypeError(f"Error: The ({i}) is not numeric")
    if not isinstance(Omega, (int, float)):
        raise TypeError(f"Error: The ({Omega}) is not numeric")
    if i > np.pi:
        raise ValueError(f"The value {i} exceeds the threshold for the True anomaly. This must be within range  0 < f < pi.")
    # rotate around z using arguemennt of perhelion, aligns the perihelion
    R_omega = np.array([
        [np.cos(omega), -np.sin(omega), 0],
        [np.sin(omega), np.cos(omega), 0],
        [0, 0, 1]])

    # Rotation matrix around x using inclination, so angled correctly relative to reference plane
    R_i = np.array([
        [1, 0, 0],
        [0, np.cos(i), -np.sin(i)],
        [0, np.sin(i), np.cos(i)]])

    # Rotation matrix around z using Longitude of ascending node.
    R_Omega = np.array([
        [np.cos(Omega), -np.sin(Omega), 0],
        [np.sin(Omega), np.cos(Omega), 0],
        [0, 0, 1]])
    R_combined = R_Omega @ R_i @ R_omega
    pos_vector = np.array([x, y, z])
    vel_vector = np.array([vx, vy, vz])
    pos_rotated = R_combined @ pos_vector
    vel_rotated = R_combined @ vel_vector
    return {
        'x_rotated': pos_rotated[0],
        'y_rotated': pos_rotated[1],
        'z_rotated': pos_rotated[2],
        'vx_rotated': vel_rotated[0],
        'vy_rotated': vel_rotated[1],
        'vz_rotated': vel_rotated[2]
    }

