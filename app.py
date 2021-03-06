from flask import Flask
from flask_socketio import SocketIO
from flask_socketio import emit
from flask import send_from_directory
from os.path import join
from flask import session

from main.main import main
from chat.chat import set_all_socket

from db.db import db_session


DEBUG = True

app = Flask(__name__)
app.config["SECRET_KEY"] = 'ifjrgdoiuertjiofgjohipijgtoijk'
socketio = SocketIO()
app.register_blueprint(main)
socketio.init_app(app)

set_all_socket(socketio)


@app.errorhandler(401)
@app.errorhandler(500)
@app.errorhandler(404)
def error404(error):
    return "Erreur {}".format(error.code), error.code


# Inutile pour la production, mais pratique pour le debug
@app.route('/static/<path>/<filename>')
def send_static(path, filename):
    return send_from_directory(join('static', path), filename)

"""
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
"""

if __name__ == '__main__':
    socketio.run(app, debug=DEBUG)

