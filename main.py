import algo
import data

grid = data.generate_grid(20)
print("grid generated")
path, searched, path_length = algo.Astar_path([0, 0, 0], [19, 19, 19], grid, 'm', False)
print("path calculation done")
data.plot_space_path(grid, path, searched, path_length, len(searched))
