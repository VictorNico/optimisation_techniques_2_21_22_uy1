import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def fonction(x,y):
    return (0.5 * (x**2)) + (3.5 * (y**2))

def derivee_x(x):
    return x

def derivee_y(y):
    return 7*y


def PasOptimal(x, y, e):
    fig = plt.figure()
    fig.set_size_inches(9, 7, forward=True)
    ax = Axes3D(fig, azim=-29, elev=49)
    a = np.arange(-5, 5, 0.1)
    b = np.arange(-5, 5, 0.1)
    A, B = np.meshgrid(a, b)
    C = fonction(A, B)
    ax.plot_wireframe(A, B, C, rstride=1, cstride=1)
    plt.xlabel("parameter 1 : x")
    plt.ylabel("parameter 2 : y")
    delta = math.sqrt(159.25)
    k = 0
    while delta > e:
        #pour calculer a chaque iteration la direction d de coordonnee dx et dy
        dx = (-1) * derivee_x(x)
        dy = (-1) * derivee_y(y)
        # pour calculer a chaque iteration le pas s qui est alpha
        s = ((x**2) + (49 * (y**2))) / ((x**2) + (343 * (y**2)))
        x = x + (s * dx)
        y = y + (s * dy)
        print("iteration", k, "fonction cout: \t\t abscisse ", x, "\t\t ordonnee", y)
        delta = math.sqrt(x ** 2 + 49 * (y ** 2))

        ax.scatter(x, y, fonction(x, y), marker="o", color="#FF0F00")
        plt.draw()
        plt.pause(0.05)
        k = k + 1
