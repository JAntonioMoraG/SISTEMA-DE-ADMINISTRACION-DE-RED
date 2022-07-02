# MINI SISTEMA DE ADMINISTRACION DE RED 
## Autor: Mora Guzman Jose Antonio
Mini sistema de administracion de red, realizado como proyecto final de la materia de Administracion de Servicios en Red de la ESCOM IPN

## DESCRIPCION DEL PROYECTO:
Realizar una aplicación que monitoree las siguientes variables de los dispositivos de la red (Máquina virtual y Router):
* Memoria
* Procesador
* Almacenamiento (solo Máquina virtual)
* Ancho de banda (Interfaces) 

## REQUERIMIENTOS FUNCIONALES: 
* La monitorización se debe realizar cada minuto.
* Guardar la información de monitorización en una base de datos o un archivo de texto.
* Utilizando las variables mencionadas, seleccionar un umbral para cada una por ejemplo 10% de Memoria RAM disponible. Cada vez que se sobrepase ese umbral, se deberá
enviar un correo al administrador de la red con la siguiente información:
  * Fecha y hora en que ocurrió el incidente
  * Dispositivo en que ocurrió
  * Falla ocurrida
* Si alguno de los dispositivos tarda más tiempo del registrado en responder se deberá enviar una notificación al administrador con la información del dispositivo y la fecha y hora.

## REQUERIMIENTOS NO FUNCIONALES
* Usar el lenguaje de programación y sistema operativo que deseen.
* La aplicación debe permitir modificar los umbrales a petición del usuario.

## TOPOLOGIA DE RED 
![TOPOLOGIA](https://github.com/JAntonioMoraG/SISTEMA-DE-ADMINISTRACION-DE-RED/blob/main/Imagenes/TOPOLOGIA.png)

## DIAGRAMA DE CASOS DE USO
![DIAGRAMA CASOS DE USO](https://github.com/JAntonioMoraG/SISTEMA-DE-ADMINISTRACION-DE-RED/blob/main/Imagenes/DiagramaCasosUso.png)

## ARQUITECTURA DEL SISTEMA
![ARQUITECTURA DEL SISTEMA](https://github.com/JAntonioMoraG/SISTEMA-DE-ADMINISTRACION-DE-RED/blob/main/Imagenes/ArquitecturaSistema.drawio.png)

## DIAGRAMA DE CLASES 
![DIAGRAMA DE CLASES](https://github.com/JAntonioMoraG/SISTEMA-DE-ADMINISTRACION-DE-RED/blob/main/Imagenes/DiagramadeClases.drawio.png)

## DIAGRAMA DE FLUJO
![DIAGRAMA DE FLUJO](https://github.com/JAntonioMoraG/SISTEMA-DE-ADMINISTRACION-DE-RED/blob/main/Imagenes/DiagramaFlujo.drawio.png)

## CONTENIDO DEL PROYECTO 
* Dentro de la carpeta [ProyectoRedes3](https://github.com/JAntonioMoraG/SISTEMA-DE-ADMINISTRACION-DE-RED/tree/main/ProyectoRedes3) se encuentra la topologia de red realizada en el programa GNS3, la topología ya esta configurada.
* El archivo [proyecto.py](https://github.com/JAntonioMoraG/SISTEMA-DE-ADMINISTRACION-DE-RED/blob/main/proyecto.py) 
* Si quieres leer el reporte completo del proyecto da clic [aqui](https://github.com/JAntonioMoraG/SISTEMA-DE-ADMINISTRACION-DE-RED/blob/main/Proyecto_FinalMGJA.pdf)

