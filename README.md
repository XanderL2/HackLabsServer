# ¿Que es Hacklabs Server?

![enter image description here](https://raw.githubusercontent.com/XanderL2/HackLabsServer/main/.preview/logo.png)

Hack Labs server es una plataforma de estadisticas interactiva la cual te permite comparar estadisticas de Hacking con las de otras personas. Estas estadisticas son recolectadas por la herramienta (Link a Pentest Tool). *Por ejemplo:*  Si tu logras penetrar una maquina con ayuda de las herramientas de Pentesting esta se añadira a tus estadisticas, siendo posible verlas de manera interactiva a traves de la web. 

Ademas, esta te permite ver las estadisticas de otras personas, ver las personas Top, etc. Por otro lado, esta te ofrece la capacidad de cambiar tu foto de perfil, nombre de usuario, contraseña, etc.


## Arquitectura y Tecnologias del Proyecto:

![enter image description here](https://raw.githubusercontent.com/XanderL2/HackLabsServer/main/.preview/architecure.png)


- **REST API - Backend:** La aplicacion hace uso de una API REST de codigo libre creada en Express JS por mi mismo, esta te permite realizar las operaciones basicas HTTP, ademas de añadidos como autenticacion mediante JWT (Json Web Tokens), paginacion, etc.



    **Tenologias**
    - *Node JS:* Entorno de Ejecución
    - *Express JS:* Framework de desarrollo
    - *JWT (Json Web Tokens):* Autenticacion
    - *Json:* Lenguaje de transmision de datos
    - *Middleware de Loggin:* Morgan
    - *Conexiones SQL:* Mysql2


- **Frontend Server:** 

    **Tenologias**
    - *HTML:* Lenguaje de hipertexto marcado basico.
    - *CSS:* Estilos de la pagina.
    - *JavaScript:* Dinamismo y funcionalidad Web
    - *Jinja:* Motor de plantillas para generar contenido dinamico.


    - *Flask:* Servicio para retorno de paginas principal.

![enter image description here](https://raw.githubusercontent.com/XanderL2/HackLabsServer/main/.preview/index.png)<br>
![enter image description here](https://raw.githubusercontent.com/XanderL2/HackLabsServer/main/.preview/landing.png)


### Referencias:
-  https://codepen.io/Str3lla/pen/KKLPObK
-  https://codepen.io/jh3y/pen/MWLyGxo
-  https://codepen.io/dtab428/pen/GRPVQXR
- https://codepen.io/TurkAysenur/pen/RwWKYMO
