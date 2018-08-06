#! /usr/bin/python3

def insideOut(x1, x2, x3, y1, y2, y3):

    a = float(0.5 *  ( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))
    if a>0 :
        return a
    else :
        return -1*a

def main() :
    x = input ("Enter the first coordinate : ")
    a = x.split()
    x1,y1 =  (float (a[0]), float (a[1]) )
    x = input ("Enter the second coordinate : ")
    b = x.split()
    x2,y2 =  (float(b[0]), float(b[1]) )
    x = input ("Enter the third coordinates : ")
    c = x.split()
    x3,y3 = (float(c[0]), float(c[1]) )
    x = input ("Enter coordinates of the key : ")
    d = x.split()
    x,y = ( float( d[0] ),float( d[1] ) )
    if ( insideOut(x1,x2,x3,y1,y2,y3) == insideOut(x1,x2,x,y1,y2,y) + insideOut(x1,x,x3,y1,y,y3) + insideOut(x,x2,x3,y,y2,y3) ) :
        print ("INSIDE")
    else :
        print ("OUTSIDE")

        
if __name__ == "__main__" :
    main()
