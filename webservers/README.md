# Node

# Python

### Web Server Gateway Interface (WSGI)

* Universal interface between web servers and web frameworks
* Two sides. The 'server/gateway' side and the 'application/framework'
* Accordion style middleware between the two sides

### chaussette

* A WSGI server.
* Can bind a socket to (1) a new port or (2) and already open socket
* Good for socket managers

### cherrypy

* A server and HTTP framework
* Can work in WSGI environments
* Very fast to get something up and running
* Designed to be very pythonic

### Gunicorn

* A WSGI framework for UNIX
* Uses the 'pre-fork worker model'
  * 'pre-for worker model' is how servers handle dealing with multiple clients. It creates a copy of itself to handle the request, to prevent blocking
* Inspired by Unicorn

### Rocket

* WSGI, pure-python  
* Compatible with cPython and Jython

### Spawning

* WSGI
* Nonblocking I/O, using eventlet
* Graceful reload

# Ruby

### Rack

* Primary webserver interface for Ruby ecosystem
* Simple API. Takes in the server application and calls it when port is hit
* Inspired by WSGI

### Puma

* Built for speed and parallelism
* Uses Rack

### Passenger

### Unicorn

* Designed for fast clients
* For Rack
* Load balancing done by OS kernel

### WEBrick

* Super simple

### Thin

# Node

### HTTP Module
