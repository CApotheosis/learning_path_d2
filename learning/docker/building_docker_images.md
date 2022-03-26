## Dockerfile
- is a small program to create and image
- to run file: `docker built -t name_of_result . `
    - -t - tag accesting a name for the image which is `name_of_result`
    - . - stands for directory where to find dockerfile to execute. we can set directory, if it's not in current directory

Options for Dockerfile
- FROM
    - which image to download from 
    - must be the first command in Dockerfile
- MAINTAINER
    - defines the autor of this Dockerfile
- RUN
    - run a command, wait to finish, and save the result  
- ADD
    - Adds local files
    - adds the contents of tar archives
    - works with URLS 
        ADD adddres /file_to_store/
- ENV
    - sets env vars
    - both during the build and when running the result
- ENTRYPOINT
    - specifies the start of the commands to run
- CMD

