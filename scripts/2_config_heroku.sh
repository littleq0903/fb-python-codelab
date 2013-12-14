#!/bin/bash
# Set config on Heroku 
heroku config:set $(cat heroku.config)
