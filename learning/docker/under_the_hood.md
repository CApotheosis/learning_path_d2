# Docker the program

# Networking and Namespacing
- Ethernet: moves frames on a woire
- IP layer: moves pacjets on a local networl
- rounting: forwards packets between networks
- ports: adress particular programs on a computer

```
# --net=host - grants access to all ports on host machine
docker run -ti --rm --net=host --privileged=true ubuntu bash
apt-get update
apt-get install iptables
iptables -n -L -t nat # list all networks

# Creating another container with port
docker run -ti --rm -p 8080:8080 ubuntu bash

# Run iptables command to list networks on container with privileges
iptables -n -L -t nat
```
# Processes and cgroups
```
# create a container with name
docker run -ti --rm --name hello ubuntu bash
# get access to PID of the container
docker inspect --format '{{.State.Pid}}' hello
# return PID of the hello container

# create container with priviliges
docker run -ti --rm --priviliged=true --pid=host ubuntu bash
kill PID
```
# Storage
```docker
# create a basic ubuntu docker image
docker run -ti --rm --priviliged=true ubuntu bash
mkdir example
mkdir work | cd work
touch

mount -o bind other-work/ work/
ls -R
```
## Questions
- Which Linux kernel feature is essential for container process isolation? - cgroups
- Docker images are _____. - **read only**
- Which feature of Docker is used to contain networks? - **namespaces**
- How do packets get into and out of networks? - **through routing:** Routing forwards packets between networks, and is how packets get into and out of networks.
- If you mount a file so it bind mounts that file onto a position in the filesystem, and then you mount a folder on top of it with the same name, where will the file be? - **beneath the folder, you will see the folder instead**
- What do you need to configure on a Docker container to run a Docker client within? - **Mount the Docker socket of the host into the container.**
- Docker uses _____ and _____ to create virtual Ethernet networks. - **bridges; NAT**




