# Presentation Materials
[![Slides](https://www.google.com/url?sa=i&url=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3AGoogle_Slides_logo_(2014-2020).svg&psig=AOvVaw09xLw3wZzD_Yp0bvjOea3u&ust=1636119190863000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCOivi4zp_vMCFQAAAAAdAAAAABAD)][1]

[1]: ./Dockers.pdf


# Install Docker and Docker compose on your machine
- Install Docker: https://docs.docker.com/engine/install/
- Install Docker-compose: https://docs.docker.com/compose/install/

# Useful Notes:

- If you encountered this error
   >Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/images/json": dial unix /var/run/docker.sock: connect: permission denied

Just type: `sudo chmod 666 /var/run/docker.sock`

# Docker Commands Examples

1. run hello world: `docker run hello-world`
2. complex image: `docker run -it  danielkraic/asciiquarium`
3. get images: `docker iamges`
4. list containers: `docker ps`, `docker ps -a`, `docker container ls`
5. container runs and close: `docker run ubuntu`, `docker  run ubuntu echo hi`
6. check for it in the images: `docker iamges`
7. previously run containers:  `docker ps -a`
---
8. keep running: `docker run ubuntu sleep 5`
9.  run in interactive mode: `docker run -it ubuntu`
---
10. get a new image: `docker pull kodekloud/simple-webapp`
11. run the image: `docker run kodekloud/simple-webapp`
12. Hide logs(detached mode): `docker run -d kodekloud/simple-webapp`
13. check it: `docker ps`
14. attach the container to see logs(no logs?): `docker attach <ID>`
15. get the logs: `docker logs <ID>`
---
16. detach ubuntu: `docker run -d -it ubuntu`
17. exec ubuntu: `docker exec b2 echo hi`
---
18. inspect: `docker inspect <ID>`
19. remove the container: `docker rm <ID>`
---
20. map ports: `docker run  -p 80:8080 kodekloud/simple-webapp`
21. get networks: `docker network ls`
---
22. view build history of an image: `docker history kodekloud/simple-webapp`


