
def get_comb(curr_list, remaining_item, n):
    if len(curr_list) == n:
        print(curr_list)
        return
    else:
        for i in range(0,len(remaining_item)):
            temp_curr = curr_list.copy()
            temp_curr.append(remaining_item[i])
            temp_rem = remaining_item.copy()
            temp_rem.remove(remaining_item[i])
            get_comb(temp_curr, temp_rem, n)

def initial_run(n):
    initial_list = []
    for i in range(1, n+ 1):
        initial_list.append(i)
    get_comb([], initial_list, n)

res = initial_run(5)
print(len(res))
