## Docker commands:
- docker images: lists installed images
- docker run -ti ubuntu:latest bash
    - -ti (terminal interactive) - we will have terminal within the image.
    - ubuntu - image name
    - latest - image tag
    - to run bash shell
- exit - ti exit running image shell or ctrl+d
- docker ps --format $FORMAT - shows running images
    - --format $FORMAT - formats to print vertically

An image is every file that makes up just enough of the operating system to do what you need to do.