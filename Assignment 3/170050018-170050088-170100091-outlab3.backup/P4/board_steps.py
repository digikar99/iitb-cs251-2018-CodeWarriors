#! /usr/bin/python3

coord_list = []

with open('students.txt', 'r') as loc_file:
    var_list = loc_file.read().split()
    n = int(var_list[0])
#    global coord_list
    for i in range(1,2*n,2):
        coord_list.append({'x': int(var_list[i]), \
                           'y': int(var_list[i+1])})

    #print(coord_list)

def find_loc(x1, y1, x2, y2):
    if (x1 <= x2 and y1 <= y2):
        return (x2-x1 + y2-y1)
    else:
        return -1

# print(coord_list)
input_line = input()
str_num = input_line.split()
x1 = int(str_num[0])
y1 = int(str_num[1])
x2 = int(str_num[2])
y2 = int(str_num[3])

print(find_loc(x1,y1,x2,y2))

