"""`main` is the top level module for your Bottle application."""
import os
import json 

from google.appengine.api import users

import bottle
from bottle.ext import i18n

IS_DEV = os.environ['SERVER_SOFTWARE'].startswith('Development')

i18n.i18n_defaults(bottle.Jinja2Template, bottle.request)

app = bottle.Bottle()

OPENID_URLS = {
               'google' : 'http://google.com/accounts/o8/id',
               'yahoo' : 'http://me.yahoo.com/',
               'aol' : 'http://openid.aol.com/',
               'myspace' : 'http://myspace.com/',
               'myopenid' : 'http://myopenid.com/',
               'versign' : 'http://pip.verisignlabs.com/',
               'launchpad' : 'http://login.launchpad.net/'
               }

def make_url(path):
    return "/%s%s" % (app.lang, path)

def get_session_data():
    user = users.get_current_user()
    index_url = make_url("/")
    if not user:
        bottle.redirect(index_url)
    data = { 'user': user, 'logout_url': users.create_logout_url(index_url), 'current_path': bottle.request.path}
    return data


@app.route('/openid/<provider>')
def openid(provider):
    user =  users.get_current_user()
    next = make_url("/home")
    if user:
        bottle.redirect(next)
    else:
        openid_url = OPENID_URLS[provider]
        bottle.redirect(users.create_login_url(next, federated_identity=openid_url))

@app.route('/')
def index():
    return bottle.jinja2_template("templates/index.html", {'title': app._("Index")})

@app.route('/home')
def home():
    data = get_session_data()
    data['title'] = app._("Home")
    return bottle.jinja2_template("templates/home.html", data)

@app.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return bottle.jinja2_template("templates/404.html", {'title': app._("Not Found")})

@app.error(500)
def error_500(error):
    """Return a custom 500 error."""
    data = {'title': app._("Internal Server Error"), 'is_dev': IS_DEV, 'error': error}
    return bottle.jinja2_template("templates/500.html", data)

bottle_app = i18n.I18NMiddleware(app, i18n.I18NPlugin(domain='messages', default='en', locale_dir='./locale'))