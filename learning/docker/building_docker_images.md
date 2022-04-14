## Dockerfile
- is a small program to create and image
- to run file: `docker built -t name_of_result . `
    - -t - tag accesting a name for the image which is `name_of_result`
    - . - stands for directory where to find dockerfile to execute. we can set directory, if it's not in current directory

Options for Dockerfile
- FROM: which image to download from; must be the first command in Dockerfile
- MAINTAINER: defines the autor of this Dockerfile # not recomended
- RUN
- ADD: copies a file into the image but supports tar and remote URL
- ENV: sets env vars; both during the build and when running the result
- VOLUME: creates aa mount point as defined when the container is run
- ENTRYPOINT: the executable runs when a container is run
- Expose: documents the ports that should be published
- CMD: provides arguments for the entrypoint (only one is allowed)
- ONBUILD
- RUN: runs a new command in a new layer
- WORKDIR: defines the working directory of the container 

ENTRYPOINT is constant
CMD we can change parameters
```Dockerfile
FROM ubuntu
LABEL
RUN
```
```docker
# Builds from Dockerfile in current directory
docker build .
# . stands for location to build docker image from. which means all the data in this dorectory will be included in our dockerimage
```

Commands:
- docker inspect: shows image details
- docker history: shows history of execution while creating image of Dockerfile



After building image from Dockerfile it's saved into memory, and if we gonna perform another build of same content as in this Dockerfile, the image will use cached data from previous build, which means build will be faster

To disable build from cached data use `--no-cache-true`


## Questions:
### What characterizes a golden image? - It replaces a canonical build with a locally-modified revision.
