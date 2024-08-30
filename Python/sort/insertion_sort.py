def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        j = i-1
        while (nums[j] > nums[j+1] and j >= 0) :
            nums[j+1], nums[j] =  nums[j], nums[j+1]
            j -= 1  
    return nums


nums = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    elem = int(input())
    nums.append(elem)
 
print(nums) 
print(insertion_sort(nums))