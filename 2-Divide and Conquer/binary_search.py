def binary_search(arr, left, right, number):

    mid = (left+right)//2

   

    if left == right:

        return -1

   

    while (left<right):

       

        if number == arr[mid]:

            return mid

       

        elif number < arr[mid]:

            binary_search (arr, left, mid, number)

        else:

            binary_search(arr, mid, right, number)

        

         

my_arr =  [1,4,6,7]       

index_value = binary_search(my_arr, 0, len(my_arr), 6 )

print("Index value is {}".format(index_value))