#!/usr/bin/env python2.7
# Copyright (C) 2013 by Ken Guyton.  All Rights Reserved.

"""Test the angle module."""

__author__ = 'Ken Guyton'

import math
import unittest
from kmg.angle import Angle
from kmg.angle import AngleRad
from kmg.angle import AngleDeg


class TestAngle(unittest.TestCase):
  def test_create(self):
    angle1 = Angle()
    self.assertEqual(angle1.deg, 0.0)
    self.assertEqual(angle1.rad, 0.0)

  def test_distfromradius(self):
    """For a radius convert the angle to a distance."""

    test_angle = AngleDeg(10.0)
    dist = test_angle.dist_from_radius(100.0)
    self.assertAlmostEqual(dist, 17.4532, delta=4)

  def test_sin(self):
    self.assertAlmostEqual(AngleDeg(30.0).sin(), 0.5, delta=4)
    self.assertAlmostEqual(AngleDeg(90.0).sin(), 1.0, delta=4)
    self.assertAlmostEqual(AngleDeg(180.0).sin(), 0.0, delta=4)

  def test_cos(self):
    self.assertAlmostEqual(AngleDeg(60.0).cos(), 0.5, delta=4)
    self.assertAlmostEqual(AngleDeg(0.0).cos(), 1.0, delta=4)
    self.assertAlmostEqual(AngleDeg(90.0).cos(), 0.0, delta=4)

  def test_acos(self):
    self.assertAlmostEqual(Angle().acos(1.0).deg, 0.0, delta=4)
    self.assertAlmostEqual(Angle().acos(0.5).deg, 60.0, delta=4)
    self.assertAlmostEqual(Angle().acos(0.0).deg, 90.0, delta=4)
    self.assertAlmostEqual(Angle().acos(-0.8660).deg, 150.0, delta=4)

  def test_equal(self):
    self.assertEqual(AngleDeg(30.0), AngleDeg(30.0))
    self.assertEqual(AngleDeg(90.0), AngleDeg(90.0))
    self.assertEqual(AngleDeg(198.0), AngleDeg(198.0))


class TestAngleRad(unittest.TestCase):
  def test_create(self):
    angle1 = AngleRad()
    self.assertEqual(angle1.deg, 0.0)
    self.assertEqual(angle1.rad, 0.0)

  def test_radtodeg(self):
    self.assertAlmostEqual(AngleRad(math.pi).deg, 180.0)
    self.assertAlmostEqual(AngleRad(5 * math.pi / 2).deg, 90.0)


class TestAngleDeg(unittest.TestCase):
  def test_create(self):
    angle1 = AngleDeg()
    self.assertEqual(angle1.deg, 0.0)
    self.assertEqual(angle1.rad, 0.0)

  def test_degtorad(self):
    self.assertAlmostEqual(AngleDeg(180.0).rad, math.pi)
    self.assertAlmostEqual(AngleDeg(450.0).rad, (math.pi / 2))


if __name__ == '__main__':
  unittest.main()
