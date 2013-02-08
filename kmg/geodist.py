# Copyright (C) 2013 by Ken Guyton.  All Rights Reserved.

"""Measure the distance between two coordinates.

We'll assume a plane approximation of the earth's surface so this
is only for distances small enough for that assumption to give 
useful answers.

We'll also assume a spherical model of the earth with a radius of
6371 km.
"""

__author__ = 'Ken Guyton'

import math

# Convert km to miles.  Everything will be in miles.
EARTH_RADIUS = 6371.0 * 0.621371


class GeoDist(object):
  """An object that computes approximate distances between two points.

  It assumes that the local surface of the earth is flat and also
  converts from angles (coordinates) to miles assuming the earth is
  a sphere.
  """

  def _normalize_angle(self, angle):
    """Normalize an angle onto the range 0 <= angle < 360."""

    new_angle = angle
    while new_angle >= 360.0:
      new_angle -= 360.0

    return new_angle

  def degtorad(self, deg):
    """Convert degrees to radians."""

    return self._normalize_angle(deg) * math.pi / 180.0

  def radtodeg(self, rad):
    """Convert radians to degrees."""

    return self._normalize_angle(rad * 180.0 / math.pi)

  def _angle_to_dist(self, radius, angle):
    """Convert an angle in degrees to a distance for a radius."""

    angle_rad = self.degtorad(angle)
    dist = angle_rad * radius

    return dist

  def delta_lat(self, delta_lat):
    """The distance in miles for a change in latitude."""

    return self._angle_to_dist(EARTH_RADIUS, delta_lat)

  def parallel_radius(self, lat):
    """The radius of the parallel circle at the given latitude in degrees."""

    return EARTH_RADIUS * math.cos(self.degtorad(lat))

  def delta_long(self, lat, delta_long):
    """The distance in miles at the given change in longitude at latitude."""

    return self._angle_to_dist(self.parallel_radius(lat), delta_long)

  def cartesian_dist(self, delta_x, delta_y):
    """Compute the distance between a change in x, y."""

    return math.sqrt(delta_x * delta_x + delta_y * delta_y)

  def distance(self, coord1, coord2):
    """Compute the distance between two Coordinates."""

    delta_x = self.delta_long(coord1.lat, coord1.delta_long(coord2))
    delta_y = self.delta_lat(coord1.delta_lat(coord2))

    return self.cartesian_dist(delta_x, delta_y)


class Coordinate(object):
  """A coordinate pair of lat, long."""

  def __init__(self, lat, longitude):
    """Initialize with two angles in degrees."""

    self.lat = lat
    self.long = longitude

  def delta_lat(self, other_coord):
    """Compute the difference in degrees of latitude."""

    return other_coord.lat - self.lat

  def delta_long(self, other_coord):
    """Compute the difference in degrees of longitude."""

    return other_coord.long - self.long


class GreatCircle(object):
  """Compute a distance using the great circle method."""

  def __init__(self):
    """Use a geodist object."""

    self.geodist = GeoDist()

  def sin(self, deg):
    """Compute the sine of an angle in deg."""

    return math.sin(self.geodist.degtorad(deg))

  def cos(self, deg):
    """Compute the cosine of an angle in deg."""

    return math.cos(self.geodist.degtorad(deg))

  def acos(self, dist):
    """Compute the arc cosine of a distance to an angle in  degrees."""

    return self.geodist.radtodeg(math.acos(dist))

  def distance(self, coord1, coord2):
    """Compute the distance using the great circle."""
    sinsin_lat = self.sin(coord1.lat) * self.sin(coord2.lat)
    coscos_lat = self.cos(coord1.lat) * self.cos(coord2.lat)
    cos_deltalong = self.cos(coord1.delta_long(coord2))

    angle = self.acos(sinsin_lat + coscos_lat * cos_deltalong)

    return self.geodist._angle_to_dist(EARTH_RADIUS, angle)
