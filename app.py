from flask_socketio import SocketIO
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template
import math
import random
import threading

datam1={
    "x":0,
    "y":0
}

def sanal_data(data):
    data["x"]=data["x"]+1
    data["y"]=math.sin(data["x"])



app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

socketio = SocketIO(app)

def thread1(data):
    threading.Timer(0.1,thread1,[data]).start()
    sanal_data(data)
    socketio.emit('server_data', data)
    
thread1(datam1)


@app.route('/')#decorator
def sessions():
    #flask server calistiginda server adresinde bu sayfa acilir
    return render_template('index.html')



if __name__ == '__main__':
    WSGIServer(('127.0.0.1', 5000), app, handler_class=WebSocketHandler).serve_forever()