class lector:
	#Atributos de la clase:
	conjunto_reglas=[]
	lt=[] #Lista de terminales.
	ln=[] #Lista de NO terminales.
	#Procesar el txt para obtener las reglas:
	def obtener_reglas(self,txt):
		archivo=open(txt,'r')

		for linea in archivo.readlines():
			print(linea,end='')
			self.conjunto_reglas.append(linea)

		archivo.close()
	#Obtener los terminales de las reglas:
	def obtener_terminales(self):
		print("OBTENIENDO TERMINALES:")
		for regla in self.conjunto_reglas:
			self.lt.append(self.obtener_subcadena(regla,'->'))
	#Obtener los no terminales de las reglas:
	def obtener_no_terminales(self):
		l_aux=[]
		print("OBTENIENDO NO TERMINALES:")
		for regla in self.conjunto_reglas:
			posicion=regla.find("->")
			cad_aux=regla[posicion+2:]
			cad_aux=cad_aux.replace(" ","")
			cad_aux=cad_aux.replace("\n","")
			#Quitando uno por uno los terminales:
			for terminal in self.lt:
				cad_aux=cad_aux.replace(terminal," ")
			l_aux.append(cad_aux)
		#l_aux es una lista que contiene todas las cadenas sin terminales.
		nt=[]
		for r_nt in l_aux:
			nt+=r_nt.split('|')

		l_aux=nt
		nt=[]
		for elemento in l_aux:
			if elemento.split() != []:
				nt+=elemento.split()

		self.ln=nt
	#Obtener el siguiente pedazo de cadena antes de un símbolo:
	def obtener_subcadena(self,cadena,simbolo):

		posicion=cadena.find(simbolo)
		temporal=cadena[:posicion]
		return temporal.replace(" ","")

#Desplegando las funciones para ver que furulen:
leer_reglas=lector()
leer_reglas.obtener_reglas('C:\\Users\\Líquido\\github\\Creator_LR0\\Reglas.txt')
leer_reglas.obtener_terminales()
leer_reglas.obtener_no_terminales()
print(leer_reglas.lt)
print(leer_reglas.ln)
