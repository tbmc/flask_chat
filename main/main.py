from flask import Blueprint
from flask import render_template, send_from_directory
from os.path import join

from . import main

@main.errorhandler(404)
@main.errorhandler(401)
@main.errorhandler(500)
def error404(error):
    return "Erreur {}".format(error.code), error.code


# Inutile pour la production, mais pratique pour le debug
@main.route('/static/<path>/<filename>')
def send_static(path, filename):
    return send_from_directory(join('static', path), filename)

