from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit
import serial
from time import sleep

print("Starting app...")

app = Flask(__name__)
app.debug = True
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
    print('Data received: size {}, teams {}, dictionary {}'.format(
        data['size'],
        data['teams'],
        data['dictionary']
    ))
    move_car()


def move_car():
    """Move car"""
    ser = serial.Serial('/dev/ttyACM1', 9600)
    sent_bytes = ser.write('1'.encode('utf-8'))
    sleep(2)
    print(sent_bytes)
    ser.close()


@app.route('/move')
def move():
    move_car()
    return render_template('move.html')


if __name__ == '__main__':
    socketio.run(app, debug=True)
