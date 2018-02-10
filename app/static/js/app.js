var manager = require('nipplejs').create(options);

var socket = io.connect('http://' + document.domain + ':' + location.port);
// verify our websocket connection is established
socket.on('connect', function() {
    console.log('Websocket connected!');
});
// message handler for the 'join_room' channel
socket.on('join_room', function(msg) {
    console.log(msg);
});
// createGame onclick - emit a message on the 'create' channel to 
// create a new game with default parameters
function createGame() {
  console.log('Creating game...');
  socket.emit('create', {size: 'normal', teams: 2, dictionary: 'Simple'});
}

var joystick = nipplejs.create({
    zone: document.getElementById('static'),
    mode: 'static',
    position: {left: '50%', top: '50%'},
    color: 'red'
});

