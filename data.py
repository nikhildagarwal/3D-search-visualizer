import matplotlib.pyplot as plt
import random


def generate_grid(size):
    x = list(range(size))
    y = []
    z = []
    for i in range(size):
        row = [i] * size
        y += row
        if i != 0:
            x += x[0:size]
    l = len(x)
    for i in range(size):
        row = [i] * (size * size)
        z += row
        if i != 0:
            y += y[0:l]
            x += x[0:l]
    grid = [[[0 for _ in range(size)] for _ in range(size)] for _ in range(size)]
    for x1, y1, z1 in zip(x, y, z):
        flag1 = random.randint(0, 1)
        flag2 = random.randint(0, 1)
        if -30 <= (((x1 - 10)**2 + (y1 - 10)**2 + (z1 - 10)**2)-36) <= 0:
            grid[x1][y1][z1] = 1
        else:
            grid[x1][y1][z1] = 0
    return grid


def plot_space_path(grid, path, searched, length, amount):
    ux = []
    uy = []
    uz = []
    bx = []
    by = []
    bz = []
    l = len(grid)
    for i in range(l):
        for j in range(l):
            for k in range(l):
                if grid[i][j][k] == 1:
                    bx.append(i)
                    by.append(j)
                    bz.append(k)
                else:
                    ux.append(i)
                    uy.append(j)
                    uz.append(k)
    px = []
    py = []
    pz = []
    for x, y, z in path:
        px.append(x)
        py.append(y)
        pz.append(z)
    sx = []
    sy = []
    sz = []
    if searched is not None:
        for x, y, z in searched:
            sx.append(x)
            sy.append(y)
            sz.append(z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if searched is not None:
        ax.scatter(sx, sy, sz, color='g', s=0.01, label="searched points: " + str(amount))
    ax.scatter(bx, by, bz, color='black', s=5)
    ax.plot(px, py, pz, label='path: ' + str(length), color='r', markersize='10')
    ax.legend()
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('Optimal Path in a 3D space')
    plt.show()
