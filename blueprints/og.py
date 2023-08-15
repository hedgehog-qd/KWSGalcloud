__all__ = ()

import od
import db
from quart import Blueprint
from quart import redirect
from quart import render_template
from quart import request
from quart import session
from quart import send_file
from blueprints.utils import flash
from functools import wraps

og = Blueprint('og', __name__)


def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if not session:
            return await flash('error', 'You must be logged in to access that page.', 'login')
        if not session['email']:
            return await flash('error', 'You must be logged in to access that page.', 'login')
        return await func(*args, **kwargs)

    return wrapper


@og.route('/')
@login_required
async def oghome():
    return await render_template('/og/oghome.html')


@og.route('/integral')
@login_required
async def integral():
    return await render_template('/og/integral.html')


@og.route('/player')
@login_required
async def player():
    return await render_template('/og/player.html')