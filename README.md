**3D Path-Finding Visualizer**

In this Project, I utilize an A* algorithm given a 3D grid to find the **optimal** path from a given start to finish. You can use different heuristics (manhattan, Euclidean) as well as varying ranges of motion (rigid, diagonal). The final path, grid space, and obstacles are plotted using MatplotLib on 3D axes. The black dots signify obstacles and the path is marked in red. Some examples are below:

<img src="/images/e_d_walls.png" width="400"/>
<img src="/images/e_nd_walls.png" width="400"/>
<img src="/images/m_d_walls.png" width="400"/>
<img src="/images/m_nd_walls.png" width="400"/>

In the images above, the obstacles are two walls that the algorithm must get around. Because we are utilizing the pathfinder on a physical space, we always find a sorter path if we allow diagonals (in a triangle we know that the hypotenuse is always smaller than the sum of its legs). However, it's interesting to see that the shortest path was with utilizing an euclidian distance heuristic and allowing diagonals. 

Below are some more examples with cool obstacles!!

<img src="/images/e_nd_sphere.png" width="400"/>
<img src="/images/m_md_wall_holes.png" width="400"/>
<img src="/images/e_d_wall_holes.png" width="400"/>
