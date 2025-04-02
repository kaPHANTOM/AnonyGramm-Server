import os
from flask import Flask, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio.run(app, host='0.0.0.0', port=port, allow_unsafe_werkzeug=True)

users = {}

@app.route('/login')
def login():
    temp_id = os.urandom(8).hex()
    search_code = os.urandom(4).hex()
    users[temp_id] = {'online': True, 'search_code': search_code}
    return jsonify({'temp_id': temp_id, 'search_code': search_code})

@app.route('/status', methods=['POST'])
def status():
    return jsonify({'online': True})

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
