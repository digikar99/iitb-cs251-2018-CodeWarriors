.PHONY:skiprebuild skiprebuildh all clean
all:main
main:main.o depend.o
	g++ main.o depend.o -o main
main.o:main.cpp depend.h
	g++ -c main.cpp
depend.o:depend.cpp depend.h
	g++ -c depend.cpp
skiprebuild:
	touch -c depend.o main.o main
skiprebuildh:
	if [ main.o -nt depend.o ]; then \
	        touch -d "2 hours ago" -r depend.o depend.h ; else \
	        touch -d "2 hours ago" -r main.o depend.h ; fi 
	        make
clean:
	rm -rf main.o depend.o