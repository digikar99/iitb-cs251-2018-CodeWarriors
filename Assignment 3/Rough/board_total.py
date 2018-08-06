 
with open('students.txt', 'r') as loc_file:
    var_list = loc_file.read().split()
    n = int(var_list[0])
    coord_list = []
    for i in range(1,2*n,2):
        coord_list.append((int(var_list[i]), \
                           int(var_list[i+1])))

    print(coord_list)
