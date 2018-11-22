home:
	mkdir -p $$HOME/SPC
bin:
	mkdir -p $$HOME/bin

config:
	mkdir -p $$HOME/.config/iitb-spc

curl:
	sudo apt install curl

install: home config curl bin
	rm -f $$HOME/bin/iitb-spc ;\
	fp="$(realpath linux-client.sh)" ;\
	ln -s $$fp $$HOME/bin/iitb-spc ;\
	chmod +x ~/bin/iitb-spc
