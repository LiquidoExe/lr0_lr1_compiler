from Lector import lector
import pdb;
pdb.set_trace()
#Clase para crear la tabla LLR0:
class LLRO:
	#Constructor de la clase
	#lt = lista de terminales
	#ln = lista de no terminales
	#dc = diccionario de terminales-reglas
	def __init__(self,lt,ln,dc):
		self.lt=lt
		self.ln=ln
		self.dc=dc
		print("\nTERMINALES:",self.lt)
		print("\nNO TERMINALES:",self.ln)
		print("\nDICCIONARIO DE REGLAS:")

		for key in self.dc.keys():
			print(key,"\t",self.dc.get(key))
	#Funcion para crear las cerraduras:
	def cerradura(self,c_e):
		c_final=[]
		p_final=0
		for x in c_e:
			if x not in c_final:
				c_final.append(x)

			while p_final < len(c_final):
				c=c_final[p_final]
				p=c.index(0)
				print("Lista",c,"en posicion",p)

				if p+1 < len(c):
					sig=c[p+1]
					print("La siguiente va a ser cerradura de",sig)
					l_aux=self.dc.get(sig)

					if l_aux is not None:
						print(l_aux)

						for e in l_aux:
							e_c=e.copy()
							e_c.insert(0,0)
							if e_c not in c_final:
								c_final.append(e_c)
								print("Agregando")
				p_final+=1
				print(c_final)
reglas=lector()
tabla=LLRO(reglas.lt,reglas.ln,reglas.diccionario)
tabla.cerradura([[0,2]])
