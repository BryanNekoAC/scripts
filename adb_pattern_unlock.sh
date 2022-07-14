#!/bin/sh

# Autor: BryanNekoAC (Based on Matt Wilson Script - Android pattern unlock).

# Desbloqueo de patron android via ADB

# Scipt para enviar patron de desbloquea a dispositivo android via ADB

# Este script necestita:
# que tengas instalado ADB y que este se encuentre en tu PATH, 
# tener la depuracion del dispositivo activada,
# Permisos de ejecucucion (chmod +x)

# Licencia: Uso Gratuito

# Variables a modificar: 

# PATRON="3 1 5 7 9" # El patron a dibujar, separar por 1 espacio

echo "Introduzca patron a intentar (separado por espacios):"

read PATRON

COL_1=240   # Coordenada de la primer columna X en pixeles
COL_2=540   # Coordenada de la segunda columna X en pixeles
COL_3=840   # Coordenada de la tercera columna X en pixeles


ROW_1=1270   # Coordenada de la primera fila Y en pixeles
ROW_2=1570  # Coordenada de la segunda fila Y en pixeles
ROW_3=1870  # Coordenada de la tercera fila Y en pixeles

#Definir los pares de coordenadas para cada posicion numerica

X[1]=${COL_1} 
X[2]=${COL_2} 
X[3]=${COL_3} 
X[4]=${COL_1} 
X[5]=${COL_2} 
X[6]=${COL_3} 
X[7]=${COL_1} 
X[8]=${COL_2} 
X[9]=${COL_3} 

Y[1]=${ROW_1} 
Y[2]=${ROW_1} 
Y[3]=${ROW_1} 
Y[4]=${ROW_2} 
Y[5]=${ROW_2} 
Y[6]=${ROW_2} 
Y[7]=${ROW_3} 
Y[8]=${ROW_3} 
Y[9]=${ROW_3} 


# Funciones Principales

EnviarCoordenadas () {
        adb shell sendevent /dev/input/event4 3 53 $1
        adb shell sendevent /dev/input/event4 3 54 $2
        adb shell sendevent /dev/input/event4 3 58 57
        adb shell sendevent /dev/input/event4 0 0 0
}


DibujarPatron() {
	for NUM in $PATRON
        do
           echo "Enviando: $NUM: ${X[$NUM]}, ${Y[$NUM]}"
           EnviarCoordenadas ${X[$NUM]} ${Y[$NUM]}
        done
}


adb shell input keyevent 26 # Presionar boton de bloqueo

adb shell input touchscreen swipe 930 880 930 380 # Hacer swipe hacia arriba

adb shell sendevent /dev/input/event4 1 330 1 # Iniciar Ingreso de patron

DibujarPatron # Ejecutar ingreso de patron

adb shell sendevent /dev/input/event4 3 57 4294967295 # Detener Ingreso de patron
adb shell sendevent /dev/input/event4 1 330 0
adb shell sendevent /dev/input/event4 0 0 0

echo "Patron enviado correctamente."

# Si el script te ayudo no olvides compartir ;)

exit 0
