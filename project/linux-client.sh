#!/bin/bash

# OUTLINE

# 1. Authenticate
# Reference: https://stackoverflow.com/questions/21306515/how-to-curl-an-authenticated-django-app

LOGIN_URL=http://127.0.0.1:8000/accounts/login/
YOUR_USER='mathews1'
YOUR_PASS='1234'
COOKIES=cookies.txt
CURL_BIN="curl -s -c $COOKIES -b $COOKIES -e $LOGIN_URL"

echo -n "Django Auth: get csrftoken ..."
$CURL_BIN $LOGIN_URL > /dev/null
DJANGO_TOKEN="csrfmiddlewaretoken=$(grep csrftoken $COOKIES | sed 's/^.*csrftoken\s*//')"

echo -n " perform login ..."
$CURL_BIN \
    -d "$DJANGO_TOKEN&username=$YOUR_USER&password=$YOUR_PASS" \
    -X POST $LOGIN_URL

echo -n " do something while logged in ..."
$CURL_BIN \
    -d "$DJANGO_TOKEN&..." \
    -X POST https://yourdjangowebsite.com/whatever/

# 2. Determine file type, get file contents, name and type in a json object

# 3. Send json object to the server

echo " logout"
rm $COOKIES



