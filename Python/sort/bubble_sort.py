def simple_bubble_sort(nums):
    n = len(nums)
    for i in range(0, n):
        for j in range(0, n-1):
            if (nums[j]>nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


# improved algorithm:
# 1) after i-iteration no need to compare elements > i -- that part is already sorted
# 2) if after i-iteration no swaps were made -- the array is already sorted
def bubble_sort(nums):
    n = len(nums)
    i = 0
    is_swapped = True
    while (is_swapped):
        is_swapped = False
        for j in range(0, n-i-1):
            if (nums[j]>nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swapped = True
        i += 1
    return nums


nums = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    elem = int(input())
    nums.append(elem)
 
print(nums) 
print(bubble_sort(nums))