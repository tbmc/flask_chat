from flask_socketio import emit

from . import socketio



@socketio.on("new_message")
def new_message(msg):
    pass

@socketio.route("/chat")
def chat():
    pass
