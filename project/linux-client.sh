#!/bin/bash

# OUTLINE
: '
1. Authenticate
2. Parse full file-path name, content, and may be, type to json 
3. Upload the json object
'
####################################################################
# 0. Parsing command line arguments

num_file="$?"
log_level=1
usage="$(basename "$0") [-h] [-u filename] -- a secure personal cloud

where:
    -h show this help text
    -u upload a single file (possibly overwriting the one on server)"

while getopts ':hu:' option; do
    case "$option" in
	h) echo "$usage"
	   exit
	   ;;
	u) file=$OPTARG
	   ;;
	:) printf "missing argument for -$OPTARG\n" >&2
	   echo "$usage" >&2
	   exit 1
	   ;;
	?) printf "illegal option: $OPTARG\n" >&2
	    echo "$usage" >&2
	    exit 1
	    ;;
    esac
done

# exit if no options supplied
if [ -z "$file" ]; then echo "$usage"; exit; fi
path=$(realpath "$file")
if ! [[ $path =~ /home/shubhamkar/SPC* ]]
then
    echo "$file should be inside $HOME/SPC/"
    exit 1
fi


####################################################################

# 1. Authenticate
# Reference: https://stackoverflow.com/questions/21306515/how-to-curl-an-authenticated-django-app

login_url=http://127.0.0.1:8000/accounts/login/
your_user='mathews'
your_pass='1234'
cookies=cookies.txt
curl_bin="curl -s -c $cookies -b $cookies -e $login_url"

# echo -n "Django Auth: get csrftoken ..."
$curl_bin $login_url > /dev/null
if [ ! -f "$cookies" ]
then
    echo "Cookies file not found. Server may be down."
    exit 1
fi

django_token="csrfmiddlewaretoken=$(grep csrftoken $cookies | sed 's/^.*csrftoken\s*//')"

# echo $django_token

# echo -n " perform login ..."
$curl_bin \
    -d "$django_token&username=$your_user&password=$your_pass" \
    -X POST $login_url

# echo -n " do something while logged in ..."
# $curl_bin \
#    -d "$django_token&..." \
#    -X POST https://127.0.0.1:8000/whatever/

##########################################################################

if [ "$log_level" > "0" ]; then echo "Logged in..." ; fi

# 2. Determine file type, get file contents, name and type in a json object
# file=$(realpath "$1") # has been obtained in part 0 already
spc_root="/home/$USER/SPC/"
# get file name wrt to the spc root
name=$(echo ${file#$spc_root}) # is echo necessary?
content=$(cat "$file")
type=""

# Reference: https://stackoverflow.com/questions/12524437/output-json-from-bash-script
json_obj="{\"name\":\""$name"\", \"content\":\""$content"\", \"type\":\""$type"\"}"

printf "\nThe following will be sent: \n$json_obj\n"

########################################################################
# 3. Send json object to the server

printf "\nAttempting to upload...\n"

upload_url="http://0.0.0.0:8080/upload_file/"
# cookie="cookie2.txt" # cookie is unused

# curl -v -c $cookie -b $cookie "$upload_url"
# django_token="csrfmiddlewaretoken=$(grep csrftoken $cookie | sed 's/^.*csrftoken\s*//')"
# echo =============================
# echo Token: $django_token
# curl -v -c $cookie -b $cookie -d "data=hello&csrfmiddlewaretoken=$django_token" "$u
# pload_url"

# curl "$upload_url"
curl --header "Content-Type: application/json" \
     --request POST \
     --data "$json_obj" \
     "$upload_url"
  


# echo " logout"
# rm $cookies



