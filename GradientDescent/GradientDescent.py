import sympy as sp
import numpy as np
import sys

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

def gradiant(function, argsf):
    Lf = []
    for var in argsf:
        Lf.append(function.diff(var))
    return sp.Matrix(Lf)


def hessian(function, argsf):
    H = []
    for i in argsf:
        line = []
        for j in argsf:
            line.append(function.diff(j).diff(i))
        H.append(line)
    return sp.Matrix(H)


def normalize(vector):
    vector = sp.Matrix(vector)
    norm = 0
    for x in vector:
        norm += x**2
    return sp.sqrt(norm)


def f(x, y):
    return 4*(x**2)+6*(y**2)+(6*x*y)+(3*x)+(4*y)+6


def h(x, y):
    return (1/2)*(x**2) + 7/2*y**2

fig = plt.figure()
fig.set_size_inches(9, 7, forward=True)
ax = Axes3D(fig, azim=-29, elev=49)
a = np.arange(-7, 8, 0.1)
b = np.arange(-7, 8, 0.1)
A, B = np.meshgrid(a, b)
C = h(A, B)
ax.plot_wireframe(A, B, C, rstride=1, cstride=1)
plt.xlabel("parameter 1 : x")
plt.ylabel("parameter 2 : y")



def fixedDepht(function, coord, s, init_point, e=10**(-5), iter=100):
    Lf = gradiant(function, coord)  # calcul gradiant of the function
    X = sp.Matrix(init_point)  # convert init_point in matrix n*m

    k = 0
    while (k < iter):
        X_K = []  # X[k]
        for i in range(len(coord)):
            # link coord to init value to substitude in Gradiant matrix
            X_K.append((coord[i], X[i]))

        grad = []  # Lf(X[k])
        for expr in Lf:
            grad.append(expr.subs(X_K))  # substitude values in gradiant matrix
        grad = sp.Matrix(grad)  # convert the result in matrix

        if ((normalize(grad)) < e):  # break if ||lf(X[k])|| < precision
            break

        X = sp.Matrix(X - s*grad)  # calcul the X[k+1] = X[k]-s*Lf(X[k])
        ax.scatter(X[0], X[1], h(X[0], X[1]), marker="o", color="#FF0F00")
        plt.draw()
        plt.pause(0.05)
        k += 1

    return X  # return the last X

def sk(xk,dk,coord,function):
    s = sp.symbols("s") # define our symbol arg
    X = sp.Matrix(xk - s*dk) # calcul Xk+sdk to get our Xk+1
    #print(function)
    #print(X)
    X_K = [] #X[k]
    for i in range(len(coord)):
        X_K.append((coord[i], X[i]))
    #print(X_K)
    phi = function.subs(X_K)
    #print(phi)
    #phi = sp.simplify(phi)
    #print(phi)
    grad = gradiant(phi,('s'))
    #print(grad)
    solution = []
    for expr in grad:
        solution.append(sp.solve(sp.Eq(expr,0)))
    #print(type(solution[0][0]))
    return sp.N(solution[0][0])


def print_details(s,k,function, norm, X, coord):
    X_K = [] #X[k]
    info = ""
    for i in range(len(coord)):
        info+= str(coord[i])+":  "+str(X[i]) +" "
        X_K.append((coord[i], X[i]))
    print("""k: {}   f(xk, yk): {}  ||∇f(xk,yk)||: {} sk: {}  {}   """.format(k, function.subs(X_K), norm, s,info))


def optimalDepht(function, coord, init_point, e = 10**(-5), iter=100 ):
    Lf = gradiant(function,coord) #calcul gradiant of the function
    X = sp.Matrix(init_point) #convert init_point in matrix n*m 
    
    k = 0
    while (k < iter):
        X_K = [] #X[k]
        for i in range(len(coord)):
            X_K.append((coord[i], X[i])) #link coord to init value to substitude in Gradiant matrix
        
        grad = [] #Lf(X[k])
        for expr in Lf:
            grad.append(expr.subs(X_K)) #substitude values in gradiant matrix
        grad = sp.Matrix(grad) # convert the result in matrix
        
        if ((normalize(grad)) < e): #break if ||lf(X[k])|| < precision
            break
            
        # determine sk
        s = sk(X,grad,coord,function)
        #print("OKK")
        #break
        X = sp.Matrix(X - s*grad) #calcul the X[k+1] = X[k]-s*Lf(X[k])
        ax.scatter(X[0],X[1],h(X[0],X[1]), marker="o", color="magenta")
        plt.draw()
        plt.pause(0.05)
        print_details(s,k,function, normalize(grad), X, coord)
        k += 1
        
    return X #return the last X


def newtonDirection(function, coord):
    Hf = hessian(function, coord)  # calcul the hessian
    Lf = gradiant(function, coord)  # calcul the gradiant

    V = []  # variables for the linear system Hf*U = -Lf
    for i in range(len(coord)):
        V.append(sp.symbols("v"+str(i)))  # variables création in dimension
    V = sp.Matrix(V)

    solution = sp.solve(Hf*V + Lf, V)  # solve linear system Hf*U = -Lf

    D = []  # newton direction vector
    for v in V:
        D.append(solution[v])  # pass solution of linear system solving
    D = sp.Matrix(D)

    return D  # return Newton Direction



def newtonLocal(function, coord, point, e = 10**(-5)):
    Lf = gradiant(function,coord) #calcul of gradiant
    DNf = newtonDirection(function,coord) #calcul of newton direction
    X = sp.Matrix(point) #init start point convertion into matrix
    

    while (True):# first break condition
        X_K = [] #X[k]
        for i in range(len(coord)):
            X_K.append((coord[i], X[i])) #substitute values coordonate 
        
        grad = [] #Lf(X[k])
        for expr in Lf:
            grad.append(expr.subs(X_K)) #calcul des coordonees de Lf(X[k])
        grad = sp.Matrix(grad)
        
        if ((normalize(grad)) < e): #break if ||lf(X[k])|| < precision
            break
            
        d = [] #DNf(X[k])
        for expr in DNf:
            d.append(expr.subs(X_K)) #calcul des final newton direction value by biding values of X_K
        d = sp.Matrix(d)

        X = sp.Matrix(X + d) #calcul of X[k+1] = Xk+Dk with fixed depth equals to 1.
        ax.scatter(X[0],X[1],h(X[0],X[1]), marker="o", color="#00FF00")
        plt.draw()
        plt.pause(0.05)
        
    return X #retour du dernier X[k]



x, y = sp.symbols('x, y')
#fixedDepht(h(x,y),(x,y),0.1,[7,1.5],10**(-15))
optimalDepht(h(x, y), (x, y), [7, 1.5], 10**(-15))
#newtonLocal(h(x,y),(x,y),[7,1.5],10**(-15))
input()
