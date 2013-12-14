#!/usr/bin/env python
"""
Example for Facebook Python SDK
Author: Colin Su <littleq0903@gmail.com>
"""
from bottle import Bottle, run, template
from bottle import static_file
import facebook

import os

# added a file "settings.py", which contains variables named:
# - FACEBOOK_APP_ID
# - FACEBOOK_SECRET
from settings import FACEBOOK_APP_ID, FACEBOOK_SECRET

# WSGI handler
app = Bottle()

@app.route('/login')
def login():
    return static_file('index.html', root=os.getcwd())

