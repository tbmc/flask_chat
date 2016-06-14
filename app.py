from flask import Flask
from flask_socketio import SocketIO

from main import main
from chat import socketio as chat

DEBUG = True


if __name__ == '__main__':
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'ifjrgdoiuertjiofgjohipijgtoijk'
    socketio = SocketIO(app)

    app.register_blueprint(main)
    app.register_blueprint(chat)

    socketio.run(app, debug=DEBUG)



