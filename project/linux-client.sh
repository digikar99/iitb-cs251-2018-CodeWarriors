#!/bin/bash

# OUTLINE
: '
1. Authenticate
2. Parse full file-path name, content, and may be, type to json 
3. Upload the json object
'
####################################################################
# 0. Parsing command line arguments

#set -x
arg_list="$@"
log_level=1 # in addition, see "exit 1" in authenticate
host="127.0.0.1:8000/"
login_url="$hostlogin/"
upload_url="$hostupload_url/"
cookies=~/.config/iitb-spc/.cookies
auth_file=~/.config/iitb-spc/.auth
enc_file=~/.config/iitb-spc/.credentials
key_file=~/.config/iitb-spc/.privkey
pub_key=~/.config/iitb-spc/.pubkey    
usage="$(basename "$0") command-line interface 

Commands:
 help			show this help text
 sync 			upload and download the files with latest changes
 upload [file/folder]	upload the single file folder 
 download [file/folder] download the single file / folder 
 config			provide new username and password
 ende-change		change encryption / decryption scheme
(see man page for more detailed help)
"

main() {
    if [ "$log_level" -gt "1" ] ; then printf "$# argument(s): $*\n\n"; fi
    if [ "$#" = "0" ] ; then
	printf "$usage"; exit 1
    elif [ "$1" = "help" ]; then
	printf "$usage" ; exit 0;
    elif [ "$1" = "ende-change" ]; then ende-change
    elif [ "$1" = "config" ]; then config
    else
	if [ -z "$2" ]; then printf "$usage"; exit 1; fi
	authenticate
	path=$(realpath "$2")
	if ! [[ $path =~ $HOME/SPC* ]]
	then
	    echo "$2 should be inside $HOME/SPC/"
	    exit 1
	fi
	if [ "$1" = "upload" ]; then upload "$2"
	elif [ "$1" = "download" ]; then download "$2"
	elif [ "$1" = "sync" ]; then sync "$2"
	else printf "Unknown command: $1\n"; exit 1; fi
    fi
				    
}

config() {
    
    printf "Change username and password: (Press Ctrl+C to cancel this action.)\n"
    read -p "Username: " user 
    read  -p "Password: " -s pass 
    if [ "$log_level" -gt "1" ] ; then
	printf "Username: $user\nPassword: $pass\n"
    else
	echo
    fi
    printf "$user $pass\n" > $auth_file
    if [ "$?" = "1" ] ; then
	printf "Could not write to ~/.config/iitb-spc/.auth. Please try reinstalling the iitb-spc.\n"
    else
	ende-change 1
	exit 0
    fi
}

authenticate() {
    # Reference: https://stackoverflow.com/questions/21306515/how-to-curl-an-authenticated-django-app
    if [ ! -f $auth_file ]; then
	printf "No $auth_file file found.\n"
	config
    fi
    read user pass  < $auth_file
    if [ "$log_level" -gt "1" ] ; then
	echo Username: $user
	echo Password: $pass
    fi

    curl_bin="curl -s -c $cookies -b $cookies -e $login_url"

    # echo -n "Django Auth: get csrftoken ..."
    $curl_bin $login_url > /dev/null
    if [ ! -f "$cookies" ]
    then
	echo "No cookies file found. Is the server running?"
	# exit 1 # comment only for testing
    fi

    django_token="csrfmiddlewaretoken=$(grep csrftoken $cookies | sed 's/^.*csrftoken\s*//')"

    if [ "$log_level" -gt "1" ]; then
	echo django token for login page: $django_token
    fi

    # echo -n " perform login ..."
    $curl_bin \
	-d "$django_token&username=$user&password=$pass" -X POST $login_url

}

ende-change() {
    printf "Choose an encryptions scheme: \n 1. AES-CBC-192 \n 2. Triple DES 192 "
    printf "\n 3. Camellia-CBC-192 (NOTE: Doesn't work in webclient.)\n(Or press Ctrl+C to cancel.)\nEnter [1], 2 or 3: "
    read choice
    if [ -z "$choice" ]; then choice=1; fi
    touch $key_file
    if [ "$choice" = "1" ]; then
	echo -aes-192-cbc > $enc_file
    elif  [ "$choice" = "2" ]; then
	echo -des-ede3-cbc > $enc_file
    elif  [ "$choice" = "3" ]; then
	echo -camellia-192-cbc > $enc_file
    fi
    key=$(openssl rand -hex 24)
    iv=$(openssl rand -hex 16)
    printf "$key\n$iv\n" > $key_file
}

sync() {
    # printf "Sync is not yet ready.\n"

    on_server=0 # get time stamp of the file/folder on server

    on_client=$(stat -c %Z "$1")
    difference=$(($on_client - $on_server))
    if [ "$log_level" -gt "1" ]; then
	on_server=$(stat -c %Z $HOME/SPC) # for testing purposes
	echo Last update time on server: $on_server
	echo Last update time on client: $on_client
	difference=$(($on_client - $on_server))
	echo $difference
    fi
    if [ "$difference" -gt "1" ]; then
	upload "$2"
    else
	download "$2"
    fi
    
    exit 0
}

upload() {
    echo In the case of a conflict, this will overwrite any file present on the server.
#    shift # ignore the first arg
    if [ "$#" = "0" ]; then
	echo "Do you want to do this for all the files? ([y]/n)"
	read response
	if [[ $response = "n" || $response = "N" ]]; then exit 0; fi
    fi
    item="$1" # handles a single file or folder
    if [ -d "$item" ]; then
	IFS=$'\n' # use new lines as field separators
	file_list=$(find ~/SPC -not -type d)
	for file in $file_list; do
	    #echo Uploading file $file ...
	    upload_file "$file"
	done
    else
	upload_file "$item"
    fi
}

download() {
    printf "Download is not yet ready.\n"
    exit 0
}

upload_file(){
    if [ -L "$1" ]; then
	echo $1 is a symlink. It may break on other devices.
	printf "  Uploading $1 still..\n"
    elif [ -f "$1" ]; then
	spc_root="/home/$USER/SPC/"
	# get file name wrt to the spc root
	name=$(echo ${file#$spc_root}) # is echo necessary?
	type=""
	echo Uploading $1...
	#enc "$1"
	content=$(enc "$1")
	if [ "$log_level" -gt "0" ]; then
	    #echo =================================
	    echo $1 encrypted:
	    echo $content;
	fi

	curl_bin="curl -s -c $cookies -b $cookies -e $upload_url"
	$curl_bin $login_url > /dev/null
	if [ ! -f "$cookies" ]
	then
	    echo "No cookies file found. Is the server running?"
	    # exit 1 # comment only for testing
	fi

	django_token="csrfmiddlewaretoken=$(grep csrftoken $cookies | sed 's/^.*csrftoken\s*//')"
	
	if [ "$log_level" -gt "1" ]; then
	    echo django token for upload page: $django_token
	fi
	$curl_bin \
	    -d "$django_token&filename=$name&filecontent=$content" \
	    -X POST "$upload_url"
    else
	echo $1 is not a regular file or a symlink.
	printf "  Uploading it as an empty file...\n"
    fi
}

enc() {
    method=$(cat $enc_file)
    unset -v key iv
    for var in key iv; do
	IFS= read -r "$var" || break
    done < $key_file
    # Reference: https://unix.stackexchange.com/questions/339992/how-to-read-different-lines-of-a-file-to-different-variables
    # echo Key: $key
    # echo IV: $iv
    openssl enc $method -K $key -iv $iv -nosalt -base64 -in "$1" | tr -d '\n'	
}

main "$@"



# exit if no options supplied
# if [ -z "$file" ]; then echo "$usage"; exit; fi
# path=$(realpath "$file")
# if ! [[ $path =~ $HOME/SPC* ]]
# then
#     echo "$file should be inside $HOME/SPC/"
#     exit 1
# fi


####################################################################

# 1. Authenticate

# echo -n " do something while logged in ..."
# $curl_bin \
#    -d "$django_token&..." \
#    -X POST https://127.0.0.1:8000/whatever/

##########################################################################

# if [ "$log_level" > "0" ]; then echo "Logged in..." ; fi

# # 2. Determine file type, get file contents, name and type in a json object
# # file=$(realpath "$1") # has been obtained in part 0 already
# spc_root="/home/$USER/SPC/"
# # get file name wrt to the spc root
# name=$(echo ${file#$spc_root}) # is echo necessary?
# content=$(cat "$file")
# type=""

# # Reference: https://stackoverflow.com/questions/12524437/output-json-from-bash-script
# json_obj="{\"name\":\""$name"\", \"content\":\""$content"\", \"type\":\""$type"\"}"

# printf "\nThe following will be sent: \n$json_obj\n"

# ########################################################################
# # 3. Send json object to the server

# printf "\nAttempting to upload...\n"

# upload_url="http://127.0.0.1:8000/upload_file/"
# # cookie="cookie2.txt" # cookie is unused

# # echo Django token: $django_token

# $curl_bin \
#     -d "$json_obj" \
#     -X POST "$upload_url"

# curl -v -c $cookie -b $cookie "$upload_url"
# django_token="csrfmiddlewaretoken=$(grep csrftoken $cookie | sed 's/^.*csrftoken\s*//')"
# echo =============================
# echo Token: $django_token
# curl -v -c $cookie -b $cookie -d "data=hello&csrfmiddlewaretoken=$django_token" "$u
# pload_url"

# curl "$upload_url"
# curl --header "Content-Type: application/json" \
#      --request POST \
#      --data "$json_obj" \
#      "$upload_url"



