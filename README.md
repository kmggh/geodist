Geo Distance
============

This is code to measure the distance between two coordinates.

With one approach, it assumes a plane approximation of the earth's
surface so this is only for distances small enough for that assumption
to give useful answers.

It also assumes a spherical model of the earth with a radius of
6371 km.

The second approach makes a great circle calculation using the same
spherical model.

The tests in test_geodist.py and an example program, dist_sf.py illustrate how to use the code.


To run
======

    ./test_geodist.py
    ./dist_sf.py

    

Author
======

Ken Guyton



