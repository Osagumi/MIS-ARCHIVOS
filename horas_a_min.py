def verificador(y):
    class error(Exception):
        pass
    class menorcero(error):
        pass
    cond = True
    while(cond):
        try:
            x = int(input(y))
            if(x < 0):
                raise menorcero
            else:
                return x
                cond = False
                
        except (ValueError):
           print("Ingresó algo distinto a un numero")
        except (menorcero):
            print("El numero es menor a cero")
texto1 = ("Ingrese minutos que convertira a horas: ")
num1 = verificador(texto1)
hora = (num1*60)
if num1 == 1:
    print("{0} hora equivalen a {1} minutos".format(num1,hora))
else:
    print("{0} horas equivalen a {1} minutos".format(num1,hora))