import os
import re

from flask import Blueprint
from flask import flash, request, redirect
from flask import render_template, session

main = Blueprint("main_blueprint", __name__)


def get_themes():
    default = "default.css"
    path = os.path.dirname(os.path.realpath(__file__))
    directory = os.listdir(path + "/../static/themes")
    directory.remove(default)
    directory.insert(0, default)

    exp = re.compile(r"\.css$|\.min.css")
    out = [[exp.sub("", e), e] for e in directory]
    return out


@main.route('/')
def index():
    if "connected" in session and session["connected"]:
        themes = get_themes()
        return render_template("index.html", pseudo=session['pseudo'], themes=themes)
    else:
        return render_template("login.html")


@main.route("/login", methods=["POST"])
def login():
    b = False
    if request.method == "POST":
        p = request.form["pseudo"]
        if p:
            session['connected'] = True
            session['pseudo'] = p
            b = True

    if b:
        return redirect("/", 303)
    else:
        flash(u'Il y a une erreur avec le pseudo')
        return render_template("login.html")


@main.route("/logout")
def logout():
    session["connected"] = False
    session["pseudo"] = None
    return redirect("/", 303)
