# Analytic geometry

## Finding line segments intersections

This [basic algorithm](geometry.py#L74) tries to find all intersections of line segments. To do this, it uses determinant for finding [line-line intersection](https://en.wikipedia.org/wiki/Line-line_intersection) and then checks whether the intersection is on these two line segments. For this check, weaker condition is checked: if the found point is inside a polygon given by ending points of the line segments - because if it is, it has to be on this two lines (which is calculated in previous step). Complexity of this algorithm is O(n^2).

To make the generation slightly more interesting, all the lines have the same length. This is done via generation of starter point, length and angle and then checking whether the line fits into the image.

[Generated image](http://xbrukner.github.com/shiny-octo-ninja/lesson05/intersection.svg)

## Triangulation

There is a simple algorithm for drawing a triangulation of generated points - take a line segment from one point to another, see if it intersects any other already chosen line segment, and it it does not, add it to the chosen line segments. This naive algorithm produces triangulation, although its complexity is possibly O(n^4).

I implemented two triangulation algorithms, which differ in a way new line segment is chosen. [First algorithm](geometry.py#L96) chooses all the lines that start in one point, then from another etc., which in the result shows [large center](http://xbrukner.github.com/shiny-octo-ninja/lesson05/triangulation.svg) from which large number of line segments start. [Second algorithm](geometry.py#L115) on the other hand sorts all the line segments by length. If the shortest lines are chosen first, [the result](http://xbrukner.github.com/shiny-octo-ninja/lesson05/triangulation_sorted.svg) shows pretty nicely distributed line segments. If the longest lines are chosen first, [some nasty long lines](http://xbrukner.github.com/shiny-octo-ninja/lesson05/triangulation_sorted.svg) are visible and the result is a bit similar to the first algorithm.

## Convex hull

This algorithm was the most difficult for me, because it took me a long time to implement it correctly. The idea is simple - choose a starting point, then choose the point which is leftmost (or rightmost), make the line from starting point to next point and repeat until you finish in the starting point. This algorithm is called [gift wrapping](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm), whith complexity O(nh), with n being the number of points and h being the number of points on the hull.

[My implementation](geometry.py#L149) uses arctangents to calculate the angle of every point, then smallest is chosen. This actually took me a long time to get it right, but in the end it works (and I had to divided the algorithm into two parts - first goes from left to right and the second from right to left). And [the result](http://xbrukner.github.com/shiny-octo-ninja/lesson05/convex_hull.svg) shows it works.
