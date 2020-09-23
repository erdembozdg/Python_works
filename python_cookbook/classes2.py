
class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    def read(self):
        return self._state.read(self)
    
    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)

class ConnectionState:

    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()   

class ClosedConnectionState(ConnectionState):

    @staticmethod
    def read(conn):
        raise RuntimeError('Not Open')
    
    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not Open')

    @staticmethod
    def open(conn):
        return conn.new_state(OpenConnectionState) 

    @staticmethod
    def close(conn):
        raise NotImplementedError() 

class OpenConnectionState(ConnectionState):

    def read(conn):
        print("reading")
    
    def write(conn, data):
        print("writing")

    def open(conn):
        raise RuntimeError('Already Open')

    def close(conn):
        return conn.new_state(ClosedConnectionState)

print("----------------")
# Inheritance
class Connection2:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, newstate):
        self.__class__ = newstate

    def read(self):
        raise NotImplementedError()
    
    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

class ClosedConnection(Connection2):

    def read(conn):
        raise RuntimeError('Not Open')
    
    def write(conn, data):
        raise RuntimeError('Not Open')

    def open(conn):
        return conn.new_state(OpenConnection) 

    def close(conn):
        raise NotImplementedError() 

class OpenConnection(Connection2):

    def read(conn):
        print("reading")
    
    def write(conn, data):
        print("writing")

    def open(conn):
        raise RuntimeError('Already Open')

    def close(conn):
        return conn.new_state(ClosedConnection)

c = Connection()
c._state
c.open()
c.read()

c = Connection2()
c.open()
c.read()



