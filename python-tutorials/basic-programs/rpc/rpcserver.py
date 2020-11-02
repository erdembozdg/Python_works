
import pickle
from multiprocessing.connection import Listener
from threading import Thread

class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_functions(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, conn):
        try:
            while True:
                func_name, args, kwargs = pickle.loads(conn.recv())
                try:
                    r = self._functions[func_name](args, kwargs)
                    conn.send(pickle.dumps(r))
                except Exception as e:
                    conn.send(pickle.dumps(e))
        except EOFError:
            pass


def rpc_server(handler, address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        client = serv.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()

def add(x, y):
    return x + y
def sub(x, y):
    return x - y

if __name__ == '__main__':
    handler = RPCHandler()
    handler.register_functions(add)
    handler.register_functions(sub)
    rpc_server(handler, ('localhost', 17000), authkey=b'erdem')
