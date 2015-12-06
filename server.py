from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

#restrict to particular path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

#Create server
server =  SimpleXMLRPCServer(("localhost", 9000))
print ("listening on port 9000...")


#register new function
def addnums_function(x,y):
    return x+y
server.register_function(addnums_function, 'add')

#run main server loop
server.serve_forever()