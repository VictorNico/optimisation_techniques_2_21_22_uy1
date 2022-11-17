import math
import matplotlib.pyplot as plt
import numpy as np

def fonction(x,y):
    return (0.5 * (x**2)) + (3.5 * (y**2))

def derivee_x(x):
    return x

def derivee_y(y):
    return 7*y

def gradientTD (x, y):
    return ( ((-1)*(x**2)) - (49*(y**2)) )

def Armijo (x,y, e1):
    s = float(input("Entrer le nombre de pas : "))
    delta = math.sqrt(159.25)
    k = 0
    s1 = 0
    s2 = 2**90
    while delta > e1:
        if (( e1 > 0) and (e1 < 1/2 )):
            if (fonction((x + s*(-1)*derivee_x(x)), (y + s*(-1)*derivee_y(y)))) <= ( fonction(x, y) + e1*s*gradientTD(x, y) ):
                x = x - (s * derivee_x(x))
                y = y - (s * derivee_y(y))
                print("iteration", k, "fonction cout: \t\t abscisse ", x, "\t\t ordonnee", y, " avec s = ", s)
                break
            else:
                print("iteration ", k, " le pas ", s, " ne verifie pas la condition d Armijo ")
                s2 = s
                s = (s1 + s2)/2
                k = k + 1
        delta = math.sqrt(x ** 2 + 49 * (y ** 2))
    return s

