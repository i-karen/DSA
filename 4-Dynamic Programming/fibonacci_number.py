def fibonacci_recursion(number):
    if number <= 1:
        return number
    else:
        result = fibonacci_recursion(number - 2) + fibonacci_recursion(number -
                                                                       1)
        return result


def fibonacci_dp(number):
    arr = [0, 1]
    if number <= 1:
        return number
    for i in range(2, number):
        import pdb
        pdb.set_trace()
        arr[i] = arr[i - 2] + arr[i - 1]
    return arr[number]


print(fibonacci_dp(6))