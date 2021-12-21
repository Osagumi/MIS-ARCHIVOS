#Tuplas01.py
# Escriba un programa que acepte una frase cualquiera (no vacía)
# y la convierta en una tupla de palabras
# Ejemplo: S = 'Hola amigos como estan'
# Salida: T = ('Hola', 'amigos', 'como', 'estan')
def main():
	S = leeFrase()
	T = convierteTupla(S)
	imprimeTupla(T)
#
def leeFrase():
	s = input('Ingrese una frase no vacía: ').strip()
	while(len(s) == 0):
		print('Nada ingresó, o solo espacios!')
		s = input('Ingrese una frase no vacía: ').strip()
	return s
#
def convierteTupla(s):
	p = s.find(' ')
	t = tuple()
	while(p != -1):
		t = t + (s[:p],)
		s = s[p+1:].strip()
		p = s.find(' ')
	t = t + (s,)	
	return t
#
def imprimeTupla(t):
	print('Su tupla: {}'.format(t))
#
main()

