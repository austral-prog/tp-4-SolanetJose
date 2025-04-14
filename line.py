def line():
    import math
    a=float(input("Ingrese el coeficiente A: "))
    b=float(input("Ingrese el coeficiente B: "))
    x1=float(input("Ingrese el coeficiente X1: "))
    x2=float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")
    print("\n"+"Para la siguiente ecuación:"+"\n"+"\t"+f"Y = {a}X + {b}"+"\n")
    y1=a*x1+b
    y2=a*x2+b
    P1=x1,y1
    P2=x2,y2
    print("Dados los siguientes puntos:"+"\n"+"\t"+f"P1 {P1}"+"\n"+"\t"+f"P2 {P2}")
    d=math.dist(P1,P2)
    print("\n"+f"La distancia entre ellos es: {d}")
