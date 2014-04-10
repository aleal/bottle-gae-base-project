## Bottle Google App Engine Base Project

Project based on https://github.com/GoogleCloudPlatform/appengine-python-bottle-skeleton

## Run Locally

###The easy way

1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too. Add app engine to your PATH if necessary. 

2. Clone this repository with

   ```shell
   git clone git@github.com/aleal/bottle-gae-base-project.git
   
   ```
3. Install dependencies in the project's `lib/` directory.
   Note: App Engine can only import libraries from inside your project directory.

   ```shell
   cd bottle-gae-base-project 
   pip install -r requirements.txt -t lib/
    # libs for development enviroment
   pip install -r requirements-dev.txt
  
   ```
4. Run this project locally from the command line:

   ```
   dev_appserver.py .
   ```

Open [http://localhost:8080](http://localhost:8080)

### The very easy way ;)

If you are in Unix enviroment...

1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too. Add app engine to your PATH if necessary. 

2. Clone this repository with

   ```shell
   git clone git@github.com/aleal/bottle-gae-base-project.git
   
   ```
3. Setup enviroment

   ```shell
   cd bottle-gae-base-project 
   source setup.sh
   ```
   
4. Run the dev server 
   ```shell
   fab run_server
   ```
   
   Fabric Available commands:
   ```
    babel_compile             compile all locales
    babel_extract             extract terms to be transalated
    babel_extract_update      extract terms and update all po files
    babel_init                initialize a locale - use it carefully it overwrites your current po file
    babel_update              update po transtation files
    deploy                    deploy app to the cloud -  don't forget to edit the fabfile.py to add you app id
    run_server                start dev server
    ```

## Deploy
To deploy the application:

1. Use the [Admin Console](https://appengine.google.com) to create an app and
   get the project/app id. (App id and project id are identical)
1. [Deploy the
   application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with

   ```
   appcfg.py -A <your-project-id> --oauth2 update .
   ```

2. Or 
   ```
   fab deploy
   ```
