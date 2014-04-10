import os

from fabric.api import local

PROJECT_DIR = os.path.dirname(__file__)

def run_server():
   	''' start dev server '''
   	babel_compile()
   	local("dev_appserver.py --log_level debug  %s" % PROJECT_DIR)

def deploy():
	''' deploy app to the cloud '''
	app_id=None # add your app id here
	if not app_id:
		raise Exception("App id is None. Add your app_id to deploy method at fabfile.py")
	local("appcfg.py -A %s update %s" % (app_id, PROJECT_DIR))

def babel_extract():
	''' extract terms to be transalated '''
	local("pybabel extract -F babel.cfg -o locale/messages.pot .")

def babel_init(locale=None):
 	''' initialize the informed locale - use it carefully it overwrites your current po file'''
 	# initialize your locales here, add or remove
 	if not locale:
 		raise Exception("Locale is None. Usage: fab babel_init:<locale> ")
 	local("pybabel init -i locale/messages.pot -d locale -l %s" % locale)

def babel_compile():
	''' compile all locales '''
	local("pybabel compile -f -d locale")

def babel_update():
	''' update po transtation files '''
	local("pybabel update -i locale/messages.pot -d locale")

def babel_extract_update():
	''' extract terms and update all po files '''
	babel_extract()
	babel_update()
