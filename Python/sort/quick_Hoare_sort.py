def partition_Hoare(nums, left, right):
    p_val = nums[(left+right)//2]          # set median element as pivot
    i = left        # first index
    j = right       # last index
    while (i < j):         
        while (nums[i] < p_val): # increment i until element i > pivot
            i+=1
        while (nums[j] > p_val): # decrement j while element j < pivot
            j-=1
        if (i>j): # in that case the subarray is alredy in order
            break
        nums[i], nums[j] = nums[j], nums[i]  # otherwise - swap elements < and > pivot
        i+=1 # to adjust the border between < and >
    return i              # index of the first element > pivot
    
def quick_Hoare_sort(nums, left, right):
    if (left >= right):
        return              # so we stop the recursion
    pivot = partition_Hoare(nums, left, right)
    quick_Hoare_sort(nums, left, pivot-1)
    quick_Hoare_sort(nums, pivot, right)
    return nums


nums = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    elem = int(input())
    nums.append(elem)

print(nums) 
print(quick_Hoare_sort(nums, 0, n-1))