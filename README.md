
En la máquina Perfection de Hack The Box, se puede resolver el desafío creando un archivo en formato .py con el código expuesto a continuación. Este código se utiliza para enviar una solicitud HTTP que incluye un payload malicioso, permitiéndonos conectarnos a la web mediante un puerto que elijamos. Asegúrate de ajustar las direcciones IP y los puertos según tu configuración específica.

Aquí está el código Python que debes utilizar:

![image](https://github.com/cyb3rNAV/Payload_perfection.py/assets/170144066/0c2178d5-969b-4421-bcd6-f741e1b82018)

Para completar la explotación, asegúrate de tener un listener en tu máquina atacante usando netcat con el siguiente comando:

![image](https://github.com/cyb3rNAV/Payload_perfection.py/assets/170144066/5cd6a44d-953e-4370-b8ef-68e5706a0744)

Este código te permitirá establecer una conexión inversa desde la máquina objetivo a tu máquina atacante, facilitando la resolución del desafío en Hack The Box.


