from flask import Flask, redirect, request, render_template
from subprocess import call, check_output
import socket
import time

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/list')
def list():
    out = check_output('docker ps --format "<tr><td>{{.Names}}</td><td><a href=\"{{.Labels}}\">{{.Labels}}</a></td></tr>"', shell=True)
    return "<h2>Environments:</h2><table><tr><th>Name</th><th>link</th</tr>%s</table>" % out


@app.route('/start', methods=['POST'])
def create_training():
    host = request.host.split(':')[0]
    print(host)
    name = request.form['name']
    if len(name) <= 3:
        return 'Seriously?!'
    port = get_free_tcp_port()
    call("docker run -d --cpu-period=100000 --cpu-quota=300000 -p %d:9000 -p %d:4040 --label=%s:%d --name=%s training" % (port, port+1, host, port, name), shell=True)
    time.sleep(15)
    return redirect("http://%s:%d" % (host, port), code=302)


def get_free_tcp_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('', 0))
    addr, port = tcp.getsockname()
    tcp.close()
    return port


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)