from flask import render_template, session
from flask import flash, request, redirect

from . import main

@main.route('/')
def index():
    if "pseudo" in session:
        return render_template("index.html", pseudo = session['pseudo'])
    else:
        return render_template("login.html")

@main.route("/login", methods=["POST"])
def login():
    b = False
    if request.method == "POST":
        p = request.form["pseudo"]
        if p:

            session['pseudo'] = p
            b = True

    if b:
        return redirect("/", 200)
    else:
        flash(u'Il y a une erreur avec le pseudo')
        return render_template("login.html")

