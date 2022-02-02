# Docker

## Table of Contents

- [Docker](#docker)
  - [Table of Contents](#table-of-contents)
  - [Sources](#sources)
  - [Docker](#docker-1)
  - [Container](#container)
  - [Image](#image)
  - [Volumes](#volumes)
  - [Commands](#commands)
    - [Containers](#containers)
    - [Images](#images)
    - [Volumes](#volumes-1)
  - [Dockerfile](#dockerfile)
  - [Django Docker Set-up (vide CS50)](#django-docker-set-up-vide-cs50)

## Sources

- [CS50 Harvard Course](https://cs50.harvard.edu/web/2020/weeks/7/)
- [Docker-Compose for Django and React with Nginx reverse-proxy and Let's encrypt certificate](https://saasitive.com/tutorial/docker-compose-django-react-nginx-let-s-encrypt/)
- [Docker & Kubernetes: The Practical Guide](https://www.udemy.com/course/docker-kubernetes-the-practical-guide/)

## Docker

- Docker, unlike hypervisors, is not meant to virtualize environments of the different systems. Main purpose of Docker is to package and containerize the application and to ship it and to run it anywhere, at any time, as many times as desired.

## Container

- **Containers** are isolated environments that have seperate processes, network and mounts, but share the same OS kernel. Applications are separated and can use different libraries and have different dependencies.

## Image

- **Docker image** is just a package template that is used to create containers.

- Image can be viewed as a set of layers where each command inside a Dockerfile is a separate layer. Each layer is cached and **can be re-used if no changes were made within this layer and layers before it**. It is therefore important to think through the order of each command to optimize building process.

- Docker image is read-only - after code is built image is locked. To make changes in code it needs to be rebuilt and new image needs to be created.

- Images for different technologies are available on **Docker Hub**.

## Volumes

- **Volumes** are folders on your host machine hard drive which are mounted (mapped) into containers.

- Volumes persist if a container shuts down. If a container re-starts/starts and mounts a volume, any data inside of that volume is available in the container.

- A container can write data into a volume and read data from it.

- Volumes can be either **managed by Docker** (location of volume is unknown) or **managed by you** in case of **bind volumes**.

- Volumes managed by Docker divide into anonymous volumes and named volumes.

- Anonymous volumes are not getting re-used. Everytime container (with defined volume) is being run a new volume is being created.

- Named volumes persists and can be pointed to when running a container.

### Bind Mounts

- **Bind Mounts** are like volumes, but are managed by us.

## Commands

### Containers

- To run a new instance of an app use: `docker run [container]`. Use `run -d` to run a container in a detached mode. To attach a container running in a detached state use `docker attach [container_id]`.

  - `-it` exposes a container's terminal with which we can interact.
  - `-p local_port:exposed_port` publishes an exposed port to the host port.
  - `--rm` automatically removes the container when it exists.
  - `--name` names a container.

- `docker ps` - lists currently running containers. `docker ps -a` - lists all containers (running currently or in the past).

- `docker stop [container]` - stops running container.

- `docker rm [container]` - removes a container permanently.

- `docker start [container]` - restarts stopped container (it does not create a new container) and runs it in the detached mode. Add `-a` flag to restart a container in an attached mode.

- `docker attach [container]` - attaches current terminal to the running container.

- `docker logs [container]` - fetches the logs printed by a container.

  - Add `-f` flag to keep on listening to the changes in the container logs (equivalent of attaching to the container).

- `docker container prune` - removes all stopped containers.

- `docker cp source destination` - allows to copy folders and files to and from running container.

### Images

- Image names follow the *name:tag* convention. Name indicates an image group whereas tag indicates specialized version of this group.

- `docker build -t name:tag` build an image with the specified name and tag.

- `docker tag current_name:new_name` - clones an image giving it a different name.

- To list all installed images `docker images` or `docker image ls`.

- `docker rmi [image]` - removes an image (all related containers must be stopped before deleting an image).

- `docker image prune` - removes all unused Docker images. Add `-a` flag to also remove tagged images.

- `docker image inspect` - inspects an image (ID, creation date, container configuration, OS, layers, etc.).

- `docker push [image]` - pushes an image to DockerHub. Use `HOST:NAME` if you want to push an image to a private registry.

- `docker pull [image]` - pulls an image from DockerHub. Use `HOST:NAME` if you want to pull an image from private registry.

### Volumes

- `docker run -v VOL_NAME:/path/in/the/container/` - runs a container using named volume for given path.

- `docker volume rm VOL_NAME` - deletes given volume.

- `docker volume prune` - deletes all unused volumes (anonymous ones).

## Dockerfile

- After creating a 'Dockerfile' it should be populated with instructions:

```dockerfile
# image upon on which new image will be created
FROM node
# set up working directory from which commands will be run
WORKDIR /app
# copy the code from the current folder to the workdir (explicitly; instead can be just "."
# since workdir has been set)
COPY . /app
# runs the command to create an image
RUN npm install
# this command is optional and is used solely for documentation purpose
EXPOSE 80
# runs when new container is created based on this image
CMD ["node", "server.js"]
```

- `docker build .` - to build a new custom image based on the Dockerfile.

- `docker run -p local_port:exposed_port container_id` - to run a container and expose specific port.

- To build an image `docker build -t app-tag .` or to specify Dockerfile location `docker build -f docker_file -t app-tag`.

## Django Docker Set-up (vide CS50)

- First step is to create a Dockerfile which we’ll name Dockerfile. Inside this file, we’ll provide instructions for how to create a Docker Image which describes the libraries and binaries we wish to include in our container. Here’s an example of what our Dockerfile might look like:

```docker
FROM python:3
COPY .  /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
```

- `FROM python:3` this shows that we are basing this image off of a standard image in which Python 3 is installed. This is fairly common when writing a Docker File, as it allows you to avoid the work of re-defining the same basic setup with each new image
- `COPY . /usr/src/app`: This shows that we wish to copy everything from our current directory (.) and store it in the /usr/src/app directory in our new container.
- `WORKDIR /usr/src/app`: This sets up where we will run commands within the container. (A bit like cd on the terminal)
- `RUN pip install -r requirements.txt`: In this line, assuming you’ve included all of your requirements to a file called requirements.txt, they will all be installed within the container.
- 'CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]': Finally, we specify the command that should be run when we start up the container.

- To run a separate server for our database, we can simply add another Docker container, and run them together using a feature called Docker Compose. This will allow two different servers to run in separate containers, but also be able to communicate with one another. To specify this, we’ll use a YAML file called docker-compose.yml:

```YAML
version: '3'

services:
    db:
        image: postgres

    web:
        build: .
        volumes:
            - .:/usr/src/app
        ports:
            - "8000:8000"
```

- Specify that we’re using version 3 of Docker Compose
- Outline two services:

  - `db` sets up our database container based on an image already written by Postgres.
  - `web` sets up our server’s container by instructing Docker to:
    - Use the Dockerfile within the current directory.
    - Use the specified path within the container.
    - Link port 8000 within the container to port 8000 on our computer.

- Now, we’re ready to start up our services with the command `docker-compose up`. This will launch both of our servers inside of new Docker containers.

- At this point, we may want to run commands within our Docker container to add database entries or run tests. To do this, we’ll first run `docker ps` to show all of the docker containers that are running. Then, well find the **CONTAINER ID** of the container we wish to enter and run `docker exec -it CONTAINER_ID bash -l`. This will move you inside the _usr/src/app_ directory we set up within our container. We can run any commands we wish inside that container and then exit by running **CTRL-D**.
