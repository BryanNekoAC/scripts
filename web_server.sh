#!/bin/bash

on="0"
off="1"

function startServer () {
    sudo systemctl start php-fpm nginx mysql
    alacritty --working-directory /usr/share/nginx/html/ &
    echo "Servidor iniciado en: http://localhost/"
}

function stopServer () {
    sudo systemctl stop php-fpm nginx mysql
    echo "Servidor detenido"
}

echo "Preciona la opcion que desee para el servidor local: "

echo "1- Iniciar servidor
2- Detener servidor"

read -p "Introducir la opcion deseada: " choice

usr_choice=''

case $choice in 
1) usr_choice="$on";;
2) usr_choice="$off";;
esac

if [ "$usr_choice" == "0" ]
then
  startServer 
else
  stopServer 
fi

echo "Listo"

exit 0