def merge(A, B):
    C = [0]*(len(A)+len(B))
    ia, ib = 0, 0
    while (ia < len(A) and ib < len(B)):
        if (B[ib] < A[ia]):
            C[ia+ib] = B[ib]
            ib += 1
        else:
            C[ia+ib] = A[ia]
            ia += 1
    while (ia < len(A)):
        C[ia+ib] = A[ia]
        ia += 1
    while (ib < len(B)):
        C[ia+ib] = B[ib]
        ib += 1
    return C

def merge_sort(nums):
    n = len(nums)
    i = 1
    while i < n: # i refers to the size of pieces that will be merged on current step
        for j in range(0, n-i, 2*i): # j points to the first element of first of merging piece
            temp = merge(nums[j:j+i], nums[j+i:min(j+2*i, n)])
            nums[j:min(j+2*i, n)] = temp
        i*=2
    return nums


nums = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    elem = int(input())
    nums.append(elem)
 
print(nums) 
print(merge_sort(nums))