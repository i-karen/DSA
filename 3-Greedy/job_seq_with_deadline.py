 
'''
Job Sequencing with deadline
https://www.geeksforgeeks.org/job-sequencing-problem/
 
Time complexity -> O(n^2)
can be optimized using disjoint set data structure
'''
 
 
def sortThird(val):
    return val[2] 
    
def printJobScheduling(job_details, slots): 
    # Sort all jobs according to 
    # decreasing order of profit
    arr.sort(key=sortThird, reverse=True)
    # To keep track of free time slots
    result_slots = [False] * slots
 
    # To store result (Sequence of jobs)
    jobs_result = ['-1'] * slots
   
    # Iterate through all given jobs
    
    for job_detail in job_details:
        for index in range(min(slots-1, job_detail[1]-1), -1, -1):
            if result_slots[index] is False:
               result_slots[index] = True
                jobs_result[index] = job_detail[0]
                break
           
    # print the sequence
    print(jobs_result)        
    
    
 
# Driver COde
arr = [['a', 2, 100], # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]
  
  
print("Following is maximum profit sequence of jobs")
printJobScheduling(arr, 3)