from functools import wraps
from flask import g, request, redirect, url_for, session, render_template

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("uuid") is None:
            return render_template('login.html')
        return f(*args, **kwargs)
    return decorated_function