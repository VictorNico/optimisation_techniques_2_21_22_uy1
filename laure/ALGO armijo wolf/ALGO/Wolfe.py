import math
import matplotlib.pyplot as plt
import numpy as np
from Armijo import *

def fonction(x,y):
    return (0.5 * (x**2)) + (3.5 * (y**2))

def derivee_x(x):
    return x

def derivee_y(y):
    return 7*y

def gradientTD (x, y):
    return ( ((-1)*(x**2)) - (49*(y**2)) )

def Wolfe (x, y, e1, e2):
    s = Armijo(x, y, e1)
    delta = math.sqrt(159.25)
    s1 = 0
    while delta > e1:
                if (e2 > e1) and (e2 < 1):
                    if (((-1) * x * (x + s*(-1*x))) + ((-7*y) * (7 * (y + s*(-7*y))))) >= (e2 * gradientTD(x, y)):
                        x = x - (s * derivee_x(x))
                        y = y - (s * derivee_y(y))
                        print(" le pas = ", s)
                        break
                    else:
                        s1 = s
                        s = s1 / 2
                delta = math.sqrt(x ** 2 + 49 * (y ** 2))

