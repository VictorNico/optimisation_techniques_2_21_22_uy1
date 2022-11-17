import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np



def fonction(x,y):
    return (0.5 * (x**2)) + (3.5 * (y**2))

def derivee_x(x):
    return x

def derivee_y(y):
    return 7*y

def PasFixe(x, y, e):
    s = float(input("Entrer le nombre de pas : "))
    delta = math.sqrt(159.25)
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
    k = 0
    while delta > e:
        #plt.plot(x, y, fonction(x, y), marker='o', color='r')
        x = x - (s * derivee_x(x))
        y = y - (s * derivee_y(y))
        print("iteration", k, "fonction cout: \t\t abscisse ", x, "\t\t ordonnee", y)
        delta = math.sqrt(x ** 2 + 49 * (y ** 2))

        ax.scatter(x, y, fonction(x, y), marker="o", color="#FF0F00")
        plt.draw()
        plt.pause(0.05)
        k = k + 1
