# Containers

## Virtual Machines vs Containers

* Virtual Machines:
  * Mimics a complete server. Has libraries, drivers, the OS, and the application
  * Run on a hypervisor, which runs on the host OS
  * A lot of duplication between the guest VMs caused by running the same binaries, wasting server resources
* Containers:
  * Virtual instances share a single host OS system, libraries, drivers, and binaries
  * More memory efficient than VM
  * Operating System-Level Virtualization
  * Function of hypervisor is handled by the container engine (i.e. Docker)
  * Built in layers of images.
    * An image is a lightweight package that includes the code, runtime, libraries, environment variables, and config files
    * Container is an instance of an image

## Docker

### Containers

* `Dockerfiles`:
  * Specifies the image.
  * Defines what happens inside of the container
  * Exposes network ports
  * Defines environment variables
* `docker run [image]`: Creates a container from an instance
* `docker build [path]`: Creates an images from a Dockerfile
* `docker images`
* `docker ps`
* `docker stop [container id]`
* `docker rmi [image]`
* Pushing to registry
  * `docker login`
  * `docker tag <image> username/repository:tag`
  * `docker push [image] username/repository:tag`
  * Defaults to Docker Registry

### Services

* "A container in production"
* Codifies the way an image is run, in `docker-compose.yml`
  * (i.e. Which ports it uses, Number of replicas on the container to run, etc)
* `docker stack ls`
* `docker stack deploy -c [compose-file] [app name]`
* `docker stack rm [app_name]`
* `docker ps [app_name]`
* A swarm is a group multi-container of services being run on multiple machines
  * Also used to refer to the group of machines running Docker
* A swarm manager is used to control the swarm
  * Strategies for running the containers within the swarm is specified the Compose file
  * Only swarm managers can execute commands and authorize other machines to join swarm
  * Enabling swarm mode makes the current machine the swarm manager
  * Machines can be virtual or physical
  * `docker swarm init` -creates the swarm manager
  * `docker join`
* Any IP of a node is the swarm can be used to access the app because they all participate in a routing mesh (aka each node has a load balancer)
* `docker-machine create --driver [driver] [name]`
* `docker-machine ssh "cmd"`
* `docker-machine scp file [name]:[path]` - copy file
* `docker-machine stop [name]`
* `docker-machine rm [name]`

### Stack

* A group of interrelated services that share dependencies and are scaled together
