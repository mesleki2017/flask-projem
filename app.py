from flask_socketio import SocketIO
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template
import math
import threading

sanal_data={
    "x":0,
    "y":0
}



app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

socketio = SocketIO(app)

def thread1():
    threading.Timer(0.5,thread1).start()
    sanal_data["x"]=sanal_data["x"]+1
    sanal_data["y"]=math.sin(sanal_data["x"])
    socketio.emit('server_data', sanal_data)

thread1()

@app.route('/')#decorator
def sessions():
    #flask server calistiginda server adresinde bu sayfa acilir
    return render_template('index.html')



if __name__ == '__main__':
    WSGIServer(('127.0.0.1', 5000), app, handler_class=WebSocketHandler).serve_forever()