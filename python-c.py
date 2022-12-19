import os

ip = input("""

Introduzca su IP

>  """)

puerto = input("""

Introduzca un puerto

>  """)

name_malware = input("""

Introduzca el un nombre

>  """)
with open(""+ name_malware +".py", "rt"")as f:
  x = f.read()
  
with open(""+ name_malware +".py", "wt"")as f:
  x = x.replace("ip", ""+ ip +"")
  x = x.replace("puerto", ""+ puerto +"")
  fin.write(x)


















