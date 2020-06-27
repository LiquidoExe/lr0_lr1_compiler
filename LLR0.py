from Lector import lector
import pdb;
pdb.set_trace()
#Clase para crear la tabla LLR0:
class LLRO:
	#Constructor de la clase
	#lt = lista de terminales
	#ln = lista de no terminales
	#dc = diccionario de terminales-reglas
	def __init__(self,lt,ln,dc,cod):
		self.lt=lt
		self.ln=ln
		self.dc=dc
		self.cod=cod
		#print("\nTERMINALES:",self.lt)
		#print("\nNO TERMINALES:",self.ln)
		#print("\nDICCIONARIO DE REGLAS:")
		print("TERMINALES:",lt)
		print("NO TERMINALES:",ln)
		for key in self.dc.keys():
			print(key,"\t",self.dc.get(key))
	#Función para crear las cerraduras:
	#C_E = Conjunto de reglas externo a la función.
	def cerradura(self,c_e):
		c_final=[]
		p_final=0
		for x in c_e:
			if x not in c_final:
				c_final.append(x)

			while p_final < len(c_final):
				c=c_final[p_final]
				p=c.index(0)
				#print("Lista",c,"en posicion",p)

				if p+1 < len(c):
					sig=c[p+1]
					#print("La siguiente va a ser cerradura de",sig)
					l_aux=self.dc.get(sig)

					if l_aux is not None:

						for e in l_aux:
							e_c=e.copy()
							e_c.insert(0,0)
							if e_c not in c_final:
								c_final.append(e_c)
				p_final+=1
				#print(c_final)
		#print("\t\tCerradura:",c_final)
		return c_final
	#Función para mover el punto:
	#c = Conjunto de reglas externo a la función.
	#s = Símbolo para mover()
	#p_s = posición del símbolo.
	def mover(self,c,s):
		c_f=[]
		for r in c:
			if s in r:
				p_s=r.index(s)
				if r.index(s) > 0 and r.index(0) == r.index(s)-1:
					c_c=r.copy()
					p=c_c.index(0)
					#print("0 en posición",p)
					if p != len(c_c) -1:
						c_c.pop(p)
						c_c.insert(p+1,0)
						c_f.append(c_c)
					else:
						c_f.append([])
		#print("Mover:",c_f)
		return(c_f)
	#Funcion ir_a:
	def ir_a(self,c,s):
		return self.cerradura(self.mover(c,s))
	#Función para obtener los símbolos antes del punto:
	#c = conjunto de reglas.
	def posteriores(self,c):
		post=[]
		for r in c:
			if r.index(0) < len(r)-1 and r[r.index(0)+1] not in post:
				post.append(r[r.index(0)+1])
		return post
	#Función para utilizar ir_a en los diferentes conjuntos:
	#pool = donde se guardan todos los conjuntos resultantes i(x)
	#p = posicion
	#s = simbolo
	#c = conjunto simple
	#l_r = lista relaciones contiene los conjuntos que salieron de otro conjunto.
	#r = relaciones
	def crear(self):
		pool=[]
		l_r=[]
		pool.append(self.cerradura([[0,1]]))
		p=0

		while p < len(pool):
			r=[]
			#print("Analizando el conjunto I("+str(p)+"):")
			for s in self.posteriores(pool[p]):
			#	print("\tBuscando el símbolo",s,":")
				c=self.ir_a(pool[p],s)
				if c not in pool:
					pool.append(c)
				r.append([s,pool.index(c)])
			l_r.append(r)
			p+=1

		#print("")
		#for conjunto in pool:
		#	print(conjunto)
		print("RELACIONES ENTRE LOS CONJUNTOS:")
		for conjunto in l_r:
			print(conjunto)
	#Función para calcular el follow de un simbolo:
	def follow(self,s):
		print (self.cod)


#Menú----------------------------------
reglas=lector()
tabla=LLRO(reglas.lt,reglas.ln,reglas.diccionario,reglas.conjunto_reglas)
tabla.crear()
tabla.follow(1)
