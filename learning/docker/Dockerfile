# FROM busybox
# RUN echo "building simple docker image."
# CMD echo "hello container."

# FROM debian:sid
# RUN apt-get -y update
# RUN apt-get -y install nano
# CMD ["bin/nano", "/tmp/notes"]

FROM example/nanoer
ADD notes.txt /notes.txt
CMD ["bin/nano", "/notes.txt"]
