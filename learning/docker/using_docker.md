## Docker commands:
- `docker images: lists installed images`
- `docker run -ti ubuntu:latest bash`
    - -ti (terminal interactive) - we will have terminal within the image.
    - ubuntu - image name
    - latest - image tag
    - bash - to run bash shell
- exit - to exit running image shell or ctrl+d
- `docker ps --format $FORMAT`:  shows running images
    - --format $FORMAT - formats to print vertically
- `docker ps -l`: shows last exited container


## Word definitions:
- ### Images – Images are the collection of file system, configuration, application and other components needed to run a container. Images are used to create containers. They have a base OS and any binaries or applications contained in it.  Images are SAVED copies of a container. A list of saved containers can be seen using the docker images command.
- ### Container – A running image. Running instances of Docker images — containers run the actual applications. A container includes an application and all of its dependencies. It shares the kernel with other containers, and runs as an isolated process in user space on the host OS. A list of running containers can be seen using the docker ps command.
- ### Nesting – Running a container based on an image making changes and saving as another image.  Any number of containers can be nested.  As an example, if I create  a new container running Ubuntu 16, add an app and save it I have a new nested image with the app that runs on Ubuntu 16.  The app container does not have the bits in it for Ubuntu 16, it only has the changes that were made from the base image to add the app.  This process can be repeated any number of times.
- ### Docker daemon (or engine) – The background service running on the host that manages building, running and distributing Docker containers.
- ### Docker client – The command line tool that allows the user to interact with the Docker daemon.
- ### Docker Hub (repository) – A registry of Docker images. You can think of the registry as a directory of all available Docker images.
- ### Dockerfile: Configuration file used to automate the image creation process to a Docker container

### To create new container from one container with its changes:
- docker commit container_id_to_copy_from: returns sha256 value
- docker tag sha256 new_image_name
### Another way of doing it:
- docker commit image_name new_image_name_to_copy

`docker run`
- containers have a main process
- the containers stops when hat process stops
- containers have names

`docker run`:
- --rm -ti ubuntu sleep 5: --rm - deletes container after use
- -ti ubuntu bash -c "sleep 3, echo all done": bash proces to do sequence of things
- -d -ti ubuntu bash: -d (detach) - runs on background
### Access to container running in background: 
- `docker attach name_of_the_container`: runs container by name;
### Key sequence to detach and keep running container:
- ctrl + p, ctrl + q


`docker exec`
- start another process in an existing container
- great for debugging and DB administration
- can't add ports, volumes, and so on
- if we quit base process, the other process will exit too
### Commands:
- -ti name_of_the_container bash

docker logs:
- Keep the output of the containers
- view log of a container: docker logs container_name
- don't let the output get too large

docker run --name example -d ubuntu bash -c "lose /etc/password" # there is a typo 

## Stopping and removing containers
- docker kill container_name: kills the process
- docker rm container_name: removes the container

## Resource contraints
- ### Memoruy limits
    - docker run --memory maximum-allowed-memory image-name command
- ### CPU limits
    - docker run --cpu-shares: cotainer gets access to cpu usage, if any other process is accessing cpu, they will share equally and so forth as number rises. relative to other containers
    - docker run --cpu-quota: to limit in general

## Lessons from the field!
- don't let your containers fetch dependencies when they start 
- don't leave important things in unnamed stopped containers



# Container Networking 
- Programs in containers are isolated from the internet by default
- You can group your containers into "private" networks
- You explicitly choose who can connect to whom

## Exposing a specific port
- explicit specifies the port inside the container and outside
- exposes as many ports as you want
- requires coordinating between containers
- makes it easy to find the exposed ports


### `docker run --rm -ti -p 45678:45678 -p 45679:45679 --name echo-server ubuntu:14:04 bash`
- -p 45678:45678: port one to be exposed, first port value is local port, second is public
- -p 45679:45679L port two to be exposed

`nc -lp 45678 | nc -lp 45679` - connects two ports for sending and recieving data. Computer with port 45678 sends data and it can be accessed with another computer listening port 45679 

### Dynamic port exposing
- `docker run --rm -ti -p 45678 -p 45679 --name echo-server ubuntu:14:04 bash`
- `docker port container_name`: returns external ports connected to internal
- `nc localhost external_port` 

### To listen to this port we can use nc on linux: `nc localhost port_to_listen_to`
### On Windows and Mac - create two containers: 
- `docker run --rm -ti ubuntu:14.04 bash`
- `nc host.docker.internal host_to_listen_from` - mac
- `nc ip_address host_to_listen_from` - windows

### Exposing ports dynamically
- the port inside the container is fixed
- the port on the host is chosen from unused ports
- this allows many containers running programs with fixed ports 
- this often is used with a service discovery program



### Exposing UDP
- `docker run --rm -ti -p 45678/udp --name echo-server ubuntu:14.04 bash`
- `nc -ulp 45678`
### To connect to the running network
- `nc -u localhost` - dynamicly assigned port
<br><br/>

## Connecting multiple networks
- `docker network ls` - lists networks
- `docker network create network_name`: creates network
- `docker run --rm -ti --net network_name --name catserver ubuntu:14.04 bash`: creates container and binds it into given network 
- `docker run --rm -ti --net learning --name dogserver ubuntu:14.04 bash`: creates another container and binds it into the same network

### We will create new network in this network only for cats
- `docker network create catsonly`
- `docker network connect catsonly catserver`
- `docker run --rm -ti --net catsonly --name bobcatserver ubuntu:14.04 bash`

<br><br/>
Now we have connected catserver and bobcatserver into the same network and thus they can send data to each connect to each other within this server and no other connection is allowed.
<br><br/>

## Legacy Linking - not recommended
- links all ports, though only one way
- secret env vars are shared only one way 
- depends on startup order
- restarts only sometimes break the links
`docker run --rm -ti -e SECRET=theinternetlovescats --name catserver ubuntu bash`
`docker run --rm -ti --link catserver --name dogserver ubuntu bash`
`nc -lp 1234`
`nc cataserver 1234`

### To remove image: `docker rmi image_name:tag or image_id`
In onrder to remove image, we need to delete all reference containers of this image.


# Volumes - shared folders
- virtula "discs" to store and share data 
- two main varieties
    - persistent: remains even after usage
    - ephermeral: doesn't use volume if it's not being accessed
- not part of images: this means are present only in my machine


## Sharing a folder with a host
`docker run -ti -v full_path_to_shared_folder:/folder_where_shared_data_is_stored ubutu bash`
- -v for volume
- full path for shared folder
- where on container shared folder are stored

Run command: `touch folder_where_shared_data_is_stored/file_name` - will create file within container and on host machine

### Note: file must exist before container is started or it will be assumed to be a directory

## Sharing data between containers
- volumes-from
- shared "discs" that exist only as longs as they are being used
- can be shared between containers

```docker
# Create a container with shared data
docker run -it -v /shared-data share_1 ubuntu bash

echo hello > shared-data/data-file # this will create a file 

# Create another container which has the shared data stored on container share_1
docker run -it --volumes-from share_1 --name share_2 ubuntu bash

echo more > shared-data/more-data # this will create a file 
```
### We can create as much connected containers with volume as we want, but the data will persist untill the container is alive. When container all containers are stopped - the data will be gone. 

# Docker Registries - peace of software 
- Registries manage and distribute images
- docker (the company) offers these for free
- you can run your own, as well

```dcoker
docker login
docker pull debian:sid # getting debian image into my local machine
docker tag debian:sid usernmae/image_name 
docker push username/image_name_to_push
```

# Questions
### If a network preference is not specified, on which network will the container be placed, by default? - bridge




