from flask import Flask, render_template, request, json
from flask_socketio import SocketIO, emit
from flask.ext.cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'justasecretkeythatihavetochange'
socketio = SocketIO(app)

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    query = dict(request.args)
    socketio.emit('log', { 'data': str(query) }, broadcast=True)
    return 'received'

@socketio.on('connect')
def on_connect():
    payload = {'data': 'connected'}
    emit('log', payload, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
