from flask import render_template
from app import app

"""
This module is used to handle errors thrown at the page.
"""


@app.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(410)
def gone_error(error):
    return render_template('410.html'), 410


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500
