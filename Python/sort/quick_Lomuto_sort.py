def partition_Lomuto(nums, left, right):
    p_val = nums[right]          # set last element as pivot
    p_ptr = left                 # first element larger than pivot (border)
    for i in range(left, right): # going through the array
        if nums[i] < p_val:      # if a new element is less than pivot, we swap it with element on the boarder (p_ptr)
            nums[p_ptr], nums[i] = nums[i], nums[p_ptr]
            p_ptr+=1           
    nums[p_ptr], nums[right] = nums[right], nums[p_ptr] # finally, we put the pivot element on the boarder  
    return p_ptr

def quick_Lomuto_sort(nums, left, right):
    if (left >= right):
        return              # so we stop the recursion
    pivot = partition_Lomuto(nums, left, right)
    quick_Lomuto_sort(nums, left, pivot-1)
    quick_Lomuto_sort(nums, pivot+1, right)
    return nums


nums = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    elem = int(input())
    nums.append(elem)
 
print(nums) 
print(quick_Lomuto_sort(nums, 0, n-1))