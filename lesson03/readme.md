# Turtle Graphics

## Simple polygon and star

[Drawing a polygon](simple.py#L7) is very simple - all you need to do is rotate n-times 360 / n degrees.

[Pentagon](http://xbrukner.github.com/shiny-octo-ninja/lesson03/polygon_5.svg) [Hexagon](http://xbrukner.github.com/shiny-octo-ninja/lesson03/polygon_8.svg)

It is also possible to draw a star with [similar code](simple.py#16), which differs from polygon in a fact that not adjecent vertices are connected, but connecting k-th nearest vertex.

[Star with 5 vertices, connecting every other vertex](http://xbrukner.github.com/shiny-octo-ninja/lesson03/star_5_3.svg)
[Star with 8 vertices, connecting every other vertex](http://xbrukner.github.com/shiny-octo-ninja/lesson03/star_8_3.svg)

## A few simple shapes

Is it easier to draw various shapes using turtle graphics or via absolutely positioned lines?

### Pentagon with vertices connected to each other
[absolute](http://xbrukner.github.com/shiny-octo-ninja/lesson03/pentagon_absolute.svg) [relative](http://xbrukner.github.com/shiny-octo-ninja/lesson03/pentagon_relative.svg)

There is a pretty short piece of code for both [absolute](absolute_relative.py#37) and [relative](absolute_relative.py#8) generation, alhough it was a bit hard for me get the angles right in relative version. But once done, it is eaiser than absolute generation.

### Square spiral
[relative](http://xbrukner.github.com/shiny-octo-ninja/lesson03/spiral_relative.svg)

I decied to go with [turtle graphics](absolute_relative.py#56), since the only hard part is to move to a start of new square, rotate and adjust the side length. But absolute version may not be that difficult either - finding the new vertices is about finding a point on a line between two vertices - which does not involve calculating the new side length (which took me the longest time).

### Crossed circle
[absolute](http://xbrukner.github.com/shiny-octo-ninja/lesson03/circle_absolute.svg)

Circle filled with lines is propably easier to generate with absolutely positioned lines, and I [did it the same way](absolute_relative.py#86). It is because otherwise one would have to move the turtle around the circle and calculate the length of every chord.

### Triangle inception
[relative](http://xbrukner.github.com/shiny-octo-ninja/lesson03/triangle_relative.svg)

Triangle inception comes very easy with [turtle graphics](absolute_relative.py#106) - the only hard thing is knowing when to stop and how to find a start of new triangle.

### Flower
[relative - 10 sided](http://xbrukner.github.com/shiny-octo-ninja/lesson03/flower_relative_10.svg)
[relative - 12 sided](http://xbrukner.github.com/shiny-octo-ninja/lesson03/flower_relative_12.svg)

This elegant shape is result of multiple n sided polygons drawn from common starting point, but every time rotated by 360 / n degrees. [Piece of cake](absolute_relative.py#123) for turtle graphics, possible nightmare for absolutely positioned lines.

## Fractals

### Bush
This fractal [is done](fractals.py#7) via dividing line into two parts - left and right - and recursively continue, doing the whole process n-times. [Simple example with four nestings](http://xbrukner.github.com/shiny-octo-ninja/lesson03/bush_4.svg) shows how it is done, one with [five](http://xbrukner.github.com/shiny-octo-ninja/lesson03/bush_5.svg) looks a bit like Edward Scissorhands, [hexagonal](http://xbrukner.github.com/shiny-octo-ninja/lesson03/bush_6.svg) a bit like a honeycomb, but [eight](http://xbrukner.github.com/shiny-octo-ninja/lesson03/bush_8.svg) and [nine](http://xbrukner.github.com/shiny-octo-ninja/lesson03/bush_9.svg) nesting steps in recursion show some nice bushes.

(BTW, the one with 16 nesting steps take a few tens of seconds to generate and the result image has more than 12 MB in size.)

## My own creation - moving circle
Let's have a circle moving sideways in a constant speed and a pen going around on the circle. The resulting shape will look like [this](http://xbrukner.github.com/shiny-octo-ninja/lesson03/circle_30.svg). I decided to create this not for a circle, but for [any polygon](circle.py). [Triangle](http://xbrukner.github.com/shiny-octo-ninja/lesson03/circle_3.svg) and [square](http://xbrukner.github.com/shiny-octo-ninja/lesson03/circle_4.svg) look absolutely unimpressive, but [pentagon](http://xbrukner.github.com/shiny-octo-ninja/lesson03/circle_5.svg) and [heptagon](http://xbrukner.github.com/shiny-octo-ninja/lesson03/circle_7.svg) show nicely the process of rotation. Polygons with more edges ([10](http://xbrukner.github.com/shiny-octo-ninja/lesson03/circle_10.svg), [15](http://xbrukner.github.com/shiny-octo-ninja/lesson03/circle_15.svg), [20](http://xbrukner.github.com/shiny-octo-ninja/lesson03/circle_20.svg)) converge nicely to a circle moving sideways. (BTW, the [original image](http://xbrukner.github.com/shiny-octo-ninja/lesson03/circle_30.svg) is not a circle, but polygon with thirty sides. ;-) )
