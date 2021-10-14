
from flask_socketio import SocketIO
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template
import math




app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

socketio = SocketIO(app)

@app.route('/')#decorator
def sessions():
    #flask server calistiginda server adresinde bu sayfa acilir
    return render_template('index.html')


if __name__ == '__main__':
    WSGIServer(('127.0.0.1', 5000), app, handler_class=WebSocketHandler).serve_forever()