'''
0/1 knapsack
 
'''
val = [60, 100, 120]
wt = [10, 20, 30]


def knapsack_recursive_decrement(capacity, current_item):
    '''
    n-1 to 0
    @param capacity
    @param current item number
   
    If item is  selected its value is chosen and added to the recursive process with the subsequent items and modifidying the total capcity
    If item not selected the recursive process is continued without modifying total capacity
    '''
    if current_item == 0 or capacity == 0:
        return 0
    if wt[current_item - 1] > capacity:
        return knapsack_recursive_decrement(capacity, current_item - 1)
    else:
        ans1 = val[current_item - 1] + knapsack_recursive_decrement(
            capacity - wt[current_item - 1], current_item - 1)
        ans2 = knapsack_recursive_decrement(capacity, current_item - 1)
        return max(ans1, ans2)


W = 50
n = len(val)
print(knapsack_recursive_decrement(W, n))


def knapsack_recursive_increment(capacity, current_item):
    '''
    0 to n
    @param capacity
    @param current item number
   
    If item is  selected its value is chosen and added to the recursive process with the subsequent items and modifidying the total capcity
    If item not selected the recursive process is continued without modifying total capacity
    '''
    if current_item >= len(val) or capacity == 0:
        return 0
    if wt[current_item] > capacity:
        return knapsack_recursive_increment(capacity, current_item + 1)
    else:
        ans1 = val[current_item] + knapsack_recursive_increment(
            capacity - wt[current_item], current_item + 1)
        ans2 = knapsack_recursive_increment(capacity, current_item + 1)
        return max(ans1, ans2)


W = 50
# n = len(val)
print(knapsack_recursive_increment(W, 0))


def knapsack_dp(capacity, item_size):
    '''
    @param capacity
    @param current item number
    '''
    k = [[0 for x in range(item_size + 1)] for x in range(capacity + 1)]
    for cur_capacity in range(capacity + 1):
        for cur_item in range(item_size + 1):
            if cur_item == 0 or cur_capacity == 0:
                k[cur_capacity][cur_item] = 0
            elif wt[cur_item - 1] > cur_capacity:
                k[cur_capacity][cur_item] = k[cur_capacity][cur_item - 1]
            else:
                k[cur_capacity][cur_item] = max(
                    k[cur_capacity][cur_item - 1], val[cur_item - 1] +
                    k[cur_capacity - wt[cur_item - 1]][cur_item - 1])
    return k[capacity][item_size]


W = 50
n = len(val)
print(knapsack_dp(W, n))
