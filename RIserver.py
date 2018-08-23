from xmlrpc.server import SimpleXMLRPCServer
#RPC - Remote Procedure Call
#Utiliza XML para fazer o encode e HTTP como mecanismo de transporte
from xmlrpc.server import SimpleXMLRPCRequestHandler
#Manipulador de Requests/Pedidos

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
#Classe para tratar o request do cliente

with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    def adder_function(x, y):
        print("Soma: ", x+y)
        return x + y
    server.register_function(adder_function, 'add')
    server.serve_forever()
