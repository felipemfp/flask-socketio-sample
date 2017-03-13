from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'justasecretkeythatishouldputhere'

socketio = SocketIO(app)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api')
def api():
    query = dict(request.args)
    socketio.emit('log', dict(data=str(query)), broadcast=True)
    return jsonify(dict(success=True, message='Received'))


@socketio.on('connect')
def on_connect():
    payload = dict(data='Connected')
    emit('log', payload, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
