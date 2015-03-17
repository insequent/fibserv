=======
fibserv
=======

This is an example web service, that accepts a number and returns with that
number of elements in a Fibonacci sequence, starting with 0.  It utilizes a
swappable web engine back-end allowing flexibility in implementation.

To run, simply run ``./deploy/run`` from the repo. The program defaults to
port 8888, the Tornado engine, and only accepts POSTs. To access it, you can
simply run:

::

    curl localhost:8888 -d "5"

And assuming all is well, you'll receive the following in response:

::

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 15
    Server: TornadoServer/3.2.1
    Date: Mon, 16 Mar 2015 03:22:19 GMT 

    [0, 1, 1, 2, 3]


File Layout
===========

Content Directory
-----------------

Here you'll find all the modules that generate content for responses.

Engines Directory
-----------------

All web engines are stored here. To create an engine, the module must
simply have a function or class named ``main`` that can take 2 positional
parameters:

1. ``port``: Port number (string)
2. ``process_request``: The function by which content is generated (function)

``process_request`` takes ``body`` as a keyword argument, which should
be the body of the request.

Currently, the frameworks created are Flask, Tornado, and Twisted. However,
Twisted currently does not have the ability to run on Python 3, and the engine
is only included on the off-chance that one of the following becomes true:

- Twisted catches up and publishes a Python 3 module
- Someone wishes to run a Python 2 version of fibserv
