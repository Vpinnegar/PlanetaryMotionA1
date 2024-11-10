# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 03:41:14 2024

@author: starv
"""

import math

def true_to_eccentric_anomaly(e, f):
    # Calculate E using the formula
    E = 2 * math.atan(math.sqrt((1 - e) / (1 + e)) * math.tan(f / 2))
    return E

# Example usage:
eccentricity = 0.5  # example eccentricity
true_anomaly = math.radians(45)  # example true anomaly in radians
eccentric_anomaly = true_to_eccentric_anomaly(eccentricity, true_anomaly)
print(f"Eccentric Anomaly: {eccentric_anomaly:.6f} radians")


def eccentric_to_true_anomaly(e, E):
    # Calculate f using the formula
    f = 2 * math.atan(math.sqrt((1 + e) / (1 - e)) * math.tan(E / 2))
    return f

# Example usage:
eccentricity = 0.5  # example eccentricity
eccentric_anomaly = math.radians(30)  # example eccentric anomaly in radians
true_anomaly = eccentric_to_true_anomaly(eccentricity, eccentric_anomaly)
print(f"True Anomaly: {true_anomaly:.6f} radians")
