from PasFixe import *
from AlgoNewton import *
from PasOptimal import *
from GaussNewton import *
from Armijo import *
from Wolfe import *

e = 0.00001
while True:
    print("\n")
    print("\t\t\t\t\t\t\t................................ Algorithme de Gradient de Descente ..........................")
    print("\t\t\t\t\t\t\t\t\t\t1. Algorithme a pas fixe ")
    print("\t\t\t\t\t\t\t\t\t\t2. Algorithme a pas optimal ")
    print("\t\t\t\t\t\t\t\t\t\t3. Algorithme Newton Local ")
    print("\t\t\t\t\t\t\t\t\t\t4. Algorithme Gauss de Newton ")
    print("\t\t\t\t\t\t\t\t\t\t5. Algorithme a pas fixe Condition D Armijo ")
    print("\t\t\t\t\t\t\t\t\t\t6. Algorithme a pas fixe Condition De Wolfe ")
    print("\t\t\t\t\t\t\t................................ Algorithme de Gradient de Descente ..........................")
    print("\n")
    x = float(input("Entrer X0 : "))
    y = float(input("Entrer Y0 : "))
    choix = input("Entrer le choix de votre algorithme : ")

    if choix == '1':
        PasFixe(x, y, e)
    elif choix == '2':
        PasOptimal(x, y, e)
    elif choix == '3':
        Newton(x, y, e)
    elif choix == '4':
        GaussNewton(x, y, 0)
    elif choix == '5':
        Armijo(x, y, 0.0001)
    elif choix == '6':
        Wolfe(x, y, e, 0.99)
    else:
        print(" Auncun choix ............. Veuillez faire un choix !!!!!!!!!! ")