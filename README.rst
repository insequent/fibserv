=======
fibserv
=======

This is an example of a Fibonacci web service, utilizing swappable back-end
web engines allowing flexibility in implementation.

To run, simply run ``./api.py`` or alternatively ``deploy/run``. The program
defaults to port 8888 and only accepts POSTS. To access, you can run:

::
    curl localhost:8888 -d "5"

And assuming all is well, you'll receive the following in response:

::
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 15
    Server: Werkzeug/0.9.6 Python/3.4.1
    Date: Mon, 16 Mar 2015 03:22:19 GMT 

    [0, 1, 1, 2, 3]

Content Directory
=================

Here you'll find all the modules that generate content for responses

Engines Directory
=================

All web engines are stored here. Currently, the frameworks included
are Flask, Tornado, and Twisted. However, Twisted currently does not
have the ability to run on Python 3, so is merely included in case:

1. Twisted catches up and publishes a Python 3 module
2. Someone wishes to run a Python 2 version of fibserv
