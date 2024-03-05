import heapq


def euclidean_distance(start, end):
    x1, y1, z1 = start
    x2, y2, z2 = end
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5


def manhattan_distance(start, end):
    x1, y1, z1 = start
    x2, y2, z2 = end
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)


def in_bound(grid, n):
    x, y, z = n
    l = len(grid)
    return 0 <= x < l and 0 <= y < l and 0 <= z < l


def Astar_path(start, end, grid, code, allow_diagonals):
    start = tuple(start)
    end = tuple(end)
    first_node = [0, 0, 0, start, None]
    searchable = []
    searched = {0}
    searched.remove(0)
    heapq.heappush(searchable, first_node)
    loc_to_node = {start: first_node}
    while searchable:
        curr_node = heapq.heappop(searchable)
        total_cost, distance_cost, length_cost, cell, prev_node = curr_node
        loc_to_node.pop(cell)
        if cell == end:
            path = []
            path_length = 0.0
            while prev_node is not None:
                path.insert(0, cell)
                next_cell = prev_node[3]
                path_length += euclidean_distance(cell, next_cell)
                cell = next_cell
                prev_node = prev_node[4]
            path.insert(0, [0, 0, 0])
            return path, list(searched), int(path_length * 1000) / 1000
        else:
            searched.add(cell)
            x, y, z = cell
            if allow_diagonals:
                neighbors = (
                    (x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x + 1, y + 1, z), (x - 1, y - 1, z),
                    (x + 1, y - 1, z), (x - 1, y + 1, z),
                    (x, y, z + 1), (x + 1, y, z + 1), (x - 1, y, z + 1), (x, y + 1, z + 1), (x, y - 1, z + 1),
                    (x + 1, y + 1, z + 1), (x - 1, y - 1, z + 1), (x + 1, y - 1, z + 1), (x - 1, y + 1, z + 1),
                    (x, y, z - 1), (x + 1, y, z - 1), (x - 1, y, z - 1), (x, y + 1, z - 1), (x, y - 1, z - 1),
                    (x + 1, y + 1, z - 1), (x - 1, y - 1, z - 1), (x + 1, y - 1, z - 1), (x - 1, y + 1, z - 1))
            else:
                neighbors = ((x + 1, y, z), (x - 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z + 1), (x, y, z - 1))
            for n in neighbors:
                nx, ny, nz = n
                if in_bound(grid, n) and grid[nx][ny][nz] != 1 and n not in searched:
                    if code == 'm':
                        new_distance_cost = manhattan_distance(n, end)
                    elif code == 'e':
                        new_distance_cost = euclidean_distance(n, end)
                    else:
                        raise ValueError("invalid distance metric")
                    new_length_cost = length_cost + euclidean_distance(cell, n)
                    new_total_cost = new_length_cost + new_distance_cost
                    if n in loc_to_node:
                        if new_total_cost < loc_to_node[n][0]:
                            loc_to_node[n][0] = new_total_cost
                            loc_to_node[n][1] = new_distance_cost
                            loc_to_node[n][2] = new_length_cost
                            loc_to_node[n][4] = curr_node
                            heapq.heapify(searchable)
                    else:
                        new_node = [new_total_cost, new_distance_cost, new_length_cost, n, curr_node]
                        loc_to_node[n] = new_node
                        heapq.heappush(searchable, new_node)
    return [[0, 0, 0]], list(searched), 0.0
