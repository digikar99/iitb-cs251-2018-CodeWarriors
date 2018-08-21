#! /usr/bin/python3

L= []

class Snake :
    def __init__(self,name,length,venom):
        self.name = name
        self.length = length
        self.venom = venom

        
def snake(name,length,venom) :
    name = Snake(name,length,venom)
    L.append(name)

def findByVenom(venom):    
    for s in L:
        if(s.venom == venom):
            print(s.name)

def findByLength(length):
    for s in L:
        if (s.length == length):
            print (s.name)

         
def main() :
    with open("snakes.txt","r") as f1:
        n = int(f1.readline())
        for i in range(0,n):
            x = f1.readline()
            a = x.split()
            snake(a[0], int(a[1]), int(a[2]) )
        m = int(f1.readline())
        for i in range (0,m):
            x = f1.readline()
            a = x.split()
            if ( a[0] == "V" ):
                findByVenom(int(a[1]))
            else:
                findByLength(int(a[1]))

if __name__ == "__main__":
    main()
