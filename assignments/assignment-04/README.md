CS 240: Computer Science II
===========================

Assignment 04
-------------

### Description
Refactor the Olympic Flag Program

Divide your program into functional section that emphasize the fact that this style of program has three main phases. The phases should focus on initialization, standard behavior, and termination. In initialization (define an init() function), be sure to prepare the main window. In the standard behavior section (define a main() function) there should be a main "game loop", and whatever is required to support the loop. For the current program, no termination code is necessary. You should also focus on eliminating unecessary global variables.

In addition to restructuring the main execution, abstract the drawing of the flag to a function (draw_flag() is suggested) that takes a pygame surface (the screen) and draws the flag. This will simplify your main() so that only a call to draw_flag() will be necessary.

How To
------
Define functions:
* init()
* draw_flag()
* main()
