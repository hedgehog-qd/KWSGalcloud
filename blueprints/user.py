__all__ = ()
# user模块
from flask import Flask, render_template, redirect, session, Blueprint

user = Blueprint('user', __name__)


# user模块
@user.route('/')
def register():
    return render_template('/user/home.html')
