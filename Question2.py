# -*- coding: utf-8 -*-
""" Planetary Motion Question 2

Description: The ISS or International space station orbits earth in a period of
92 minutes, with an orbital inclination of 51.6 degrees, at a height between 300-420 km
and orbits in prograde motion. This code takes this information using the funcitons 
defined in Question 1 to output the oribit of the nearly circular
ISS orbit and output the position in lat and long on a map of the earth

    
Attributes:
    Inputs: 
        Julian Date: Ex. 2456789 is May 11, 2014 at 12:00:0000
        x: Cartesian coordinates
        y:Cartesian coordinates
        z: Cartesian coordinates
    
TODO:
    - What is the most northerly Declination of the ISS against the celestial sphere as seen by
an observer at the center of the Earth?
    - If the ISS crosses the First Point of Aries heading northward at Julian Date 2456674.5,
what is its RA and Dec as seen by an observer at the center of the Earth? 
    - What is the geodetic latitude and longitude and altitude on Julian Date 2456674.5? Plot
the longitude and latitude of the ISS for the next 3 orbits at one minute intervals. Replot
the longitude and latitude of the ISS on a map of the Earth using the matplotlib Basemap
or Cartopy toolkit.

References:
         Julian Date converter : https://aa.usno.navy.mil/data/JulianDate 
         Moon data: https://rhodesmill.org/skyfield/
Author:
    Victoria Pinnegar
"""

import Question1
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature



""" PLotting a Visual for the orbit of the ISS"""
# Constants
equator_radius = 6380  # Radius of the equator circle in km
orbit_radius = 6680  # Radius of the inclined orbit in km
inclination = 51.6  # Inclination angle in degrees

# Parameter for plotting the circles
theta = np.linspace(0, 2 * np.pi, 1000)

# Equator circle (lying in the x-y plane)
x_equator = equator_radius * np.cos(theta)
y_equator = equator_radius * np.sin(theta)
z_equator = np.zeros_like(theta)  # z=0 for the equator

# Inclined orbit circle
x_orbit = orbit_radius * np.cos(theta)
y_orbit = orbit_radius * np.sin(theta) * np.cos(np.radians(inclination))
z_orbit = orbit_radius * np.sin(theta) * np.sin(np.radians(inclination))

# Set up the 3D plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the equator circle
ax.plot(x_equator, y_equator, z_equator, label="Equator (Radius = 6380 km)", color="blue")
# Plot the inclined orbit circle
ax.plot(x_orbit, y_orbit, z_orbit, label="Inclined Orbit (51.6° Inclination, Radius = 6680 km)", color="orange")
orbit_radius = 6800
x_orbit = orbit_radius * np.cos(theta)
y_orbit = orbit_radius * np.sin(theta) * np.cos(np.radians(inclination))
z_orbit = orbit_radius * np.sin(theta) * np.sin(np.radians(inclination))

ax.plot(x_orbit, y_orbit, z_orbit, label="Inclined Orbit (51.6° Inclination, Radius = 6800 km)", color="orange")

# Configure plot appearance
ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")
# ax.set_title("3D View of Equatorial Circle and Inclined Orbit at 51.6°")
ax.legend()

# Set equal scaling for all axes for accurate representation
ax.set_box_aspect([1, 1, 1])  # Aspect ratio is 1:1:1
plt.show()




""" PLotting each minute of the orbit of the ISS over the orbit in 3D"""
#constants

radius_earth =6380000
orbit_radius = 6680000
inclination_deg = 51.6
num_points = 92
JulianDateStart = 2456674.5
SecondOrbit = 2456674.563194
ThirdOrbit = 2456674.626389

theta_time = np.linspace(0, 2*np.pi, num_points)
x_orbit = orbit_radius * np.cos(theta_time)
y_orbit = orbit_radius *np.sin(theta_time)
z_orbit = orbit_radius *np.sin(np.radians(inclination_deg))*np.sin(theta_time)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the orbit with points for each minute
ax.plot(x_orbit, y_orbit, z_orbit, label="ISS Orbit", color='blue')
ax.scatter(x_orbit, y_orbit, z_orbit, color='orange', s=20, label="Minute Markers")

# arrow_length = 1000  # Length of the arrow
# ax.quiver(radius_earth, 0, 0, 1, 0, 0, length=arrow_length, color='red', arrow_length_ratio=0.5, label="First Point of Aries")

# Set plot parameters
# ax.set_title("ISS Orbit with Inclination of 51.6° and Minute Markers")
ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")
ax.legend()
plt.show()
""" The first point within the orbit output is at the first point of Aries
which corresponds to 0 degrees Declination and 00hh 00 mm 000ss Right Ascension"""








""" Using the functions in Question 1, plotting the first three orbits of the ISS """
plt.figure()
RA = []
Dec = []
xx = []
yy = []
hh = []
for i in range(len(x_orbit)):
    RA1, Dec1 = Question1.cartesian_to_ra_dec(x_orbit[i],y_orbit[i],z_orbit[i])
    x1, y1, h1 = Question1.equatorial_to_cartographic(x_orbit[i],y_orbit[i],z_orbit[i], JulianDateStart)
    x,y,h = Question1.cartesian_to_geodetic(x1, y1, h1)
    RA.append(RA1)
    Dec.append(Dec1)
    xx.append(x)
    yy.append(y)
    hh.append(h)

plt.plot(RA, Dec, label="ISS Orbit", color='blue' )
plt.scatter(RA, Dec, color='orange', s=20, label="Minute Markers")
plt.scatter(0,0, color = 'red', marker='x', s=90, label = "First Point of Aries")
plt.xlabel("Right Ascension ($^\circ$)")
plt.ylabel("Declination ($^\circ$)")
plt.legend()


fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the orbit with points for each minute
ax.plot(xx, yy, hh, label="ISS Orbit", color='blue')
ax.scatter(xx, yy, hh, color='orange', s=20, label="Minute Markers")

arrow_length = 1000  # Length of the arrow
ax.quiver(radius_earth, 0, 0, 1, 0, 0, length=arrow_length, color='red', arrow_length_ratio=0.1, label="First Point of Aries")

# Set plot parameters
ax.set_title("ISS Orbit with Inclination of 51.6° and Minute Markers")
ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")
ax.legend()


orbit_minutes = 91 * 3 
interval = 1
plt.figure(figsize=(15, 8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.scatter(yy, xx, marker='o', label = 'First Orbit')
ax.plot(np.linspace(-180, 180, 1000), np.zeros(1000), color='gray', linestyle='--', label='Equator')
ax.set_global()
ax.gridlines(draw_labels=True)
# plt.legend()
xx1 = []
yy1 = []
hh = []
for i in range(len(x_orbit)):
    RA1, Dec1 = Question1.cartesian_to_ra_dec(x_orbit[i],y_orbit[i],z_orbit[i])
    x1, y1, h1 = Question1.equatorial_to_cartographic(x_orbit[i],y_orbit[i],z_orbit[i], SecondOrbit)
    x,y,h = Question1.cartesian_to_geodetic(x1, y1, h1)
    RA.append(RA1)
    Dec.append(Dec1)
    xx1.append(x)
    yy1.append(y)
    hh.append(h)
ax.scatter(yy1, xx1, marker='o', label = 'Second Orbit')    
    
    
xx2 = []
yy2 = []
hh = []
for i in range(len(x_orbit)):
    RA1, Dec1 = Question1.cartesian_to_ra_dec(x_orbit[i],y_orbit[i],z_orbit[i])
    x1, y1, h1 = Question1.equatorial_to_cartographic(x_orbit[i],y_orbit[i],z_orbit[i], ThirdOrbit)
    x,y,h = Question1.cartesian_to_geodetic(x1, y1, h1)
    RA.append(RA1)
    Dec.append(Dec1)
    xx2.append(x)
    yy2.append(y)
    hh.append(h)
ax.scatter(yy2, xx2, marker='o', label = 'Third Orbit')
ax.legend()

plt.figure(figsize=(15, 8))
plt.scatter(xx,yy, label = "First orbit")
plt.scatter(xx1, yy1, label = 'Second orbit')
plt.scatter(xx2, yy2, label = 'Third orbit')
plt.legend()
plt.xlabel("Latitude $(\circ)$")
plt.ylabel("Longitude $(\circ)$")

""" The geodetic latitude and Longitude are both 0 degrees, corresponding to the point at 245667.5
which is when the RA and DEC are both 0 """
