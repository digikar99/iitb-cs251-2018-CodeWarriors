#!/bin/bash

# echo "This script will set up spc (Secure Personal Cloud) on your device by doing the following:"
# echo " 1. Create SPC directory in your home, if it does not exists."
# echo ' 2. Create a link named spc in ~/bin to linux-client.sh present in this directory' 

if [ ! -d "$HOME/SPC" ]
then 
    echo Creating $HOME/SPC...
    mkdir "$HOME/SPC"
else
    echo $HOME/SPC already exists...
fi

to_path="$(realpath linux-client.sh)"

if [ ! -f "$HOME/iitb-spc" ]
then
    echo "Creating link to linux-client.sh..."
    ln -s "$to_path" "$HOME/bin/iitb-spc"
else
    echo "$HOME/bin/iitb-spc already exists. Would you like to overwrite it? [y/N]"
    read overwrite
    if [ "$overwrite" = "y" || "$overwrite" = "Y" ]
    then
	echo Yes
    else
	echo "$HOME/bin/iitb-spc not overwritten. Run ./install.sh again if you wanted to overwrite it."
	exit 0
    fi
    rm "$HOME/bin/iitb-spc"
    ln -s "$to_path" "$HOME/bin/iitb-spc"
fi

echo "Currently, we haven't included set up additional necessary tools."
echo "Fun Fact: Entering spc in bash suggests installing supercat."
    
    
