#! /usr/bin/python3

class Menu():
    def __init__(self,l):
        self.items = l

    def __len__(self):
        return len(self.items)  

    def __str__(self):
       m=""
       for ele in self.items:
        #   m+=("Item: "+ele.name+", Cost: "+str(ele.cost)+", Rating: "+str(ele.rating)+"\n")
           m+=(str(ele)+"\n")
       return m
