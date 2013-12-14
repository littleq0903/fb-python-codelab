#!/bin/bash
heroku apps:info | grep -Eo "http://[[:alnum:]\.-]*/"
