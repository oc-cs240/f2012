CS 240: Computer Science II
===========================

Assignment 05
-------------

### Description
Add a Class to the Olympic Flag Program

Create a separate module (flag.py is suggested) that defines a class to handle the drawing and maintaining of flag objects. The class should have a custom initializer (the __init__() function) that allows objects to be created with some paramters. The init params must include left and top for the location of the flag. Other parameters (eg. width, height) are optional at this time, and may be included as default parameters or skipped. The class should also have a draw() function that is to be called by the session host once for each object, every time through the game loop.

To make your Flag class easy to use and to add functionality, store the location and size parameters in a pygame.Rect object.

How To
------
Define a class:
* Flag
 * Members:
  - rect
 * Methods:
  - __init__()
  - draw()
