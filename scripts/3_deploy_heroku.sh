#!/bin/bash
# Script to deploy to heroku
git add .
git commit -m '[AUTO HEROKU DEPLOY]'
git push heroku master
