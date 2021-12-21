def verificador(rut):
    class error(Exception):
        pass
    cond = True
    while(cond):
        try:
            temp = [rut.append(numeros) for numeros in (input("Rut aqui: "))]
            lista2 = []
            for i in range(len(rut)):
                if rut[i] != "." and rut[i] != "-":
                    lista2.append(rut[i])
            rut = lista2
            if (len(rut) == 8):
                calculo(rut)
                rut = []
            elif (len(rut) > 9 or len(rut) < 7):
                print("Ingreso un RUT no valido")
                rut = []
            elif (len(rut) == 7):
                rut.reverse()
                rut.append("0")
                rut.reverse()
                calculo(rut)
                rut = []
            else:
                print(rut[8])
                verif_temporal = rut[8]
                print(rut)
                rut.remove(rut[8])
                digito = calculo(rut)
                if str(digito) == str(verif_temporal):
                    print("Dígito verificador ingresado correcto")
                    print(digito)
                    print(verif_temporal)
                    rut = []
                else:
                    print("Dígito veridicador ingresado incorrecto")
                    rut = []    
                
        except (ValueError):
           print("Ingresó algo distinto a un numero")
           rut = []

def calculo(rut):
    rut.reverse()
    recorrido = 2
    multiplicar = 0
    for i in rut:
        multiplicar+=int(i)*recorrido
        if recorrido == 7:
            recorrido = 1
        recorrido+=1
    modulo = multiplicar%11
    resultado = 11-modulo
    if resultado == 11:
        digito = 0
    elif resultado == 10:
        digito = "k"
    else:
        digito = resultado
    print("Dígito verificador: ", digito)
    return digito

rut = []
verificador(rut)