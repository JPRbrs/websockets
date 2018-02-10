from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit
# from codenames import game

app = Flask(__name__)
socketio = SocketIO(app)
ARBITRARY_NUMBER = 15


@app.route('/')
def index():
    """Serve the index HTML"""
    return render_template('index.html')


@socketio.on('create')
def on_create(data):
    """Create a game lobby"""
    room = ARBITRARY_NUMBER
    join_room(room)
    emit('join_room', {'room': room})
    print ('Data received: size {}, teams {}, dictionary {}'.format(
        data['size'],
        data['teams'],
        data['dictionary']
    ))


if __name__ == '__main__':
    socketio.run(app, debug=True)
