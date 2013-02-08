#!/usr/bin/env python2.7
# Copyright (C) 2013 by Ken Guyton.  All Rights Reserved.

"""Compute the distance from SFO to Twitter.

This is a test and example file for using geodist.
"""

__author__ = 'Ken Guyton'

from kmg import geodist

SFO_LAT = 37.61940
SFO_LONG = -122.37392

TW_LAT = 37.77677
TW_LONG = -122.41673

# Distance measured with measurement tool on Google Maps.
GMAP_DIST = 11.1148


def report_error(orig_dist, a_dist):
  """Report the error given an actual dist."""

  error = orig_dist - a_dist
  error_ft = error * 5280.0
  percent_err = error / orig_dist * 100.0

  print 'Computed distance SFO to Twitter: %.4f miles.' % a_dist
  print 'Original dist: %.4f miles.' % orig_dist
  print 'Error: %.4f miles = %.1f feet.' % (error, error_ft)
  print 'Percentage error: %.3f %%.' % percent_err


def main():
  sfo = geodist.Coordinate(SFO_LAT, SFO_LONG)
  tw = geodist.Coordinate(TW_LAT, TW_LONG)

  geodist_obj = geodist.GeoDist()
  dist = geodist_obj.distance(sfo, tw)
  print '\nUsing the flat-earth approximation.\n'
  report_error(GMAP_DIST, dist)

  gcdist_obj = geodist.GreatCircle()
  gc_dist = gcdist_obj.distance(sfo, tw)
  print '\nUsing the great circle computation.\n'
  report_error(GMAP_DIST, gc_dist)

  print '\nCompare great circle to flat..\n'
  report_error(gc_dist, dist)

  print


if __name__ == '__main__':
  main()
