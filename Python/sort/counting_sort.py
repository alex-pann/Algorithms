def counting_sort(nums, k):
    n = len(nums)
    counters = [0]*k
    for i in range(0, n):
        counters[nums[i]]+=1
    
    ind = 0
    for i in range(0, k):
        for j in range(0, counters[i]):
            nums[ind] = i
            ind+=1 
    return nums

nums = []
k = int(input("Your array must contain n integers from 0 to k, better k <= n. Enter k :"))+1
n = int(input("Enter number of elements n : "))
for i in range(0, n):
    elem = int(input())
    nums.append(elem)  
 
print(nums) 
print(counting_sort(nums, k))