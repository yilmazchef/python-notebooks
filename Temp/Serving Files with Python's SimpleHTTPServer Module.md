### Introduction

Servers are computer software or hardware that processes requests and deliver data to a client over a network. Various types of servers exist, with the most common ones being web servers, database servers, application servers, and transaction servers.

Widely used web servers such as [Apache](https://www.apache.org/), [Monkey](http://monkey-project.com/), and [Jigsaw](https://jigsaw.w3.org/) are quite time-consuming to set up when testing out simple projects and a developer's focus is shifted from producing application logic to setting up a server.

Python's `SimpleHTTPServer` module is a useful and straightforward tool that developers can use for a number of use-cases, with the main one being that it is a quick way to serve files from a directory.

It eliminates the laborious process associated with installing and implementing the available cross-platform web servers.

**Note**: While `SimpleHTTPServer` is a great way to easily serve files from a directory, it shouldn't be used in a production environment. According to the official Python docs, it "only implements basic security checks."

### What is an HTTP Server

**HTTP** stands for _HyperText Transfer Protocol_. Let us think of a protocol as a spoken language like English. English has a set of rules and vocabulary. Thus, if we both understand the rules and vocabulary defining the English Language, then we can communicate in the language effectively.

Just like human beings, electronic devices too communicate with each other. They, therefore, need a 'set of rules and vocabulary' to actively pass and receive information from each other.

A protocol is a standard set of rules that facilitates successful communication between electronic devices. These sets of mutually accepted and implemented rules include the commands used to initiate the sending and reception of data, the data types to be transmitted between devices, how to detect errors in data, how successful data transfers are confirmed, and much more.

For example, when you perform a simple search using a browser, there were two essential systems involved - the _HTTP Client_ and _HTTP Server_.

The client, commonly referred to as the _browser_, can be an elaborate program such as Google Chrome, or Firefox, but it can also be as simple as a CLI application. The client sends your _request_ to the server, which the processes the HTTP requests and provides a _response_ to the client. In the case of browsers, the response is typically an HTML page.

### Python's _SimpleHTTPServer_ Module

When you need a quick web server running, setting up a production-level server is a massive overkill.

Python's `SimpleHTTPServer` module is a labor-saving tool that you can leverage for turning any directory in your system into an uncomplicated web server. It comes packaged with a simple HTTP server that delivers standard `GET` and `HEAD` request handlers.

With a built-in HTTP server, you are not required to install or configure anything to have your web server up and running.

**Note**: The Python `SimpleHTTPServer` module was merged into the `http.server` module in Python 3. Throughout this article we'll be using the Python 3 version, but if you're using Python 2 you can swap out `http.server` for `SimpleHTTPServer` and it should work in most cases.

### Command Line Usage

The simplest way to start up a web server that serves the directory in which the command is ran is to simply navigate to your project's directory using the terminal and run:

**Python 2**

```
$ python -m SimpleHTTPServer 8000
```

**Python 3**

```
$ python3 -m http.server 8000
```

By running this command, you'll be able to access the files in your directory through your browser at `localhost:8000`:

![application directory listing](https://stackabuse.s3.amazonaws.com/media/serving-files-with-pythons-simplehttpserver-module-1.png)

As you can see, the server provides a simple directory UI in which you can access any of the files. This is the simplest way to directly serve files locally over HTTP.

### Default Python Usage

For one reason or another, running this server via the command line might not suit our use-case. At times like this we can instead use the server directly in our code using the `SimpleHTTPRequestHandler` object. But first, we need to set it up with a socket server.

Beneath the HTTP protocol are _UDP_ (User Datagram Protocol) or _TCP_ (Transmission Control Protocol), which are transport protocols that handle the transportation of data from one network location to another. Since we're running an HTTP server, our application will use the TCP protocol, through a _TCP Socket Address_ which contains an IP address and a port number. This can be set up with Python's `socketserver.TCPServer`, which we've implemented below:

Check out our hands-on, practical guide to learning Git, with best-practices, industry-accepted standards, and included cheat sheet. Stop Googling Git commands and actually _learn_ it!

```
import http.server
import socketserver

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()
```

**Note**: The code will fail with the error `AttributeError: __exit__` for Python versions < 3.6. This is because in previous versions `socketserver.TCPServer` does not support use with [context managers](https://stackabuse.com/python-context-managers/) (the `with` keyword). In these cases you need to call `server_close()` to stop the server.

By default, the `SimpleHTTPRequestHandler` serves files from the current directory and related subdirectories. As the name suggests, it is a simple HTTP request handler. Being the simple server that it is, it only allows you to retrieve data and not post it to the server. And because of this, it only implements the HTTP `GET` and `HEAD` methods via `do_GET()` and `do_HEAD()`.

The parameters passed to the `TCPServer` represent the IP address and port number. By leaving the IP address empty, the server listens to all available IP addresses, while we've set the port to `8000`. This means that it would then be accessible on `localhost:8000`.

Finally, `httpd.server_forever()` starts the server, listens, and responds to incoming requests from the a client.

The server can be started by simply executing the file:

```
$ python3 simple-server.py
```

And just like with the command line usage, we can now access the directory through our web browser:

![application directory listing](https://stackabuse.s3.amazonaws.com/media/serving-files-with-pythons-simplehttpserver-module-1.png)

### Customizing Paths

Another approach we can take is to make a custom class that extends `SimpleHTTPRequestHandler` and handles our requests with some custom functionality. To do this, we implement our own `do_GET()` function.

But before we get to that, let's say we have an HTML file that we want to serve, `mywebpage.html`:

```
<!DOCTYPE html>
<html>
<head>
  <title>Using Python's SimpleHTTPServer Module</title>
  <style>
    #rectangle {
      height: 50px;
      width: 100px;
      background-color: #00f28f;
    }
  </style>
</head>
<body>
  <h2>Rectangle served by SimpleHTTPServer</h2>
  <div id="rectangle"></div>
</body>
</html>
```

In order to serve this HTML from a path that isn't `/mywebpage.html`, we can use our custom handler to serve it on any path we want. In this example we'll just serve it on the root path, `/`:

```
import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'mywebpage.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
```

Again, running this script will allow us to access it through the browser:

![rectangle served on the browser](https://stackabuse.s3.amazonaws.com/media/serving-files-with-pythons-simplehttpserver-module-2.png)

Though, there are a lot more customizations we can do with the response via the `self` reference, which we'll see in the next section.

### Returning Dynamic HTML

A common usage of web servers is to serve dynamically generated HTML. Although this is only as very simple server, it can perform this task as well. In addition to sending dynamic HTML, we can also set different status codes, headers, etc. In the following example we set some headers and return dynamic HTML that is generated using the query parameter `name`:

```
import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Sending an '200 OK' response
        self.send_response(200)

        # Setting the header
        self.send_header("Content-type", "text/html")

        # Whenever using 'send_header', you also have to call 'end_headers'
        self.end_headers()

        # Extract query param
        name = 'World'
        query_components = parse_qs(urlparse(self.path).query)
        if 'name' in query_components:
            name = query_components["name"][0]

        # Some custom HTML code, possibly generated by another function
        html = f"<html><head></head><body><h1>Hello {name}!</h1></body></html>"

        # Writing the HTML contents with UTF-8
        self.wfile.write(bytes(html, "utf8"))

        return

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
```

And running this code with the URL `http://localhost:8000?name=Billy` will yield:

![serving dynamic html](https://stackabuse.s3.amazonaws.com/media/serving-files-with-pythons-simplehttpserver-module-3.png)

Any value you set for the `name` query parameter will then show up on the screen! You can even omit the `name` query parameter and see what happens.

As you can see, creating a custom request handler allows us to manipulate the responses as much as we'd like by changing the implementation of the `do_GET` method and we don't have such control over our responses with the default implementation.

The same can be done with the HTTP HEAD method (via the `do_HEAD()` function), but since it is very similar to that of GET method we'll leave that as an exercise to the reader.

### Conclusion

Python provides us with the `SimpleHTTPServer` module (or `http.server` in Python 3) that can be used to quickly and easily serve files from a local directory via HTTP. This can be used for many development or other internal tasks, but is not meant for production.

This is a great solution for local use since web servers such as [Apache](https://www.apache.org/), [Monkey](http://monkey-project.com/), and [Jigsaw](https://jigsaw.w3.org/) are much more difficult to get set up and are often overkill for development activities.