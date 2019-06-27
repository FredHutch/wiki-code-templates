README file

# Flask app template

This is a template for flask apps.  It is meant as a very basic skeleton for a typical flask application to reduce the overhead of creating a new website.  This is not meant for large, complex apps but should suffice for small web apps that consist only of a few pages and don't need to do anything particularly fancy.

## Overview and contents
Included is a basic flask app, Bootstrap 4, and the various libraries (jquery, etc.) necesary to support bootstrap 4.  All versions in the Pipfile.lock were the latest available at the time this README was written.

## Running the app
Run `run.sh` to run the app.

## Directory structure and files
`run.py`: imports the app and is meant to be run with `flask run` along with the `FLASK_APP` environment variable set (see `run.sh`).
`run.sh`: use this to start the app.  It will set the `FLASK_APP` environment variable required by flask's default development server.

`app`: this folder contains the actual code to do anything useful.

`app/templates`: is where all Jinja templates should be located by default.

`app/templates/layout.html`: base Jinja template that can be inherited and provides a simple layout for content, includes the relevant CSS/javascript files including external resources (e.g. Bootstrap 4), and avoids the need to duplicate code for additional pages.

`app/templates/index.html`: effectively empty "hello, world" default landing page that inherits from `layout.html`

`app/static`: directory contains files served statically from the site, such as css, js, images, etc.

`app/static/style.css`: empty css file for use with the project.  Automatically included by `layout.html`

`app/static/script.js`: empty javascript file for use with the project.  Automatically included by `layout.html`

`config.py.ex`: example config file.  Use an actual `config.py` file for configuration.  It will automatically be loaded when the app starts.

`app/__init__.py`: flask is initialized in this file, including configuration

`app/routes.py`: location of routes for flask.  Imported automatically in `__init__.py`

`test/test_app.py`: contains a sample unit test that can be run with pytest

`test/__init__.py`: makes test folder into a package so that it can just import app in order to test things in the `app/` directory
