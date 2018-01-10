from flask import Flask, redirect
from subprocess import call
import socket
import time

app = Flask(__name__)


@app.route('/')
def login():
    return '<form method="POST">' \
           '<input name="text">' \
           '<input type="submit">' \
           '</form>'


@app.route('/<name>')
def create_training(name):
    port = get_free_tcp_port()
    call("docker run -d -p %d:9000 -p %d:4040 --name=%s training" % (port, port+1, name), shell=True)
    time.sleep(7)
    return redirect("http://vmiaavm11.iil.intel.com:%d" % port, code=302)


def get_free_tcp_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('', 0))
    addr, port = tcp.getsockname()
    tcp.close()
    return port


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
