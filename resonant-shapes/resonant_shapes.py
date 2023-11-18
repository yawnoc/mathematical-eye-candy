import os

import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, pi

GRID_SIZE = 5
PLOT_STEP = 1/30


def xi_level(x, y, m, n):
    return sin(m * pi * x) * sin(n * pi * y) + sin(n * pi * x) * sin(m * pi * y)


def main():
    grid_indices = range(0, GRID_SIZE)
    x_values = np.arange(0, 1, PLOT_STEP)
    y_values = np.arange(0, 1, PLOT_STEP)

    fig, axs = plt.subplots(GRID_SIZE, GRID_SIZE)

    for m_index in grid_indices:
        for n_index in grid_indices:
            m = 2 * m_index + 1
            n = 2 * n_index + 1

            xx, yy = np.meshgrid(x_values, y_values)
            zz = xi_level(xx, yy, m, n)

            ax = axs[m_index, n_index]
            ax.contour(xx, yy, zz, levels=[0])
            ax.set_aspect('equal')

    plt.setp(axs, xticks=[], yticks=[])
    plt.savefig(os.path.join(os.path.dirname(__file__), 'resonant-shapes.svg'))


if __name__ == '__main__':
    main()