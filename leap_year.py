def leap_year():
    text=input("Ingrese un año: ")
    year=int(text)
    resto=year%4
    cent=year%100
    cuat=year%400
    
    def first():
        if resto==0:
            second()
        else:
            print(f"El año {year} no es bisiesto")
    
    def second():
        if cent==0 and cuat!=0:
            print(f"El año {year} no es bisiesto")
        elif cent==0 and cuat==0:
            print(f"El año {year} es bisiesto")
        else:
            print(f"El año {year} es bisiesto")
    first()
