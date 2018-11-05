import os
import pprint

pp = pprint.PrettyPrinter()

fc = {}
def get_tree(path):
    files = os.listdir(path)
    d={}
    for f in files:
        if os.path.isdir(f):
            d[f] = get_tree(f)
        else:
            d[f] = ""
    return d

pp.pprint(get_tree('.'))
