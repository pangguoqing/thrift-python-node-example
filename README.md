#thrift-python-node-example

Quick and Dirty example of running interchangable Thrift node.js/python clients/servers.

I compiled the latest version of thrift from source (0.7.x) and used that to generate the thrift code.

I also used [node-thrift](https://github.com/wadey/node-thrift)

##Gotchas

There were some gotchas with getting everything setup, some of the code that is currently being generated for js:node is incorrect. 

By default, Thrift generates the following:

if (!arg.property)

This is actually incorrect and will cause problems hydrating the object.  Instead you should be using:

if (null != arg.property)

There were also some issues with python and module importing, but I think those are probably just me being moronic.  I was able to get around this by using sys.path.append in a few select files.

The last thing I had an issue with was making Python client work with Node.js server.  I missed the very clear NOTE: on wadey's README talking about having to use framed thrift transport, TFramedTransport.  That had me scratching my head, but I finally got it working.

##Results

I have both node.js/python servers working. Each of them will handle node.js/python client.  You can pick whatever you want for the server and whatever you want for the client.  I chose node.js server and python client as I have a project coming up soon that may use this combination.
