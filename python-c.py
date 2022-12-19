import os

ip = input("""

Introduzca su IP

>  """)

puerto = input("""

Introduzca un puerto

>  """)

with open(""+ name_malware +", "rt"")as f:
  x = f.read()
  
with open(""+ name_malware +", "wt"")as f:
  x = x.replace("ip", ""+ ip +"")
  x = x.replace("puerto", ""+ puerto +"")
  fin.write(x)


















