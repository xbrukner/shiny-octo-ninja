# Maze solution

I chose a maze where you need to go through some of the walls in order to solve the maze. The task is to minimize number of walls blown and secondly by number of steps. This is nice ordering criteria, which makes it ideal for dynamic programming.

[The code](dynamite.py#L24) itself is more similar to DFS than to dynamic programming. The explanation is simple - because every cell will be visited just once, but the order of cells visited depends on the maze's structure. Since two criteria has to be met, the algorithm works by alternating them - it first explores all the cells available without any wall blasting, and when no other cell is reacheable, it tries to go through the walls. This is not enough for the ordering to work though, because some cell might be reachable through two different walls, the length of the way has to be taken into account.

## Results
I created two input files ([A](maze1), [B](maze2)), the second one is taken from the slides. The solution visualises the maze and shows the path with blue line ([A](http://xbrukner.github.com/shiny-octo-ninja/lesson11/maze1.svg), [B](http://xbrukner.github.com/shiny-octo-ninja/lesson11/maze2.svg)).
