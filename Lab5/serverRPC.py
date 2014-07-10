import SimpleXMLRPCServer
import os

def ls(dir):
	return os.listdir(dir)

if __name__ == '__main__':
		s = SimpleXMLRPCServer.SimpleXMLRPCServer(('127.0.0.1',1212))
		s.register_function(ls)
		s.serve_forever()
	

