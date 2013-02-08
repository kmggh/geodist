#!/usr/bin/env python2.7
# Copyright (C) 2013 by Ken Guyton.  All Rights Reserved.

"""Test the geodist module."""

__author__ = 'Ken Guyton'

import math
import unittest
from kmg import geodist

# In miles.
ONE_DEG_OF_LAT = 69.0933

# In degrees.
TEST_LAT = 33.0

# In miles.
PARALLEL_RADIUS = 3320.0910
ONE_DEG_OF_LONG = 57.9465

LAT1 = 33.77264
LONG1 = -84.39290

LAT2 = 33.94979
LONG2 = -83.37332

# In miles.
# From Google maps 59.8288 mi, delta = 25.87 ft.
DISTANCE = 59.8239


class TestGeoDist(unittest.TestCase):
  def setUp(self):
    self.geodist = geodist.GeoDist()

  def test_create(self):
    self.assertNotEqual(self.geodist, None)

  def test_degtorad(self):
    self.assertAlmostEqual(self.geodist.degtorad(180.0), (math.pi))
    self.assertAlmostEqual(self.geodist.degtorad(0.0), 0.0)
    self.assertAlmostEqual(self.geodist.degtorad(450.0), (math.pi / 2))

  def test_radtodeg(self):
    self.assertAlmostEqual(self.geodist.radtodeg(math.pi), 180.0)
    self.assertAlmostEqual(self.geodist.radtodeg(0.0), 0.0)
    self.assertAlmostEqual(self.geodist.radtodeg((5 * math.pi / 2)), 90.0)

  def test_delta_lat(self):
    self.assertAlmostEqual(self.geodist.delta_lat(1.0), ONE_DEG_OF_LAT,
                           delta=4)

  def test_parallel(self):
    self.assertAlmostEqual(self.geodist.parallel_radius(TEST_LAT),
                           PARALLEL_RADIUS, delta=4)

  def test_delta_long(self):
    self.assertAlmostEqual(self.geodist.delta_long(TEST_LAT, 1.0),
                           ONE_DEG_OF_LONG, delta=4)

  def test_cartesian_dist(self):
    self.assertAlmostEqual(self.geodist.cartesian_dist(3.0, 4.0), 5.0)

  def test_distance(self):
    coord1 = geodist.Coordinate(LAT1, LONG1)
    coord2 = geodist.Coordinate(LAT2, LONG2)

    self.assertAlmostEqual(self.geodist.distance(coord1, coord2), DISTANCE,
                           delta=4)


class TestCoordinate(unittest.TestCase):
  def setUp(self):
    self.coord = geodist.Coordinate(LAT1, LONG1)
    self.coord2 = geodist.Coordinate(LAT2, LONG2)
  def test_coordinate(self):
    self.assertEqual(self.coord.lat, LAT1)
    self.assertEqual(self.coord.long, LONG1)

  def test_delta_lat(self):
    self.assertAlmostEqual(self.coord.delta_lat(self.coord2),
                           (LAT2 - LAT1), delta=4)

  def test_delta_long(self):
    self.assertAlmostEqual(self.coord.delta_long(self.coord2),
                           (LONG2 - LONG1), delta=4)


class TestGreatCircle(unittest.TestCase):
  def setUp(self):
    self.gc_dist = geodist.GreatCircle()

  def test_sin(self):
    self.assertAlmostEqual(self.gc_dist.sin(30.0), 0.5, delta=4)
    self.assertAlmostEqual(self.gc_dist.sin(90.0), 1.0, delta=4)
    self.assertAlmostEqual(self.gc_dist.sin(180.0), 0.0, delta=4)

  def test_cos(self):
    self.assertAlmostEqual(self.gc_dist.cos(60.0), 0.5, delta=4)
    self.assertAlmostEqual(self.gc_dist.cos(0.0), 1.0, delta=4)
    self.assertAlmostEqual(self.gc_dist.cos(90.0), 0.0, delta=4)

  def test_acos(self):
    self.assertAlmostEqual(self.gc_dist.acos(1.0), 0.0, delta=4)
    self.assertAlmostEqual(self.gc_dist.acos(0.5), 60.0, delta=4)
    self.assertAlmostEqual(self.gc_dist.acos(0.0), 90.0, delta=4)
    self.assertAlmostEqual(self.gc_dist.acos(-0.8660), 150.0, delta=4)

  def test_distance(self):
    coord1 = geodist.Coordinate(LAT1, LONG1)
    coord2 = geodist.Coordinate(LAT2, LONG2)

    self.assertAlmostEqual(self.gc_dist.distance(coord1, coord2), DISTANCE,
                           delta=4)


if __name__ == '__main__':
  unittest.main()
