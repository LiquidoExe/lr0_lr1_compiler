from Lector import lector
import pdb;
pdb.set_trace()

class LR1:
	#Constructor de la clase
	#lt = lista de terminales
	#ln = lista de no terminales
	#dc = diccionario de terminales-reglas
	def __init__(self,lt,ln,dc,cod):
		self.lt=lt
		self.ln=ln
		self.dc=dc
		self.cod=cod
		self.inv_cod()
		print("TERMINALES:",lt)
		print("NO TERMINALES:",ln)
		print("CÓDIGO:",self.cod)
		print("\nDICCIONARIO DE REGLAS:")
		for key in self.dc.keys():
			print(key,"\t",self.dc.get(key))
		#print("CÓDIGO:",self.inv_cod)
	#Función para invertir las llaves y los valores del dic cod.
	def inv_cod(self):
		inv_map = {v: k for k, v in self.cod.items()}
		self.inv_cod=inv_map
	#Función para obtener el First:
	#El First() se forma con el primer símbolo de una producción:
	#1. Si el símbolo es terminal, el first del símbolo es el mismo símbolo.
	#2. Si el símbolo es no terminal se vuelve a aplicar el first sobre el nuevo no terminal.
	#s = símbolo
	#c = conjunto
	#r = regla
	#res = conjunto resultado
	def first(self,s,res):
		print("First de",s,res)
		#Caso terminal:
		if s not in res and s in self.lt:
			res.append(s)
			return
		#caso no terminal:
		c=self.dc.get(s)
		if c != None:
			for r in c:
				if len(r) > 0:
					s_aux=r[0]
					if s != s_aux:
						self.first(s_aux,res)
		else:
			print("Noone.")
	#Función para obtener el Follow:
	#El Follow() de un no terminal es el First() de el símbolo que está
	#delante de él en los lados derechos.
	#Si no hay un símbolo delante, entonces se agrega el Follow del lado izquierdo.
	#Si épsilon está en el resultado se calcula el follow del lado izquierdo.
	#s = símbolo
	#c = conjunto
	#r = regla
	#k = llave
	#p = posición
	#res = conjunto resultado
	def follow(self,s,res):
		print("Follow de",s,res)
		#Si se busca el follow del primer símbolo de la gramática se agrega '$'
		if s == 0 and -1 not in res:
			res.append(-1)

		for k in self.dc.keys():
			c=self.dc.get(k)
			for r in c:
				if s in r:
					p=r.index(s)
					#Si es el último elemento se calcula el follow del lado izquierdo:
					if p == len(r)-1 and k != s:
						self.follow(k,res)
					#Si s tiene otro símbolo adelante se calcula el first de lo que sigue:
					elif p < len(r)-1:
						print("Símbolo delante:",r[p+1])
						self.first(r[p+1],res)
	#Función mover:
	#c = conjunto
	#r = regla
	#s = simbolo
	#c_f = conjunto final
	#p_s = posicion de s
	#c_r = copia de regla
	def mover(self,c,s):
		#print("moviendo",c,"con",s)
		c_f=[]
		for r in c:
			if self.a_mover(r,s) != None:
				c_f.append(self.a_mover(r,s))

		print("Resultado:",c_f)
		return(c_f)
	#Función auxiliar de mover():
	#c_r = copia de la regla
	#p = posición
	#r = regla
	#s = simbolo
	def a_mover(self,r,s):
		try:
			p=r.index(0)
		except ValueError:
			return r.copy()

		if p < len(r)-1 and r[p+1] == s:
			print("ingreso",r)
			c_r=r.copy()
			c_r.remove(0)
			c_r.insert(p+1,0)
			print("regreso",c_r)
			return c_r
		else:
			return None

	#Devolver todas las posiciones de un símbolo:
	#r = regla
	#s = símbolo
	#c_r = conjunto resultado
	def buscar_s(self,r,s):
		c_r=[]
		for p in range(len(r)):
			if s == r[p]:
				c_r.append(p)
		return c_r

#Menú:
reglas=lector()
tabla=LR1(reglas.lt,reglas.ln,reglas.diccionario,reglas.conjunto_reglas)
r=[[0,1,2,3],[1,2,0,3],[1,2,3,0]]
print(tabla.mover(r,3))
