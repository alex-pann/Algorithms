def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):

        # binary search by answer for the minimal element in unsorted part
        left = -1
        right = i
        while (right-left > 1):
            mid = int((right + left)/2)
            if nums[mid] >= nums[i]:
                right = mid
            else:
                left = mid
        j = i  

        # put the found element to the right place in sorted part
        while j > right:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums


nums = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    elem = int(input())
    nums.append(elem)
 
print(nums) 
print(insertion_sort(nums))