
from urllib import request, parse
import requests
from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler
from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing.connection import Listener
import traceback
import ipaddress
import hmac
import os

url = 'http://httpbin.org/get'

params = {
    'name1': 'value1',
    'name2': 'value2'
}

headers = {
    'User-agent': ''
}

resp = requests.post(url, data=params, headers=headers)
text = resp.text
print(text)

# u = request.urlopen(url, querystring.encode('ascii'))

# req = request.Request(url, querystring.encode('ascii'), headers=headers)
# u = request.urlopen(req)

querystring = parse.urlencode(params)
u = request.urlopen(url + '?' + querystring)
resp = u.read()
print(resp)

resp = requests.head('http://www.python.org/index.html')
print(resp)

# status = resp.status_code
# last_modified = resp.headers['last-modified']
# content_type = resp.headers['content-type']
# content_length = resp.headers['content-length']

resp = requests.get('http://pypi.python.org/pypi?:action=login',
auth=('user','password'))

resp2 = requests.get(url, cookies=resp.cookies)

# url = 'http://httpbin.org/post'
# files = { 'file': ('data.txt', open('data.txt', 'rb')) }
# r = requests.post(url, files=files)

print("----------------")
# TCP Handler
class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from ', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)

class EchoHandler2(StreamRequestHandler):
    def handle(self):
        print('Got connection from ', self.client_address)
        for line in self.rfile:
            self.wfile.write(line)

print("----------------")

def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')

def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()

print("----------------")

def client_auth(conn, secret_key):
    msg = conn.recv(32)
    hash = hmac.new(secret_key, msg)
    digest = hash.digest()
    conn.send(digest)

def server_auth(conn, secret_key):
    msg = os.urandom(32)
    conn.send(msg)
    hash = hmac.new(secret_key, msg)
    digest = hash.digest()
    resp = conn.recv(len(digest))
    return hmac.compare_digest(digest, resp)


secret_key = b'peekaboo'
def echo_handler(client):
    if not server_auth(client, secret_key):
        client.close()
        return
    while True:
        msg = client.recv(8192)
        if not msg:
            break
        client.sendall(msg)

def echo_server_secured(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        c,a = s.accept()
        echo_handler(c)

if __name__ == "__main__":
    # serv = TCPServer(('', 20000), EchoHandler2)
    # serv.serve_forever()

    # Create IPs from CIDR network adress
    net = ipaddress.ip_network('123.45.67.64/30')
    print('Num of IPs: ', net.num_addresses)
    print(ipaddress.ip_address('123.45.67.64') in net)
    for n in net:
        print(n)

    # echo_server(('', 25000), authkey=b'peekaboo')
    echo_server_secured(('', 18000))

