#! /usr/bin/python3

class MenuItem():
    def __init__(self,n,c,r):
        self.name=n
        self.cost=c
        self.rating=r

    def __eq__(self,b):
        if(self.name==b.name and self.cost==b.cost and self.rating==b.rating):
            return True
        else:
            return False
        
    def __str__(self):
        return("Item: "+self.name+", Cost: "+str(self.cost)+", Rating: "+str(self.rating)+"00000")

    def __lt__(self,b):
        if self.rating != b.rating :
            return self.rating<b.rating
        else:
            return self.cost<b.cost

    def __hash__(self):
        return hash((self.name,self.cost,self.rating))
