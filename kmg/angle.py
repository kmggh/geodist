# Copyright (C) 2013 by Ken Guyton.  All Rights Reserved.

"""An angle object with built in trig functions."""

__author__ = 'Ken Guyton'

import math


class Angle(object):
  """An angle."""

  def __init__(self, rad=0.0):
    """Create an angle from radians."""

    self.rad = rad

  @property
  def deg(self):
    """Return the angle in deg."""

    return self._radtodeg(self.rad)

  def _normalize_angle(self, angle):
    """Normalize an angle onto the range 0 <= angle < 360."""

    new_angle = angle
    while new_angle >= 360.0:
      new_angle -= 360.0

    return new_angle

  def _degtorad(self, deg):
    """Convert degrees to radians."""

    return self._normalize_angle(deg) * math.pi / 180.0

  def _radtodeg(self, rad):
    """Convert radians to degrees."""

    return self._normalize_angle(rad * 180.0 / math.pi)

  def dist_from_radius(self, radius):
    """Compute a distance along a circle from the radius given."""

    return radius * self.rad

  def sin(self):
    """Return the sine of this angle."""

    return math.sin(self.rad)

  def cos(self):
    """Return the cosine of this angle."""

    return math.cos(self.rad)

  def acos(self, dist):
    """Return a new Angle as the arccosine of the input distance."""

    return Angle(math.acos(dist))

  def __eq__(self, other_angle):
    """Test equal."""

    return self.rad == other_angle.rad


class AngleRad(Angle):
  """An angle initialized in radians."""


class AngleDeg(Angle):
  """An angle initialized in degrees."""

  def __init__(self, deg=0.0):
    """Initialize with degrees."""

    self.rad = self._degtorad(deg)
