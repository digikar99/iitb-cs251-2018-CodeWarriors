#!/bin/bash

# OUTLINE
: '
1. Authenticate
2. Parse full file-path name, content, and may be, type to json 
3. Upload the json object
'

####################################################################

# 1. Authenticate
# Reference: https://stackoverflow.com/questions/21306515/how-to-curl-an-authenticated-django-app

LOGIN_URL=http://127.0.0.1:8000/accounts/login/
YOUR_USER='mathews1'
YOUR_PASS='1234'
COOKIES=cookies.txt
CURL_BIN="curl -s -c $COOKIES -b $COOKIES -e $LOGIN_URL"

# echo -n "Django Auth: get csrftoken ..."
$CURL_BIN $LOGIN_URL > /dev/null
DJANGO_TOKEN="csrfmiddlewaretoken=$(grep csrftoken $COOKIES | sed 's/^.*csrftoken\s*//')"

# echo -n " perform login ..."
$CURL_BIN \
    -d "$DJANGO_TOKEN&username=$YOUR_USER&password=$YOUR_PASS" \
    -X POST $LOGIN_URL

# echo -n " do something while logged in ..."
$CURL_BIN \
    -d "$DJANGO_TOKEN&..." \
    -X POST https://yourdjangowebsite.com/whatever/

##########################################################################

# 2. Determine file type, get file contents, name and type in a json object
FILE=$(realpath "$1")
SPC_ROOT="/home/$USER/SPC/"
# get file name wrt to the spc root
NAME=$(echo ${FILE#$SPC_ROOT}) # is echo necessary?
CONTENT=$(cat "$FILE")
TYPE=""

# Reference: https://stackoverflow.com/questions/12524437/output-json-from-bash-script
JSON_OBJ="{\"name\":\""$NAME"\", \"content\":\""$CONTENT"\", \"type\":\""$TYPE"\"}"

echo $JSON_OBJ

########################################################################
# 3. Send json object to the server

# echo " logout"
rm $COOKIES



