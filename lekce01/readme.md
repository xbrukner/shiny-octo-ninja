# Lesson 1

## Collatz conjecture

[Collatz conjecture](collatz.py) is a interesting unsolved (and undecidable) problem in mathematics. We tried to generate a graph which show two things - maximum number reached when generating Collatz sequence and number of steps in the sequence. [Maximum](collatz maximum 0 1000.svg) may be really high even for small numbers (graph shows maximums for every natural number smaller than 1000), but [height](collatz height 0 10000.svg) seems to create interesting graphs even for larger numbers (here for every number smaller than 10000).

## Gradient generation

[Color gradient](color gradient.py) produces blue/red color gradient - black color is in left top corner, red in right top corner, blue in left bottom corner and pink in right bottom corner. It also supports scaling, although it always produces a square (it cannot produce rectangle).

[Example - 500 pixels](gradient.png)

## Star from lines

[Star from lines](lines.py) produces SVG file of a star generated only from lines. Every line comes from point on one axis (x or y) to point on the other axis. These axis divide the whole image into four quadrants with same dimensions. Also, sum of distances from the center of the star to starting and ending point of every line is kept the same.

[Small image](lines-normal.svg) shows the structure of the star, [dense example](lines-dense.svg) shows a star with lots of lines. [Int rounding](lines-dense-int.svg) shows what happens, if division for size is done correctly.


