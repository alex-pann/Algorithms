def index_min(nums):
    n = len(nums)
    i_min = 0
    for i in range (1, n):
        if nums[i] < nums[i_min]:
            i_min = i
    return i_min

def selection_sort(nums):
    n = len(nums)
    for i in range(0, n-1):
        i_min = index_min(nums[i:n])
        nums[i], nums[i+i_min] =  nums[i+i_min], nums[i]
    return nums


nums = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    elem = int(input())
    nums.append(elem)  
 
print(nums) 
print(selection_sort(nums))