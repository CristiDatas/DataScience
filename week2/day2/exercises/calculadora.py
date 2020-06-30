
def menu_calculadora():
    print("\n\n --- CALCULADORA ---\n\n")
    print("Éstas son las operaciones que puedes realizar:\n\n")
    print("+\t>>>\tSUMA")
    print("-\t>>>\tRESTA")
    print("*\t>>>\tMULTIPLICACIÓN")
    print("/\t>>>\tDIVISIÓN")
    print("//\t>>>\tDIVISIÓN ENTERA")
    print("**\t>>>\tPOTENCIA")
    print("%\t>>>\tRESTO\n\n")
    
    num1=(input("Dime un número: "))
    if num1.isnumeric():
        num1=float(num1)
    else:
        print("\n\nESO NO ERA UN NÚMERO. PRUEBA OTRA VEZ.\n\n")
        menu_calculadora()

    num2=(input("\nDime otro número: "))
    if num2.isnumeric():
        num2=float(num2)
    else:
        print("\n\nESO NO ERA UN NÚMERO. PRUEBA OTRA VEZ.\n\n")
        menu_calculadora()

    operadores=("+","-","*","/","//","**","%")

    operador=(input("\nIntroduce el primer operador (+ - * / // ** %): "))
    
    resultado=()

    if operador not in operadores:
        print("\n\nDebes introducir un operador válido (+ - * / // ** %). PRUEBA OTRA VEZ.")
        menu_calculadora()

    else:
        if operador=="+":
            resultado=num1+num2
        elif operador=="-":
            resultado=num1-num2
        elif operador=="*":
            resultado=num1*num2
        elif operador=="/":
            resultado=num1/num2
        elif operador=="//":
            resultado=num1//num2
        elif operador=="**":
            resultado=num1**num2
        elif operador=="%":
            resultado=num1%num2
        
    print("\n\nEl resultado de", num1,operador,num2,"es: ",resultado,".\n")
    
    operador2=(input("\nAhora introduce otro operador (+ - * / // ** %): "))

    if operador2 not in operadores:
        print("\n\nDebes introducir un operador válido (+ - * / // ** %). PRUEBA OTRA VEZ.")
        menu_calculadora()
    else:
        if operador2=="+":
            resultado2=num1+num2
        elif operador2=="-":
            resultado2=num1-num2
        elif operador2=="*":
            resultado2=num1*num2
        elif operador=="/":
            resultado2=num1/num2
        elif operador2=="//":
            resultado2=num1//num2
        elif operador2=="**":
            resultado2=num1**num2
        elif operador2=="%":
            resultado2=num1%num2

    print("\n\nEl resultado de", num1,operador2,num2,"es: ",resultado2,".\n")

    rep=input("\nSi quieres repetir la experiencia escribe OK: ").upper()
    if rep=="OK":
        menu_calculadora()
    else:
        print("Hastaluegomaricarmen")
        

menu_calculadora()