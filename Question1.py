# -*- coding: utf-8 -*-
""" Planetary Motion Question 1

Description: Takes in various coordinates in cartesian and outputs them into various
frame of references, including geocentric cartographic,
geodetic and celestial. Addiitonally, the conversion of
Julian Date to sidereal time is contained

Example:
        
    
Attributes:
    Inputs: 
        Julian Date: Ex. 2456789 is May 11, 2014 at 12:00:0000
        x: Cartesian coordinates
        y:Cartesian coordinates
        z: Cartesian coordinates
    
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

References:
         Julian Date converter : https://aa.usno.navy.mil/data/JulianDate 
         Moon data: https://rhodesmill.org/skyfield/
Author:
    Victoria Pinnegar
"""

import math 


def juliandate_to_GAA(julian_date):
    
    """Input: 
            Julian Date: Ex. 2456789 is May 11, 2014 at 12:00:0000
       Output:
           Angle: Ex. 177 degrees """
    if not isinstance(julian_date, (int, float)):
        raise TypeError(f"Error: The ({julian_date}) is not numeric")
    JD2000 = 2451545.0
    t = julian_date - JD2000
    T = t/36525
    gaa = 280.46061837 + 360.98564736629 * t + 0.000387933 * T**2 - (T**3) / 38710000.0
    gaa = gaa % 360
    return gaa


def cartesian_to_ra_dec(x, y, z):
    """ Input:
            x: float units: m
            y: float units: m
            z: float units: m
        Output:
            Right Ascension:float degrees
            Declination: float degrees
        """
    ### errors in input
    if not isinstance(x, (int, float)):
        raise TypeError(f"Error: The ({x}) is not numeric")
    if not isinstance(y, (int, float)):
        raise TypeError(f"Error: The ({y}) is not numeric")
    if not isinstance(z, (int, float)):
        raise TypeError(f"Error: The ({z}) is not numeric")
    
    # Calculate the distance from Earth's center to the body (radius)
    r = math.sqrt(x**2 + y**2 + z**2)
    
    # Declination in degrees
    declination = math.degrees(math.asin(z / r))
    
    # Right Ascension in degrees, ensuring the angle is between 0 and 360 degrees
    right_ascension = math.degrees(math.atan2(y, x)) % 360
    
    return right_ascension, declination


def equatorial_to_cartographic(x, y, z, julian_date):
    """ Input:
            Julian Date: float 
            x: float units: m
            y: float units: m
            z: float units: m
        Output:
            x_cartographic: float units: m
            y_cartographic: float units: m
            z_cartographic: float units: m
        """
    ### errors in input
    if not isinstance(x, (int, float)):
        raise TypeError(f"Error: The ({x}) is not numeric")
    if not isinstance(y, (int, float)):
        raise TypeError(f"Error: The ({y}) is not numeric")
    if not isinstance(z, (int, float)):
        raise TypeError(f"Error: The ({z}) is not numeric")
    if not isinstance(julian_date, (int, float)):
        raise TypeError(f"Error: The ({julian_date}) is not numeric")
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



def cartesian_to_geodetic(x, y, z):
    """ Input:
            x: float units: m
            y: float units: m
            z: float units: m
        Output:
            latitude_deg_: float units: degrees
            Longitude_deg: float units: degrees
            altitude: float units: m
        """
    ### errors in input
    if not isinstance(x, (int, float)):
        raise TypeError(f"Error: The ({x}) is not numeric")
    if not isinstance(y, (int, float)):
        raise TypeError(f"Error: The ({y}) is not numeric")
    if not isinstance(z, (int, float)):
        raise TypeError(f"Error: The ({z}) is not numeric")
    
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
    u = math.atan2((z*a),(p*b))
    lat = math.atan2(z + eprime*b*math.sin(u)**3, p-eprime*a*math.cos(u)**3)  # initial latitude approximation
    
    latitude_deg = math.degrees(lat)
    
    # Calculate altitude above the ellipsoid
    N = a / math.sqrt(1 - e2 * math.sin(lat)**2)  
    altitude = p / math.cos(lat) - N

    return latitude_deg, longitude_deg, altitude

### test case : fake

x = 6680000
y = 0
z = 0
julian_date = 2456674.5
ra, dec = cartesian_to_ra_dec(x, y, z)
xx, yy, zz = equatorial_to_cartographic(x, y, z, julian_date)
lat, long, alt = cartesian_to_geodetic(x, y, z)
print(ra, dec, xx, yy, zz, lat, long, alt)



### Test Case: Moon


from skyfield.api import load


eph = load('de421.bsp')  
earth, moon = eph['earth'], eph['moon']

# Specify the date and time (UTC)
ts = load.timescale()
time = ts.utc(2024, 9, 2, 0, 0, 0)

# Calculate position
astrometric = earth.at(time).observe(moon).apparent()
ra, dec, distance = astrometric.radec()
geocentric = astrometric.position.km
julian_date = 2460555.5
print("Geocentric Cartesian Coordinates (in km):", geocentric)
print("Right Ascension (RA):", ra)
print("Declination (Dec):", dec)

ra, dec = cartesian_to_ra_dec(geocentric[0]*1000, geocentric[1]*1000,geocentric[2]*1000)
print(ra, dec)
total_hours = ra/ 15.0
hours = int(total_hours)
total_minutes = (total_hours - hours) * 60
minutes = int(total_minutes)
total_seconds = (total_minutes - minutes) * 60
seconds = total_seconds
print(hours, minutes, seconds, dec)
# c, v, b = equatorial_to_cartographic(geocentric[0]*1000, geocentric[1]*1000,geocentric[2]*1000, julian_date)
# k,l,j = cartesian_to_geodetic(c, v, b)
k,l,j = cartesian_to_geodetic(geocentric[0]*1000, geocentric[1]*1000,geocentric[2]*1000)

# print(c,k)
# print(v,l)
# print(b, j)
""" The output of the functions using the cartesian coordinates for the moon have
the same RA and Dec. 
"""
