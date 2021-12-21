def verificador(y):
    class error(Exception):
        pass
    class Cero(error):
        pass
    class menorcero(error):
        pass
    cond = True
    while(cond):
        try:
            x = int(input(y))
            if (x == 0):
                raise Cero
            elif(x < 0):
                raise menorcero
            else:
                return x
                cond = False
                
        except (ValueError):
           print("Ingresó algo distinto a un numero")
        except (Cero):
            print("Ingresó cero")
        except (menorcero):
            print("El numero es menor a cero")
    
texto1 = ("Ingrese el primer diametro: ")
num1 = verificador(texto1)
texto2 = ("Ingrese el segundo diametro: ")
num2 = verificador(texto2)
if num1 == num2:
    print("Es un cuadrado")
    resultado = (num1*num2/2)
    print("El area del cuadrado es: {0}".format(resultado))
else:
    resultado = (num1*num2/2)
    print("El area del rombo es: {0}".format(resultado))