def expand(lb, ub, skip):
    expanded_list = []
    for num in range(lb, ub+1):
        bool = False
        for s in skip:
            if s % num == 0:
                bool = True
                break
        if bool == False:
            expanded_list.append(num) 
    return expanded_list
print(expand(7, 17, [60, 16]))