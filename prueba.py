#P1_Control1.py
# Secuencia: 21, 2, 13, 24, 5, 16, 27, 8, 19, 0, ....
def main():
	N = 21
	C = leeCantidad()
	imprimeSecuencia(N,C)
#
def leeCantidad():
        num = int(input("Cuantos números quiere para esta secuencia (minimo 2): "))
        while (num < 2):
                print("Debe repetir el ingreso!!")
                num = int(input("Cuantos números quiere para esta secuencia (minimo 2): "))
        c = num
        return c

def imprimeSecuencia(n,c):
        sec = ""
        cond = 0
        cond2 = 0
        for i in range(c):
                x = (n - 19)
                y = x + 11
                z = y + 11
                sec = sec + " " + str(x) + " " + str(y) + " " + str(z)
                print(sec)
                n = z
        sec = ("21" + sec)
        print(sec)
        for i in sec:
                print("xd")
                print(i)
                cond2 += 1
                if i.isspace():
                        cond += 1
                        if cond == c:
                                sec = sec[:cond2]

                
        print(sec)
main()

