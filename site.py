from flask import Flask, redirect, request
from subprocess import call, check_output
import socket
import time

app = Flask(__name__)


@app.route('/')
def login():
    return '<h2>Give you workspace a unique name please (no spaces):</h2>' \
           '<form method="POST" action="start">' \
           '<input name="name">' \
           '<input type="submit">' \
           '</form>'


@app.route('/list')
def list():
    out = check_output('docker ps --format "<tr><td>{{.Names}}</td><td><a href=\"{{.Labels}}\">{{.Labels}}</a></td></tr>"', shell=True)
    return "<h2>Environments:</h2><table><tr><th>Name</th><th>link</th</tr>%s</table>" % out


@app.route('/start', methods=['POST'])
def create_training():
    name = request.form['name']
    if len(name) <= 3:
        return 'Seriously?!'
    port = get_free_tcp_port()
    call("docker run -d -p %d:9000 -p %d:4040 --label=%s:%d --name=%s training" % (port, port+1, 'http://vmiaavm11.iil.intel.com', port, name), shell=True)
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