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

The tests in test_geodist.py and an example program, **dist_sf.py**
illustrate how to use the code.


Library Usage
=============

See the program **basic_usage.py** for a simple example.  Note that
the **GeoDist** and **GreatCircle** classes have the same interface,
i.e., they are used the same way.


To run
======

    ./test_geodist.py
    ./dist_sf.py


Output from dist_sf.py
======================


    Using the flat-earth approximation.
    
    Computed distance SFO to Twitter: 11.1228 miles.
    Original dist: 11.1148 miles.
    Error: -0.0080 miles = -42.1 feet.
    Percentage error: -0.072 %.
    
    Using the great circle computation.
    
    Computed distance SFO to Twitter: 11.1222 miles.
    Original dist: 11.1148 miles.
    Error: -0.0074 miles = -39.3 feet.
    Percentage error: -0.067 %.
    
    Compare great circle to flat..
    
    Computed distance SFO to Twitter: 11.1228 miles.
    Original dist: 11.1222 miles.
    Error: -0.0005 miles = -2.8 feet.
    Percentage error: -0.005 %.


Observations
------------

Over a distance like this, the great-circle and plane-approximation
approaches are very close, within 0.005%.  Both differ more
significantly from a measurement off of Google Maps using the
measurement tool.

The differences could be due to:

1. Errors in Google Maps or in the lab measurement tool.
2. Variations introduced by topographic features.
3. Differences introduced by the mean earth radius used.


Release Notes
=============

Release 1.0 
-----------

*2013-02-08*

This release puts most of the functionality in the **geodist.py**
module with methods in the classes that take a float as input
representing degrees.


Release 2.0 
-----------

*2013-02-10*

This release adds an **Angle** class that handles degrees and radians
and contains the trig functions as well.  With all of those details
separated the other classes become much simpler.


Author
======

Ken Guyton
2013-02-08


