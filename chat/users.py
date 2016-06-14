from flask import Blueprint
from flask import render_template
import json

users = Blueprint("users", __name__)


@users.route("/users")
def users():
    pass

def list_users():
    return json.dump(["user1", "user2"])
