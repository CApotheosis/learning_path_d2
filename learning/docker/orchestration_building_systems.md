# Registries in detail
```
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```
## Saving and loading docker images:
- docker save
- docker load
```
# Backing up docker images
docker save -o my-images.tar.gz debian:sid busybox ubuntu:14.04
# loads 
docker load -i my0images.tar.gz
```


# Questions
- Which orchestration option would be best for single machine coordination? - **Docker Compose**: 
Docker Compose is designed for projects that have more than one container, but not for serving on a large scale.