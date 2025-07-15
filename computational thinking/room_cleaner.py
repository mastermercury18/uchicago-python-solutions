# right == j + 1 
# up == i - 1
# left == j - 1
# down == i + 1

# grid = [[d, v, d, d], [d, v, d, d], [d, v, d, d]]
# total_rows = len(grid)
# total_cols = len(grid[0])

# boundary conditions 
# i >= 0 and i <= total_rows - 1
# j >=0 and j <= total_cols - 1

def clean_room(room, start_loc, fuel):
    total_rows = len(room)
    total_cols = len(room[0])

    i, j = start_loc 

    cleaned = 0

    if room[i][j] == 'd':
        cleaned += 1 
    
    while fuel > 0:
        if boundary_checker(i, j+1, total_rows, total_cols):
            j += 1
            fuel -= 1
            if room[i][j] == 'd':
                cleaned += 1
        elif boundary_checker(i - 1, j, total_rows, total_cols):
            i -= 1
            fuel -= 1
            if room[i][j] == 'd':
                cleaned += 1
        elif boundary_checker(i, j - 1, total_rows, total_cols):
            j -= 1
            fuel -= 1
            if room[i][j] == 'd':
                cleaned += 1
        elif boundary_checker(i + 1, j, total_rows, total_cols):
            i += 1
            fuel -= 1
            if room[i][j] == 'd':
                cleaned += 1
        else:
            return cleaned 
        
    return cleaned 


def boundary_checker(i, j, total_rows, total_cols):
    if i >= 0 and i <= total_rows - 1 and j >=0 and j <= total_cols - 1:
        return True 
    else:
        return False 

print(clean_room([['d', 'v', 'd', 'd'], ['d', 'v', 'd', 'd'], ['d', 'v', 'd', 'd']], (1,1), 3))