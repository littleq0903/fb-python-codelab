#!/usr/bin/env python
"""
Example for Facebook Python SDK
Author: Colin Su <littleq0903@gmail.com>
"""
from bottle import Bottle, run, template
from bottle import static_file
from bottle import jinja2_template
import facebook

import os

# setup these environment variable by adding "heroku.config"
# - FACEBOOK_APP_ID
# - FACEBOOK_SECRET
FACEBOOK_APP_ID = os.environ['FACEBOOK_APP_ID']
FACEBOOK_SECRET = os.environ['FACEBOOK_SECRET']

# WSGI handler
app = Bottle()

# Checkpoint 0
@app.route('/login')
def login():
    template_data = {
        'facebook_app_id': FACEBOOK_APP_ID
    }
    return jinja2_template('index.html', **template_data)

