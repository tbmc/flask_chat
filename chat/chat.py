from flask_socketio import emit
from flask import session


ns = "/chat"


def set_all_socket(socketio):
    @socketio.on("new_user")
    def joined(data={}):
        print(data)
        emit("new_user", {
            "pseudo": session["pseudo"]
        }, broadcast=True)

    @socketio.on("message")
    def new_message(message={}):
        print(message, type(message))
        emit("message", {
            "pseudo": session["pseudo"],
            "message": message["message"]
        }, broadcast=True)





