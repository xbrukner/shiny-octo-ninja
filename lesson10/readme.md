# Linear regression and k-means clustering

Two independent programs are implemented - one for [linear regression](linear regression.py) and one for [k-means clustering](clustering.py).

## Linear regression

[Program](linear regression.py) calculates linear regression via analytic solution, which gives a correct solution for any set of points. The program after calculation prints the a and b for line (ax + b). 

The [input data set](linreg.txt) was provided, and the solution (with a = 0.0479948579494, b = 1.44551940122) can be seen [here](http://xbrukner.github.com/shiny-octo-ninja/lesson10/linreg.svg).

## K-means clustering

For me, the clustering is more interesting. It works in two phases - [**assignement phase**](clustering.py#L16), when for every point closest center is assigned, and [**update phase**](clustering.py#L26), when for every set of points with common center the center is moved to the centroid of given points. This is repeated until a fixed point is reached.

For the initial state, there are two possibilities - assign random centers and start with assignement phase, or create random assignement and start with update phase. [Wikipedia](https://en.wikipedia.org/wiki/K-means_clustering#Initialization_methods) summarizes the methods. I chose the second approach. This also means that the result is non-deterministic and it depends on initial state, so multiple different results may be reached for same data.

The program tries at most hundred iterations before giving up on fixed point calculation and then prints out number of iterations needed. Surprisingly, usually the number is lower than ten on given data. 

### Results
I worked with two sets of data - [Old Faithful](faithful.txt) and [cluster data](cluster_data.txt). The [solution for Old Faithful](http://xbrukner.github.com/shiny-octo-ninja/lesson10/faithful.svg) is not in my opinion very interesting. (The two centers are showed as rectangles).

For cluster data, the results are far more interesting. Usually [this solution](http://xbrukner.github.com/shiny-octo-ninja/lesson10/cluster_data.svg) or with [different colors](http://xbrukner.github.com/shiny-octo-ninja/lesson10/cluster_data2.svg) is reached. Sometimes, [completely different](http://xbrukner.github.com/shiny-octo-ninja/lesson10/cluster_different.svg) solution is reached - as I said in previous paragraph, the solution is non-deterministic. This solution is, however, far less likely than the first solution. One other solution is possible, which results [only in four colors](http://xbrukner.github.com/shiny-octo-ninja/lesson10/cluster_four.svg) - that happens when center is moved far from points and no points are then assigned to it.

I did the experiments manually, so I do not know what are the probabilities for every scenario. However, if indeed the most probable solution is the preferable one, I can think of way to make the generation automatic - generate multiple solution and choose the one where the number of points assigned to every cluster is the most similar to the others.