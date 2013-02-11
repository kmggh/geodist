#!/usr/bin/env python2.7
# Copyright (C) 2013 by Ken Guyton.  All Rights Reserved.

"""Illustrate the basic usage of the geodist library."""

__author__ = 'Ken Guyton'

from kmg import geodist
from kmg.angle import AngleDeg

LAT1 = AngleDeg(37.61940)
LONG1 = AngleDeg(-122.37392)

LAT2 = AngleDeg(37.77677)
LONG2 = AngleDeg(-122.41673)


def main():
  coord1 = geodist.Coordinate(LAT1, LONG1)
  coord2 = geodist.Coordinate(LAT2, LONG2)

  dist_obj = geodist.GeoDist()
  distance = dist_obj.distance(coord1, coord2)

  print '%.2f miles' % distance


if __name__ == '__main__':
  main()
