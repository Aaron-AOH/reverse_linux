***Evil-Linux***

***Introduccion***

Esta herramienta escrita en python y bash tiene la funcion de crear un archivo malicioso que nos brindara una reverse shell sobre un dispositivo linux.
La creacion de archivos maliciosos es una interfaz muy sencilla de entender, solo tendria que introducir el numero escogido.
Una vez creado el archivo malicioso puede abrir un listener automaticamente poniendo "y" cuando pregunte por el listener, sino debera abrir un listener manualmente en ecucha del puerto que se ha configurado para el archivo malicioso.
Dos de los tres posibles archivos maliciosos tienen incorporado una herramienta de automatizacion de comandos graficamente para la post explotacion.



***Instalacion:*** 

`git clone https://github.com/Xenon/evil-linux.git`

`cd evil-linux`

`chmod +x *`

`sudo python3 requirements.py`



***Ejecucion:***

Una vez hemos realizado correctamente los pasos de la instalacion pasaremos a ejecutar la herramienta.
Con el comando:

`python3 evil-linux.py` 

La herramienta que se vera asi :


FOTO DE LA HERAMIENTA MENU
Podremos escoger si nuestro malware es un archivo .py [python] o .sh [bash]. 

*la opcion 1:* Un ejecutable python que creara una reverse shell simple, donde tendremos dificultades para movernos entre los directorios, tendriamos que listar el contenido de los directorios para ver lo que hay dentro, no podriamos movernos de la ruta en la que nos encontremos. Pero si podemos ver, modificar o eliminar lo que hay dentro de cada directorio, sabiendo la ruta completa del elemento.
Ejemplo: 

`ls /root` #Para listar los contenidos que hay dentro de root, al mostrar las subcarpetas o archivos podremos seguir navegando

`cat /root/prueba.txt`#Se mostrara el contenido del archivo txt.

*La opcion 2:* Un ejecutable bash que creara un reverse shell, a la vez que descargara una interfaz de comandos automatizados para la post explotacion.
Para poder utilizar esta interfaz/menu tendremos que poner el siguiente comando. **al conseguir la conexion:** 
`bash .autoshell.sh` 

automaticamente estaremos en un menu con diferentes funcionalidades y solo tendremos que indicar el numero de la funcion que queremos.

*La opcion 3:* Un ejecutable python que creara un reverse shell, a la vez que descargara una interfaz de comandos automatizados para la post explotacion.
Para poder utilizar esta interfaz/menu tendremos que poner el siguiente comando **al conseguir la conexion:** 
`bash .autoshell.sh` 

automaticamente estaremos en un menu con diferentes funcionalidades y solo tendremos que indicar el numero de la funcion que queremos.

***Interfaz/menu Automatizado "autoshell.sh"***
solo cuentan con esta herrmaineta las opciones  2 y 3. Para imbocarla despues de aver conseguido una reverse shell poner en la terminal el comando `bash autoshell.sh`
En caso de que no funcione poner los siguientes comandos `chmod +x *` y `./autoshell.sh` o `bash autoshell.sh`

Imagen de la herramienta autoshell.sh


**Video Demostrativo**

La guia o tutorial a fondo de esta herramienta se encuentra en este video.

url video















