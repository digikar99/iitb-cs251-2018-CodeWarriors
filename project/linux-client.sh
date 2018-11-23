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
log_level=0 # in addition, see "exit 1" in authenticate
host="http://127.0.0.1:8000/"
login_url="$host"'login/'
upload_url="$host"'upload_file/'
download_url='' # created in authenticate
cookies=~/.config/iitb-spc/.cookies
auth_file=~/.config/iitb-spc/.auth
enc_file=~/.config/iitb-spc/.credentials
key_file=~/.config/iitb-spc/.privkey
pub_key=~/.config/iitb-spc/.pubkey
username=''
password=''
usage="$(basename "$0") command-line interface 

Commands:
 help			show this help text
 sync 			keep files with the most recent updates on both
 upload [file|folder/]	upload the single file folder 
 download [file|folder/] download the single file / folder 
 config			provide new username and password
 ende-change		change encryption / decryption scheme
 ende-list		see encryption scheme; get keys in a file $HOME/keys.txt
(see man page for more detailed help)
"

main() {
    if [ "$log_level" -gt "1" ] ; then printf "$# argument(s): $*\n\n"; fi
    if [ "$#" = "0" ] ; then
	printf "$usage"; exit 1
    elif [ "$1" = "help" ]; then
	printf "$usage" ; exit 0;
    elif [ "$1" = "ende-change" ]; then ende-change
    elif [ "$1" = "ende-list" ]; then
	echo -n Encryption scheme:
	cat "$enc_file"
	cp "$key_file" "$HOME/keys.txt"
    elif [ "$1" = "config" ]; then config
    elif [ "$1" = "sync" ]; then
	authenticate
	sync
    else
	if [ -z "$2" ]; then printf "$usage"; exit 1; fi
	authenticate
	pdir="$(pwd)"
	#echo $pdir
	if ! [[ $pdir =~ $HOME/SPC* ]];	then
	    echo "You should operate inside $HOME/SPC"
	    exit 1
	fi
	if [ "$1" = "upload" ]; then
	    if [ "$2" = "." ]; then item="$(pwd)"; else item="$2"; fi
	    echo Item: $item
	    upload "$item"
	elif [ "$1" = "download" ]; then
	    spc_root="$(echo $HOME/SPC)"
	    item="${2#$spc_root}"
	    download "$item"
	    curl -s -c "$cookies" -b "$cookies" -e "$host"'download_file/sucess/' "$host"'download_file/sucess/';
	else printf "Unknown command: $1\n"; exit 1; fi
    fi
				    
}

config() {
    
    printf "Enter login details. (Press Ctrl+C to cancel this action.)\n"
    printf "NOTE: YOU WILL NEED TO, FIRST, REGISTER ON $host\n"
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
    username=$user
    password=$pass
    
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

    $curl_bin \
	-d "$django_token&username=$user&password=$pass" -X POST $login_url
}

ende-change() {
    printf "Choose an encryptions scheme: \n 1. AES-CBC-192 \n 2. Triple DES 192 "
    printf "\n 3. DES-CBC-64 \n(Or press Ctrl+C to cancel.)\nEnter [1], 2 or 3: "
    read choice
    if [ -z "$choice" ]; then choice=1; fi
    touch $key_file
    if [ "$choice" = "1" ]; then
	echo -aes-192-cbc > $enc_file
    key=$(openssl rand -hex 24)
    iv=$(openssl rand -hex 16)
    elif  [ "$choice" = "2" ]; then
	echo -des-ede3-cbc > $enc_file
	key=$(openssl rand -hex 24)
    iv=$(openssl rand -hex 16)
    elif  [ "$choice" = "3" ]; then
	echo -des-cbc > $enc_file
	key=$(openssl rand -hex 8)
    iv=$(openssl rand -hex 16)
    fi
    printf "$key\n$iv\n" > $key_file
}

sync() {
    # printf "Sync is not yet ready.\n"
    url="$host"'download_file/all_files/'"$username/"
    url="$(replace_spaces_in_url "$url")"
    curl_bin="curl -s -c $cookies -b $cookies -e $url"
    contents="$($curl_bin "$url")"
    #echo $contents
    server_files=$(python3 <<EOF
for file in $contents:
    print(file)
EOF
		)
    # printf "$server_files"
    IFS=$'\n'
    for file in $server_files ;
    do
	unset IFS
	local_file=${file#$username/}
	if [ -f "$local_file" ]; then 
	    time_url="$host"'download_file/last_update_time/'"$file"
	    time_url="$(replace_spaces_in_url "$time_url")"
	    curl_bin="curl -s -c $cookies -b $cookies -e $time_url"
	    on_server=$($curl_bin $time_url)
	    #echo $on_server
	    on_client=$(stat -c %Z "$local_file")
	    if [ "$log_level" -gt "0" ]; then
		echo Server: $on_server
		echo Client: $on_client
	    fi
	    difference=$(( $on_client - $on_server ))
	    if [ "$difference" -gt "0" ] ; then upload_file "$local_file" ;
	    elif [ "$difference" -lt "0" ]; then download_file "$local_file" ;
	    fi
	else download_file "$local_file"
	fi
    done
    # At the end of this, whichever files exist on the client
    # are the new ones. Therefore, upload all the files!
    IFS=$'\n' # use new lines as field separators
    subitem_list=$(find "$HOME/SPC/" -not -type d)
    for subitem in $subitem_list; do
	# if it exists on the server, skip
	remote_file="$username/""${subitem#$HOME/SPC/}"
	if [ ! -z "$server_files" ]; then
	   exists=$(python3 -c "print(\"$remote_file\" in $contents)")
	else exists=False ; fi
	if [ "$exists" = "False" ]; then upload_file "$subitem"; fi
    done
				    
				    
    
}

upload() {
    item="$1" # handles a single file or folder

    if [ -d "$item" ]; then
	delete_remote_folder "$item"
	IFS=$'\n' # use new lines as field separators
	subitem_list=$(find "$item" -not -type d)
	for subitem in $subitem_list; do
	    #echo Uploading file $file ...
	    upload_file "$subitem"
	done
    else
	upload_file "$item"
    fi
}

download() {
    #echo "$1"
    if [ ! -z "$1" ]; then local item="$(ensure_trailiing_slash "$1")";
    else local item="$1" ; fi
    download_url="$host"'download_file/data/'"$username/$item"
    download_url="$(replace_spaces_in_url "$download_url")"
    curl_bin="curl -s -c $cookies -b $cookies -e ""$download_url"
    #echo "$download_url"
    local contents="$($curl_bin "$download_url")"
    #echo $contents
    local temp=$(python3 -c "print(type($contents) == type({}))" 2> /dev/null)
    # echo $temp
    if [ "$temp" = "True" ] && [ ! -z "$contents"  ] ; then
	# that is a dictionary indeed
	echo Deleting $item on local...
	rm -rf "$item"
	local sub_dirs=$(python3 <<EOF
dir_contents = dict($contents)
for item in dir_contents:
    if dir_contents[item] == 'dir':
        print(item)
EOF
		)
	IFS=$'\n'
	for dir in $sub_dirs; do unset IFS; download "$dir"; done
	# echo $contents
	local files=$(python3 <<EOF
dir_contents = dict($contents)
for item in dir_contents:
    if dir_contents[item] == 'file':
        print(item)
EOF
	     )
	IFS=$'\n'
	for file in $files; do unset IFS; download_file "$item$file"; done
    else
	# that is not a dictionary
	download_file "$1"
    fi
    
}

upload_file(){
    if [ -L "$1" ]; then
	echo $1 is a symlink. It may break on other devices.
	printf "  Uploading $1 still..\n"
    elif [ -f "$1" ]; then
	spc_root="/home/$USER/SPC/"
	# get file name wrt to the spc root
	name=$(echo ${1#$spc_root}) # is echo necessary?
	type=$(get_type "$name")
	echo Uploading $name...
	#enc "$1"
	content=$(enc "$1")
	lut=$(stat -c %Z "$1") # last_update_time
	md5=$(echo $content | md5sum | cut -d " " -f 1)
	if [ "$log_level" -gt "0" ]; then
	    echo =================================
	    echo name_path: $name
	    echo file_data: [not shown]
	    echo last_update_time: $lut
	    echo file_type: $type
	    echo md5sum: $md5
	    #echo $content > "$1.enc"
	fi

	unset IFS
	curl_bin="curl -s -c $cookies -b $cookies -e $upload_url"
	$curl_bin $upload_url > /dev/null
	if [ ! -f "$cookies" ]
	then
	    echo "No cookies file found. Is the server running?"
	    # exit 1 # comment only for testing
	fi

	django_token="csrfmiddlewaretoken=$(grep csrftoken $cookies | sed 's/^.*csrftoken\s*//')"
	
	if [ "$log_level" -gt "1" ]; then
	    echo django token for upload page: $django_token
	fi
	
	token=\"$(grep csrftoken $cookies | sed 's/^.*csrftoken\s*//')\"

	CURL=$($curl_bin "$upload_url" -X POST -d @- <<EOF
$django_token&user_name_path=$username/$name&file_data=$content&last_update_time=$lut&file_type=$type&md5sum=$md5
EOF
	    )
	if [ ! -z "$CURL" ]; then
	    # echo Curl was unsuccessful
	    $curl_bin "$(replace_spaces_in_url "$host"delete"/$username/$name")" > /dev/null
	    $curl_bin "$upload_url" -X POST -d @- <<EOF
$django_token&user_name_path=$username/$name&file_data=$content&last_update_time=$lut&file_type=$type&md5sum=$md5
EOF
	fi	
    else
	echo $1 is not a regular file or a symlink.
	printf "  Uploading it as an empty file...\n"
    fi
}

download_file() {
    # downloads a single file
    echo Downloading "$1"...
    mkdir -p "$(dirname "$1")"
    download_url="$host"'download_file/data/'"$username/$1"
    download_url=${download_url// /%20}
    curl_bin="curl -s -c $cookies -b $cookies -e ""$download_url"
    contents="$($curl_bin "$download_url")"
    dec "$contents" "$1"
    time_url="$host"'download_file/last_update_time/'"$username/$1"
    time_url="$(replace_spaces_in_url "$time_url")"
    curl_bin="curl -s -c $cookies -b $cookies -e $time_url"
    on_server=$($curl_bin $time_url)
    touch -d @$on_server "$1"
    #file_data=$(dec "$contents")
    #printf "$file_data" > "$1"
    
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

dec() {
    method=$(cat $enc_file)
    unset -v key iv
    for var in key iv; do
	IFS= read -r "$var" || break
    done < $key_file
    # echo "$1" | tr ' ' '+' | sed -e "s/.\{80\}/&\n/g"
    echo "$1" | tr ' ' '+' | sed -e "s/.\{80\}/&\n/g" \
	| openssl enc -d $method -K $key -base64 -iv $iv -nosalt -a -out "$2"
}

get_type() {
    possible_extension="${1##*.}"
    if [ "$1" = "$possible_extension" ]; then
	read -p "Specify filetype (mp4, png, bmp, jpg, jpeg, [other]) of $1: " possible_extension
	if [ -z "$possible_extension" ]; then possible_extension=other; fi
    fi
    echo $possible_extension
}

ensure_trailiing_slash() {
    echo "${1%/}/" # do not remove the new line
}

replace_spaces_in_url() {
    echo "${1// /%20}" # do not remove the new line
}

delete_remote_folder() {
    item="$(ensure_trailiing_slash "$1")"
    if [ "$item" = "$HOME/SPC/" ]; then
	all_files_url="$host"'download_file/all_files/'"$username/"
    else
	all_files_url="$host"'download_file/all_files/'"$username/$item"
    fi
    all_files_url="$(replace_spaces_in_url "$all_files_url")"
    curl_bin="curl -s -c $cookies -b $cookies -e ""$all_files_url"
    contents="$($curl_bin "$all_files_url")"
    #echo "Contents: $contents"
    if [ "$?" = "0" ]; then # indicates folder exists on remote
	
	file_list=$(python3 <<EOF
for item in $contents:
    print(item)
EOF
		 )
	#echo $file_list
	IFS=$'\n'
	for file in $file_list; do
	    file_url="$host"'delete/'"$file"
	    file_url="$(replace_spaces_in_url "$file_url")"
	    curl_bin="curl -s -c $cookies -b $cookies -e ""$file_url"
	    unset IFS
	    echo Deleting $file on remote...
	    $curl_bin "$file_url" > /dev/null
	done
    fi
	
}

main "$@"
