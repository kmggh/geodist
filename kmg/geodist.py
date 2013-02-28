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
from kmg.angle import AngleRad
from kmg.angle import AngleDeg

# Convert km to miles.  Everything will be in miles.
EARTH_RADIUS = 6371.0 * 0.621371


class GeoDist(object):
  """An object that computes approximate distances between two points.

  It assumes that the local surface of the earth is flat and also
  converts from angles (coordinates) to miles assuming the earth is
  a sphere.

  All input angles are expected to be Angle objects.
  """

  def delta_lat_miles(self, delta_lat):
    """The distance in miles for a change in latitude."""

    return delta_lat.dist_from_radius(EARTH_RADIUS)

  def parallel_radius(self, lat):
    """The radius of the parallel circle at the given latitude in degrees."""

    return EARTH_RADIUS * lat.cos()

  def delta_long_miles(self, lat, delta_long):
    """The distance in miles at the given change in longitude at latitude."""

    return delta_long.dist_from_radius(self.parallel_radius(lat))

  def cartesian_dist(self, delta_x, delta_y):
    """Compute the distance between a change in x, y."""

    return math.sqrt(delta_x * delta_x + delta_y * delta_y)

  def distance(self, coord1, coord2):
    """Compute the distance between two Coordinates."""

    delta_x = self.delta_long_miles(coord1.lat, coord1.delta_long(coord2))
    delta_y = self.delta_lat_miles(coord1.delta_lat(coord2))

    return self.cartesian_dist(delta_x, delta_y)


class Coordinate(object):
  """A coordinate pair of lat, long."""

  def __init__(self, lat, longitude):
    """Initialize with two angles in degrees."""

    self.lat = lat
    self.long = longitude

  def delta_lat(self, other_coord):
    """Compute the difference in degrees of latitude."""

    delta_rad = other_coord.lat.rad - self.lat.rad

    return AngleRad(delta_rad)

  def delta_long(self, other_coord):
    """Compute the difference in degrees of longitude."""

    delta_rad = other_coord.long.rad - self.long.rad

    return AngleRad(delta_rad)


class GreatCircle(object):
  """Compute a distance using the great circle method."""

  def distance(self, coord1, coord2):
    """Compute the distance using the great circle."""
    sinsin_lat = coord1.lat.sin() * coord2.lat.sin()
    coscos_lat = coord1.lat.cos() * coord2.lat.cos()
    cos_deltalong = coord1.delta_long(coord2).cos()

    angle = AngleDeg().acos(sinsin_lat + coscos_lat * cos_deltalong)

    return angle.dist_from_radius(EARTH_RADIUS)
