
def solve(num_projects, curr_level, increase_lst, min_lvl_lst):

    new_lst = [[increase_lst[i], min_lvl_lst[i]] for i in range(len(increase_lst))]

    new_lst = sorted(new_lst, key=lambda x: x[0], reverse=True)
    print(new_lst)
    i = 0
    while(num_projects > 0):
        if (curr_level >= new_lst[i][1]):
            num_projects -= 1
            curr_level += new_lst[i][0]
            new_lst[i][0], new_lst[i][1] = 0, 0
            new_lst.remove(new_lst[i])
        i += 1
        if i == len(new_lst):
            i = 0

    
    return curr_level





if __name__ == "__main__":
    increase_lst =  [100,6,7]
    min_lvl_lst = [5,3,0]
    print(solve(2, 0, increase_lst, min_lvl_lst))