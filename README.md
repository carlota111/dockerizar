# Desenvolvemento e integración de scripts en Python
O obxectivo deste exercicio é desenvolver dous scripts en Python que interactúen cunha API, unha base de datos MongoDB e diversas ferramentas para o manexo de datos. Ademais, inclúense opcións avanzadas para mellorar a funcionalidade e integración da solución.

## MongoDB

### Creación de MongoDB
```bash
docker run --name mongoDB -d -p 27017:27017 mongo
````

### Ejecutar MongoDB
```bash
docker exec -it mongoDB mongosh
````

## 1.	Dockerizar o primeiro script para que se poida executar dentro dun contedor Docker.
Crear una estructura donde se desenvuelva la imagen del contenedor (en letras minúsculas)
```bash
mkdir dockerizar
cd dockerizar
````
Crear fickero Dockerfile
```bash
FROM python:3.12-slim
COPY connectAPI.py /
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./connectAPI.py"]
````
Crear un requierements.txt con las librerias necesarias:
```bash
requests
pandas
pymongo
````
Crear imagen:
```bash
docker build -t dockerizar .
````
Lanzar un contedor a partir de la imagen recién creada:
```bash
docker run dockerizar
````

Dentro de la carpeta tenemos que tener:
-   connectAPI.py 
-   requirements.txt 
-   Dockerfile

## 3.	Publicar a imaxe Docker no Docker Hub.
Iniciar sesión en DockerHub desde la línea de comandos, esto nos dará un código y un enlace, abrimos el enlace e introducimos el código:
```bash
docker login
````

Etiqueta la imagen con tu nombre de usuario (carlotagp) y el nombre que quieres usar en Docker Hub:
```bash
docker tag dockerizar carlotagp/dockerizar:latest
````

Sube la imagen etiquetada a Docker Hub con el siguiente comando:
```bash
docker push carlotagp/dockerizar:latest
````

## 4.	Configura e executa a aplicación on cloud en OpenStack usando Docker (Mongo + Applicación), que quedará executándose durante as vacacións.  Calcula o número de documentos que almacenarás unha vez finalizadas as vacacións.
Debes crear una instancia en https://cloud.srv.cesga.es/project/instances/ pasádole este fichero en el apartado de "Configuración" [Descargar script_docker_ubuntu2204.sh](https://github.com/carlota111/eva_1_SBD/raw/refs/heads/main/Downloads/script_docker_ubuntu2204.sh))

Entrar a la instancia:
```bash
 ssh -J xueduaXXX@hadoop.cesga.es cesgaxuser@XXX.XXX.XXX.XXX
````

Instalar los servicios definidos en el docker-compose
```bash
 docker compose up -d
````
