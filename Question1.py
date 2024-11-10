# -*- coding: utf-8 -*-
""" Planetary Motion Question 1

Description: This module...

Example:
        
    
Attributes:
    Inputs: Julian Date, x, y,z, 
    
TODO:
    - Accept Julian data and return angle between first point of aries and Greeenwich meridian
    - accept cartesian x, y, z coordinates of a body in a geocentric equatorial coordinate
system with its origin at the Earth’s centre, its z-axis along the north pole and its x-axis out
through the First Point of Aries and returns the Right Ascension and Declination as seen
from the Earth’s centre.
    - accepts the Cartesian x, y, z coordinates of a body in the geocentric equatorial coordinate
system above and the Julian date, and returns the Cartesian x, y, z coordinates in a geocentric
cartographic coordinate system with the same origin but with its z-axis along the north pole
and its x-axis out along the Greenwich meridian.
    - accepts Cartesian x, y, z coordinates in the geocentric cartographic coordinate system
above and returns the geodetic latitude, longitude and altitude above the WGS84 reference
ellipsoid.

"""

import math 


def juliandate_to_GAA(julian_date):
    """Input: 
            Julian Date: Ex. 2456789
       Output:
           Angle: Ex. 177 degrees """
           
    JD2000 = 2451545.0
    t = julian_date - JD2000
    T = t/36525
    gaa = 280.46061837 + 360.98564736629 * t + 0.000387933 * T**2 - (T**3) / 38710000.0
    gaa = gaa % 360
    return gaa


def cartesian_to_ra_dec(x, y, z):
    """ Input:
            x: 
            y: 
            z:
        Output:
            Right Ascension:
            Declination:
        """
    
    # Calculate the distance from Earth's center to the body (radius)
    r = math.sqrt(x**2 + y**2 + z**2)
    
    # Declination in degrees
    declination = math.degrees(math.asin(z / r))
    
    # Right Ascension in degrees, ensuring the angle is between 0 and 360 degrees
    right_ascension = math.degrees(math.atan2(y, x)) % 360
    
    return right_ascension, declination


def equatorial_to_cartographic(x, y, z, julian_date):
    # Calculate GST in degrees
    gst_degrees = juliandate_to_GAA(julian_date)
    # Convert GST to radians
    gst_radians = math.radians(gst_degrees)
    
    # Rotation matrix for rotation about z-axis by GST radians
    cos_gst = math.cos(gst_radians)
    sin_gst = math.sin(gst_radians)
    
    # Apply the rotation matrix
    x_cartographic = cos_gst * x + sin_gst * y
    y_cartographic = -sin_gst * x + cos_gst * y
    z_cartographic = z  # z-axis remains the same in both systems
    
    return x_cartographic, y_cartographic, z_cartographic



# def cartesian_to_geodetic(x, y, z):
#     # WGS84 ellipsoid constants
#     a = 6378137.0  # semi-major axis in meters
#     f = 1 / 298.257223563  # flattening
#     e2 = 2 * f - f ** 2  # square of eccentricity
#     b = a * (1 - f)  # semi-minor axis

#     # Calculate longitude in radians
#     longitude = math.atan2(y, x)
#     longitude_deg = math.degrees(longitude)
    
#     # Initialize parameters for latitude iteration
#     p = math.sqrt(x**2 + y**2)  # distance from z-axis
#     lat = math.atan2(z, p * (1 - e2))  # initial latitude approximation
#     lat_prev = 0
#     epsilon = 1e-12  # convergence tolerance
    
#     # Iteratively calculate latitude
#     while abs(lat - lat_prev) > epsilon:
#         lat_prev = lat
#         N = a / math.sqrt(1 - e2 * math.sin(lat)**2)  # prime vertical radius of curvature
#         lat = math.atan2(z + e2 * N * math.sin(lat), p)

#     # Convert latitude to degrees
#     latitude_deg = math.degrees(lat)
    
#     # Calculate altitude above the ellipsoid
#     N = a / math.sqrt(1 - e2 * math.sin(lat)**2)  # final prime vertical radius of curvature
#     altitude = p / math.cos(lat) - N

#     return latitude_deg, longitude_deg, altitude
import numpy as np
def cartesian_to_geodetic(x, y, z):
    # WGS84 ellipsoid constants
    a = 6378137.0 
    b = 6356752.314245# semi-major axis in meters
    f = 1 -b/a  # flattening
    e2 = (a**2 - b**2)/a**2  # square of eccentricity
    # b = a * (1 - f)  # semi-minor axis
    eprime = (a**2)/(b**2)-1
    # Calculate longitude in radians
    longitude = math.atan2(y, x)
    longitude_deg = math.degrees(longitude)
    
    # Initialize parameters for latitude iteration
    p = math.sqrt(x**2 + y**2)# distance from z-axis
    u = math.atan((z*a)/(p*b))
    lat = math.atan2(z + eprime*b*math.sin(u)**3, p-eprime*a*math.cos(u)**3)  # initial latitude approximation
    lat_prev = 0
    epsilon = 1e-12  # convergence tolerance
    
    # Iteratively calculate latitude
    # while abs(lat - lat_prev) > epsilon:
    #     lat_prev = lat
    #     N = a / math.sqrt(1 - e2 * math.sin(lat)**2)  # prime vertical radius of curvature
    #     lat = math.atan2(z + e2 * N * math.sin(lat), p)

    # Convert latitude to degrees
    latitude_deg = math.degrees(lat)
    
    # Calculate altitude above the ellipsoid
    N = a / math.sqrt(1 - e2 * math.sin(lat)**2)  # final prime vertical radius of curvature
    altitude = p / math.cos(lat) - N

    return latitude_deg, longitude_deg, altitude
