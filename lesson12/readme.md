# Maze generation

For my maze generation I decided to create a classical perfect maze, but on hexagonal grid. For this, three things are needed:

 * Rendering
 * Neighbouring cells
 * Depth-first search

## Rendering
For rendering I chose SVG, since it allows me to easily draw lines. [Code for this](generate.py#L11) is not very nice, but it works for this occasion. It could be easily replaced with code for generation of any regular polygon, but unfortunately there would be a problem in other methods with this.

There one more method, [putDots](generate.py#L77) which just puts blue dots into the top left and bottom right corner, as to make the start and finish of the maze clear.

## Neighbouring cells
When generating maze, we need to know which cells are neighbouring for any other - for example when removing a wall, we need to remove it from current cell and the neighbouring cell. Also, for DFS, we need to know where to go next.

This turned out to be a bit difficult for hexagonal grid. If the grid should change, this method would probably have to be adjusted manually. I used two dimensional array for representation of all cells and I believe the problem cannot be overcome even if only one dimensional array is used. For example when going to right or left, in two-dimensional grid only one parameter needs to be changed, but here also [the other one](generate.py#L45) has to be changed. This is the main reason I did not try to make the generation general for any polygon, because this method would be difficult to implement.

## Depth-first search
Opposite to programming complexity of previous methods, [DFS](generate.py#L66) turned out to be easy and quite general for any maze. Two things are fixed for this implementation - the number of neighbours (on line 68) and two dimensional position of cell in the array (parameters x and y). Otherwise, the implementation should work with any grid.

# Results
I created [two](http://xbrukner.github.com/shiny-octo-ninja/lesson12/perfect7.svg) [small](http://xbrukner.github.com/shiny-octo-ninja/lesson12/perfect8.svg) mazes, which differ in parity of size. Also one [large](http://xbrukner.github.com/shiny-octo-ninja/lesson12/large.svg) maze is generated.