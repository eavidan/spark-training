from flask import Flask, redirect, request
import socket
import time
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def login():
    return '<h2>Give you workspace a unique name please (no spaces):</h2>' \
           '<form method="POST" action="start">' \
           '<input name="name">' \
           '<input type="submit">' \
           '</form>'


@app.route('/list')
def list():
    lst = []
    for container in client.containers.list():
        lst.append((container.attrs['Name'], container.attrs['Config']['Labels']))
    tbl = ''
    for x in lst:
        tbl += "<tr><td>%s</td><td>%s</td></tr>" % (x[0], x[1])
    return "<h2>Environments:</h2><table><tr><th>Name</th><th>link</th</tr>%s</table>" % tbl


@app.route('/start', methods=['POST'])
def create_training():
    name = request.form['name']
    if len(name) <= 3:
        return 'Seriously?!'
    port = get_free_tcp_port()
    ports = {'9000/tcp': port, '4040/tcp': port+1}
    link = "http://vmiaavm11.iil.intel.com:%d" % port
    client.containers.run('training', name=name, detach=True, ports=ports, labels=[link])
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