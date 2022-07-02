import os
import time
import subprocess #biblioteca comandos terminal
import re #biblioteca separar texto
from puresnmp import get 
from datetime import datetime

def anchobanda(comunidad,ipdis,numerointerfaz):
	inif1=subprocess.getoutput("snmpwalk -v2c -c "+comunidad+"  "+ipdis+" .1.3.6.1.2.1.2.2.1.10."+numerointerfaz)#in octets interfaz 1
	outif1=subprocess.getoutput("snmpwalk -v2c -c "+comunidad+" "+ipdis+" .1.3.6.1.2.1.2.2.1.16."+numerointerfaz)#out octets interfaz 1
	speedif1=subprocess.getoutput("snmpwalk -v2c -c "+comunidad+" "+ipdis+" .1.3.6.1.2.1.2.2.1.5."+numerointerfaz)#velocidad interfaz 1
	intoctets=re.sub("IF-MIB::ifInOctets."+numerointerfaz+" = Counter32: ","",inif1).replace("","")#datos entrada bits
	outoctets=re.sub("IF-MIB::ifOutOctets."+numerointerfaz+" = Counter32: ","",outif1).replace("","")#datos salida bits
	#ancho banda total (velocidad)
	velif1=re.sub("IF-MIB::ifSpeed."+numerointerfaz+" = Gauge32: ","",speedif1).replace("","")
	BW=int(velif1)-(int(intoctets)+int(outoctets))#BW disponible
	BWW=int(velif1)-BW#BW usada
	porcBW=((BW/1000)*100/100000)
	if ipdis=="209.111.20.125" and numerointerfaz=="1":
		porcBW=porcBW*10
	if ipdis=="209.111.20.125" and numerointerfaz=="2":
		porcBW=porcBW/10
	print("Ancho banda total: {} kbit/seg ".format(int(velif1)/1000))
	print("Datos entrantes: {} kbit/s".format(int(intoctets)/1000))
	print("Datos salientes {} kbit/s".format(int(outoctets)/1000))
	print("Estas usando un total de {} kbit/s".format(BWW/1000))
	print("Ancho de banda Disponible {} kbit/s = {}%".format(BW/1000,porcBW))
	archivo.write("Ancho banda total del router: {} kbit/seg\n ".format(int(velif1)/1000))
	archivo.write("Datos entrantes: {} kbit/s\n".format(int(intoctets)/1000))
	archivo.write("Datos salientes {} kbit/s\n".format(int(outoctets)/1000))
	archivo.write("Estas usando un total de {} kbit/s\n".format(BWW/1000))
	archivo.write("Ancho de banda Disponible {} kbit/s = {}%\n".format(BW/1000,porcBW))
	if bwumbral > porcBW:
		
		if ipdis=="209.111.10.100" and numerointerfaz=="1":
			mensajeif="UMBRAL ANCHO DE BANDA DISPONIBLE MENOR AL ESPERADO EN ROUTER INTERFAZ 1 HORARIO: {}".format(datetime.now())
			asuntoif="UMBRAL ANCHO DE BANDA SUPERADO ROUTER IF 1"
			correoif="echo '"''+mensajeif+''"' | mail -s '"''+asuntoif+''"' tonomoradta@hotmail.com"
		if ipdis=="209.111.10.100" and numerointerfaz=="2":
			mensajeif="UMBRAL ANCHO DE BANDA DISPONIBLE MENOR AL ESPERADO EN ROUTER INTERFAZ 2 HORARIO: {}".format(datetime.now())
			asuntoif="UMBRAL ANCHO DE BANDA SUPERADO ROUTER IF 2"
			correoif="echo '"''+mensajeif+''"' | mail -s '"''+asuntoif+''"' tonomoradta@hotmail.com"
		if ipdis=="209.111.20.125" and numerointerfaz=="1":
			mensajeif="UMBRAL ANCHO DE BANDA DISPONIBLE MENOR AL ESPERADO EN PC INTERFAZ 1 HORARIO: {}".format(datetime.now())
			asuntoif="UMBRAL ANCHO DE BANDA SUPERADO PC IF 1"
			correoif="echo '"''+mensajeif+''"' | mail -s '"''+asuntoif+''"' tonomoradta@hotmail.com"
		if ipdis=="209.111.20.125" and numerointerfaz=="2":
			mensajeif="UMBRAL ANCHO DE BANDA DISPONIBLE MENOR AL ESPERADO EN PC INTERFAZ 2 HORARIO: {}".format(datetime.now())
			asuntoif="UMBRAL ANCHO DE BANDA SUPERADO PC IF 2"
			correoif="echo '"''+mensajeif+''"' | mail -s '"''+asuntoif+''"' tonomoradta@hotmail.com"	
		os.system(correoif)
		print("****ALERTA ANCHO DE BANDA DISPONIBLE MENOR AL ESPERADO CORREO ENVIADO****")
		archivo.write("\n****ALERTA ANCHO DE BANDA DISPONIBLE MENOR AL ESPERADO CORREO ENVIADO****\n")


def umbralmemoria():
	while True:
		tmumbral=int(input("Ingrese umbral para la Memoria USADA en porcentaje de 0-100 "))
		if(tmumbral<0 or tmumbral>100):
			print("Error Umbral fuera de rango")
		else:
			return tmumbral
			break

def umbralprocesador():
	while True:
		tpumbral=int(input("Ingrese umbral de maxima carga del procesador en porcentaje 0-100 "))
		if(tpumbral<0 or tpumbral>100):
			print("Error umbral fuera de rango")
		else:
			return tpumbral
			break
def umbralanchobanda():
	while True:
		tbwumbral=int(input("Ingrese umbral de ancho de banda disponible en porcentaje 0-100 "))
		if(tbwumbral<0 or tbwumbral>100):
			print("Error umbral fuera de rango")
		else:
			return tbwumbral
			break
def umbraldisco():
	while True:
		tdumbral=int(input("Ingrese umbral de almacenamiento restante en porcentaje 0-100 "))
		if(tdumbral<0 or tdumbral>100):
			print("Error umbral fuera de rango")
		else:
			return tdumbral
			break
def tiempoumbral():
	ttimeumbral=int(input("\nIngrese cada cuantos minutos desea cambiar sus umbrales "))
	return ttimeumbral
	
mumbral=umbralmemoria()
pumbral=umbralprocesador()
dumbral=umbraldisco()
bwumbral=umbralanchobanda()
timeumbral=tiempoumbral()
nummon=1
errorrouter=0
errorpc=0	
while True:
	os.system("clear")
	archivo=open('DatosMonitorizacion.txt','a')
	print("Umbales:")
	print("Memoria: {}% Procesador: {}% Ancho de banda {}% Disco: {}%".format(mumbral,pumbral,bwumbral,dumbral))
	archivo.write("\nUmbales:\n")
	archivo.write("\nMemoria: {}% Procesador: {}% Ancho de banda {}% Disco: {}%\n".format(mumbral,pumbral,bwumbral,dumbral))
	
	archivo.write("\n**********Monitorizacion numero: {}***********\n".format(nummon))
	ip="209.111.10.100"
	community="LECT"
	
	#**********ROUTER***************
	
	timerout=datetime.now()
	timeout=subprocess.getoutput("snmpwalk -v2c -c LECT "+ip+" .1.3.6.1.2.1.1.3.0")#COMANDO PARA VER RESPUESTA
	error="Timeout: No Response from "+ip
	if (error==timeout):
		errorrouter=errorrouter+1
		mensaje="ERROR ROUTER "+ip+" NO RESPONDIO HORARIO INCIDENTE: {}".format(timerout)
		asunto="FALLA DEL ROUTER"
		correo="echo '"''+mensaje+''"' | mail -s '"''+asunto+''"' tonomoradta@hotmail.com"
		os.system(correo)
		print(mensaje+"\nCORREO ENVIADO")
		print("Falla ocurrida: ",error)
		archivo.write(mensaje+"\nCORREO ENVIADO\n ")
		archivo.write("Falla ocurrida: "+error+"\n")
	else:
		print("")
		print("******DATOS DEL ROUTER******")
		archivo.write("\n")
		archivo.write("******DATOS DEL ROUTER******\n")
		#MEMORIA
		oidmem="1.3.6.1.4.1.9.2.1.8.0" #oid memoria disponible
		ciscousedmemorybits=get(ip,community,oidmem)#memoria disponible en bits
		ciscousedmemorymbits=ciscousedmemorybits/1000000#Memoria disponible en MiB
		ciscoporcentajememory=ciscousedmemorymbits*100/512#porcentaje memoria
		memdis=512-ciscousedmemorymbits
		print("______________________________________________________")
		print("INFORMACION DE MEMORIA")
		print("")
		print("Memoria total del router: 512 Mib") 
		print("memoria usada router: {0:.2f} Mib".format(ciscousedmemorymbits))
		print("Memoria disponible router {0:.2f}".format(memdis))
		print("El porcentaje de RAM usada del router es: {0:.2f}%".format(ciscoporcentajememory))
		archivo.write("______________________________________________________\n")
		archivo.write("INFORMACION DE MEMORIA\n")
		archivo.write("")
		archivo.write("Memoria total del router: 512 Mib\n") 
		archivo.write("memoria usada router: {0:.2f} Mib\n".format(ciscousedmemorymbits))
		archivo.write("Memoria disponible router {0:.2f}\n".format(memdis))
		archivo.write("El porcentaje de RAM usada del router es: {0:.2f}%\n".format(ciscoporcentajememory))

		ciscomemrest=100-ciscoporcentajememory
		print("Queda libre el {0:.2f}% de memoria RAM".format(ciscomemrest))
		archivo.write("Queda libre el {0:.2f}% de memoria RAM\n".format(ciscomemrest))
		
		if mumbral < ciscoporcentajememory:
			mensaje="UMBRAL DE MEMORIA ROUTER SOBREPASADO HORARIO: {}".format(timerout)
			asunto="UMBRAL MEMORIA ROUTER"
			correo="echo '"''+mensaje+''"' | mail -s '"''+asunto+''"' tonomoradta@hotmail.com"
			os.system(correo)
			print("****ALERTA USO DE MEMORIA SOBREPASADO CORREO ENVIADO****")
			archivo.write("\n****ALERTA USO DE MEMORIA SOBREPASADO CORREO ENVIADO****\n")
		archivo.write("________________________________________\n")	
		print("______________________________________________________")

		#CPU
		print("INFORMACION DEL CPU")
		archivo.write("\nINFORMACION DEL CPU\n")
		oidcpu="1.3.6.1.4.1.9.2.1.57.0"#oid carga cpu 1 minuto
		ciscocpucarga=get(ip,community,oidcpu)#carga cpu 1 minuto
		print("")
		print("Carga del procesador en el ultimo minuto: {}%".format(ciscocpucarga))
		print("_______________________________________________________")
		archivo.write("\nCarga del procesador en el ultimo minuto: {}%\n".format(ciscocpucarga))
		if pumbral < ciscocpucarga:
			mensaje="USO DE CPU DEL ROUTER SOBREPASADO HORARIO: {}".format(timerout)
			asunto="UMBRAL CPU ROUTER"
			correo="echo '"''+mensaje+''"' | mail -s '"''+asunto+''"' tonomoradta@hotmail.com"
			os.system(correo)
			print("****ALERTA USO DE CPU SOBREPASADO CORREO ENVIADO****")
			archivo.write("\n****ALERTA USO DE CPU SOBREPASADO CORREO ENVIADO****\n")

		archivo.write("_______________________________________________________\n")

		#Ancho de banda ROUTER
		print("INFORMACION DE LAS INTERFACES")
		print("****INTERFAZ 1****")
		anchobanda(community,ip,"1")
		print("\n****INTERFAZ 2****")
		archivo.write("\n****INTERFAZ 2****\n")
		print("")
		anchobanda(community,ip,"2")
	
	#***********PC*********************
	
	timepc=datetime.now()
	ippc="209.111.20.125"
	compc="public"
	pctimeout=subprocess.getoutput("snmpwalk -v2c -c public "+ippc+" .1.3.6.1.2.1.1.3.0")#COMANDO PARA VER RESPUESTA
	pcerror="Timeout: No Response from "+ippc
	if pcerror==pctimeout:
		errorpc=errorpc+1
		mensaje="ERROR PC "+ippc+"NO RESPONDIO HORARIO INCIDENTE: {}".format(timepc)
		asunto="FALLA DE LA PC"
		correo="echo '"''+mensaje+''"' | mail -s '"''+asunto+''"' tonomoradta@hotmail.com"
		os.system(correo)
		print("\n"+mensaje+"\nCORREO ENVIADO")
		archivo.write("\n"+mensaje+"\nCORREO ENVIADO")

	else:
		print("")
		print("******DATOS DE LA MAQUINA VIRTUAL******")
		archivo.write("\n******DATOS DE LA MAQUINA VIRTUAL******\n")
		#MEMORIA
		oidmemtot="1.3.6.1.4.1.2021.4.5.0" #oid memoria total
		pcmemtot=get(ippc,compc,oidmemtot)#memoria disponible en kbytes
		pcmemtotgb=pcmemtot/1000000
		oidmemused="1.3.6.1.4.1.2021.4.6.0"
		pcmemused=get(ippc,compc,oidmemused)#memoria usada en kBytes
		pcmemusedgb=pcmemused/1000000
		oidmemfree="1.3.6.1.4.1.2021.4.11.0"
		pcmemfree=get(ippc,compc,oidmemfree)
		pcmemfreegb=pcmemfree/1000000
		porcmemused=pcmemusedgb*100/pcmemtotgb
		porcmemfree=100-porcmemused
		print("______________________________________________________")
		print("INFORMACION DE MEMORIA")
		print("")
		print("Memoria RAM total de la pc : {0:.2f} gb".format(pcmemtotgb)) 
		print("memoria RAM usada en la pc: {0:.3f} gb".format(pcmemusedgb))
		print("Memoria RAM libre en pc: {0:.3f} gb".format(pcmemfreegb))
		print("Porcentaje RAM usada {0:.2f}%".format(porcmemused))
		print("Porcentaje RAM disponible {0:.2f}%".format(porcmemfree))
		print("______________________________________________________")

		archivo.write("______________________________________________________\n")
		archivo.write("INFORMACION DE MEMORIA\n")
		archivo.write("\n")
		archivo.write("Memoria RAM total de la pc : {0:.2f} gb\n".format(pcmemtotgb)) 
		archivo.write("memoria RAM usada en la pc: {0:.3f} gb\n".format(pcmemusedgb))
		archivo.write("Memoria RAM libre en pc: {0:.3f} gb\n".format(pcmemfreegb))
		archivo.write("Porcentaje RAM usada {0:.2f}%\n".format(porcmemused))
		archivo.write("Porcentaje RAM disponible {0:.2f}%\n".format(porcmemfree))
		if mumbral < porcmemused:
			mensaje="UMBRAL DE MEMORIA PC SOBREPASADO HORARIO: {}".format(timerout)
			asunto="UMBRAL MEMORIA PC"
			correo="echo '"''+mensaje+''"' | mail -s '"''+asunto+''"' tonomoradta@hotmail.com"
			os.system(correo)
			print("****ALERTA USO DE MEMORIA SOBREPASADO CORREO ENVIADO****")
			archivo.write("\n****ALERTA USO DE MEMORIA SOBREPASADO CORREO ENVIADO****\n")
		print("______________________________________________________")

		archivo.write("______________________________________________________\n")
		#CPU
		oidcpupc="1.3.6.1.4.1.2021.11.9.0"#OID CPU USE PORCENTAJE
		cpupcuse=get(ippc,compc,oidcpupc)
		print("INFORMACION CPU")
		print("")
		print("Porcentaje uso CPU: {}%".format(cpupcuse))
		archivo.write("INFORMACION CPU\n")
		archivo.write("\n")
		archivo.write("Porcentaje uso CPU: {}%\n".format(cpupcuse))
		if pumbral < cpupcuse:
			mensaje="USO DE CPU DE PC SOBREPASADO HORARIO: {}".format(timerout)
			asunto="UMBRAL CPU PC"
			correo="echo '"''+mensaje+''"' | mail -s '"''+asunto+''"' tonomoradta@hotmail.com"
			os.system(correo)
			print("****ALERTA USO DE CPU SOBREPASADO CORREO ENVIADO****")
			archivo.write("\n****ALERTA USO DE CPU SOBREPASADO CORREO ENVIADO****\n")
		print("___________________________________________________")
		archivo.write("________________________________________\n")
		
		#Ancho de banda PC
		print("INFORMACION DE LAS INTERFACES PC")
		print("****INTERFAZ 1****")
		archivo.write("INFORMACION DE LAS INTERFACES PC\n")
		archivo.write("****INTERFAZ 1****\n")
		print("")
		anchobanda(compc,ippc,"1")	
		print("\n****INTERFAZ 2****")
		archivo.write("\n****INTERFAZ 2****\n")
		print("")
		anchobanda(compc,ippc,"2")
		
		#ALMACENAMIENTO
		oiddisktot="1.3.6.1.4.1.2021.9.1.6.1"#OID TAMAÑO TOTAL HDD KBYTES
		disktot=get(ippc,compc,oiddisktot)
		disktotgb=disktot/1000000
		oiddiskuse="1.3.6.1.4.1.2021.9.1.8.1"#OID DISCO USADO KBYTES
		diskuse=get(ippc,compc,oiddiskuse)
		diskusegb=diskuse/1000000
		oiddiskfree="1.3.6.1.4.1.2021.9.1.7.1"#OID DISCO DISPONIBLE KBYTES
		diskfree=get(ippc,compc,oiddiskfree)
		diskfreegb=diskfree/1000000
		oidporcdiskuse="1.3.6.1.4.1.2021.9.1.9.1"
		porcdiskuse=get(ippc,compc,oidporcdiskuse)
		porcdiskfree=100-porcdiskuse
		print("INFORMACION ALMACENAMIENTO")
		print("")
		print("Tamaño total del disco: {0:.2f} gb".format(disktotgb))
		print("Has usado un total de: {0:.2f} gb".format(diskusegb))
		print("Queda Disponible: {0:.2f} gb".format(diskfreegb))
		print("Porcentaje usado: {}%".format(porcdiskuse))
		print("Porcentaje libre: {}%".format(porcdiskfree))
		archivo.write("___________________________________\n")
		archivo.write("\nINFORMACION ALMACENAMIENTO\n")
		archivo.write("\n")
		archivo.write("Tamaño total del disco: {0:.2f} gb\n".format(disktotgb))
		archivo.write("Has usado un total de: {0:.2f} gb\n".format(diskusegb))
		archivo.write("Queda Disponible: {0:.2f} gb\n".format(diskfreegb))
		archivo.write("Porcentaje usado: {}%\n".format(porcdiskuse))
		archivo.write("Porcentaje libre: {}%\n".format(porcdiskfree))
		if dumbral > porcdiskfree:
			mensaje="QUEDA MENOS ESPACIO DE ALMACENAMIENTO DEL QUE SE ESPERA HORARIO: {}".format(timerout)
			asunto="UMBRAL ALMACENAMIENTO PC"
			correo="echo '"''+mensaje+''"' | mail -s '"''+asunto+''"' tonomoradta@hotmail.com"
			os.system(correo)
			print("****ALERTA QUEDA MENOS ESPACIO DEL ESPERADO CORREO ENVIADO****")
			archivo.write("\n****ALERTA QUEDA MENOS ESPACIO DEL ESPERADO CORREO ENVIADO****\n")
	archivo.close()
	nummon=nummon+1
	if timeumbral==0:
		mensaje="DEBE CAMBIAR LOS UMBRALES"
		asunto="CAMBIO UMBRALES"
		correo="echo '"''+mensaje+''"' | mail -s '"''+asunto+''"' tonomoradta@hotmail.com"
		os.system(correo)
		mumbral=umbralmemoria()
		pumbral=umbralprocesador()
		dumbral=umbraldisco()
		bwumbral=umbralanchobanda()
		timeumbral=tiempoumbral()
	print("QUEDAN {} minutos antes de tener que modificar los umbrales".format(timeumbral))
	timeumbral=timeumbral-1
	print("Esperando la monitorizacion numero: {}".format(nummon))
	if errorrouter==3 and errorpc==3:
		mensaje="PROGRAMA CERRADO PORQUE NO MONITOREO NADA EN 3 MINUTOS"
		asunto="MONITOREO TERMINADO"
		correo="echo '"''+mensaje+''"' | mail -s '"''+asunto+''"' tonomoradta@hotmail.com"
		os.system(correo)
		print("NO MONITOREASTE NADA EN 3 MINUTOS, PROGRAMA CERRADO")
		exit()
	time.sleep(60)
