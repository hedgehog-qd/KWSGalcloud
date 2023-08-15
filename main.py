__all__ = ()

from quart import Quart
from quart import render_template
import config

app = Quart(__name__)

app.secret_key = config.secret_key


@app.errorhandler(404)
async def page_not_found(e):
    # NOTE: we set the 404 status explicitly
    return (await render_template('404.html'), 404)


@app.errorhandler(500)
async def page_not_found(e):
    # NOTE: we set the 500 status explicitly
    return (await render_template('500.html'), 500)


@app.template_global()
def appVersion() -> str:
    return config.app_version


@app.template_global()
def appName() -> str:
    return config.app_name


@app.template_global()
def redirectUrl() -> str:
    return config.redirect_url


from blueprints.frontend import frontend

app.register_blueprint(frontend)

from blueprints.admin import admin

app.register_blueprint(admin, url_prefix='/admin')

from blueprints.user import user

app.register_blueprint(user, url_prefix='/user')

from blueprints.og import og

app.register_blueprint(og, url_prefix='/og')

if __name__ == '__main__':
    app.run(port=5000)  # blocking call
