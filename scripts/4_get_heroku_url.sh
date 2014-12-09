#!/bin/bash
parseurl () {
    local input=$(cat)
    local regex="Web URL:\ +(https://[[:alnum:]\.\-]*/)"
    [[ $input =~ $regex ]]
    echo ${BASH_REMATCH[1]}
}
heroku apps:info | parseurl
