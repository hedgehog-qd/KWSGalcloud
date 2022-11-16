__all__ = ()
import od
from quart import Blueprint
from quart import redirect
from quart import render_template
from quart import request
from quart import session
from quart import send_file

admin = Blueprint('admin', __name__)


# admin模块
@admin.route('/')
async def alluser():
    return 'adminhome'


@admin.get("/manualrefresh")
async def read_root():
    stacode = od.refresh()
    if stacode == 0:
        return {"RefreshDatabase": "success"}
    elif stacode == 1:
        return {"failed": "you can't refresh the database toooo many times!"}
    elif stacode == 2:
        return {"error": "something wrong happened"}
