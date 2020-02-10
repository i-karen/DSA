'''

Merge sort recursive - O(log n)

Merge sort iterative - O(n)

iterative
http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/7-Sort/merge-sort5.html


most appropriate to my debug
https://stackoverflow.com/questions/19085450/merge-sort-in-place-for-python-cant-find-what-is-wrong
'''

def merge(arr, left, mid, right):
    L = arr[left:mid]
    R = arr[mid:right]
    i = 0
    j = 0
    k = left
    # import pdb; pdb.set_trace()
    while (i<len(L) and j<len(R)):

        if L[i]<R[j]:
            arr[k] = L[i]

            i +=1

        else:

            arr[k] = R[j]
            j +=1
        k +=1

   
    while (i<len(L)):
        arr[k] = L[i]
        i +=1
        k +=1
    while (j<len(R)):
        arr[k] = R[j]
        j +=1
        k +=1    
       
def merge_sort(arr, left, right):
    mid = (left+right)//2

    if len(arr)==1:
        return arr

    if(right-left>1):
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        # import pdb; pdb.set_trace()
       
        merge(arr, left, mid, right)
       
arr = [1, 9, 5 , 4, 7 , 8, 2, 6]

merge_sort(arr, 0, len(arr))
print(arr)