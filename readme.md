IntroducciÃ³n

Esta herramienta escrita en python y bash tiene la funciÃ³n de crear un archivo malicioso que nos brindarÃ¡ una reverse shell sobre un dispositivo linux.
La creaciÃ³n de archivos maliciosos es una interfaz muy sencilla de entender, solo tendrÃ­a que introducir el numero escogido.
Una vez creado el archivo malicioso puede abrir un listener automaticamente poniendo "y" cuando pregunte por el listener, sino deberÃ¡ abrir un listener manualmente en ecucha del puerto que se ha configurado para el archivo malicioso.
Dos de los tres posibles archivos maliciosos tienen incorporado una herramienta de automatizaciÃ³n de comandos graficamente para la post explotaciÃ³n.



InstalaciÃ³n: 

git clone https://github.com/Xenon/evil-linux.git
cd evil-linux
chmod +x *
sudo python3 requirements.py



EjecuciÃ³sn:**

Una vez hemos realizado correctamente los pasos de la instalaciÃ³n pasaremos a ejecutar la herramienta.
Con el comando python3 evil-linux.py iniciaremos la herramienta que se verÃ¡ asÃ­:
FOTO DE LA HERAMIENTA MENÃš
Podremos escoger si nuestro malware es un archivo .py [python] o .sh [bash]. 

la opciÃ³n 1: Un ejecutable python que crearÃ¡ una reverse shell simple, donde tendremos dificultades para movernos entre los directorios, tendrÃ­amos que listar el contenido de los directorios para ver lo que hay dentro, no podrÃ­amos movernos de la ruta en la que nos encontremos.

La opciÃ³n 2: Un ejecutable bash que crearÃ¡ un reverse shell, a la vez que descargarÃ¡ una interfaz de comandos automatizados para la post explotaciÃ³n.
Para poder utilizar esta interfaz/menÃº tendremos que poner el siguiente comando al conseguir la conexiÃ³n: "bash .autoshell.sh" automaticamente estaremos en un menÃº condiferentes funcionalidades y solo tendremos que indicar el numero de la funciÃ³n que queremos.

La opciÃ³n 3: Un ejecutable python que crearÃ¡ un reverse shell, a la vez que descargarÃ¡ una interfaz de comandos automatizados para la post explotaciÃ³n.
Para poder utilizar esta interfaz/menÃº tendremos que poner el siguiente comando al conseguir la conexiÃ³n: "bash .autoshell.sh" automaticamente estaremos en un menÃº condiferentes funcionalidades y solo tendremos que indicar el numero de la funciÃ³n que queremos.


Video Demostrativo

video youtube













