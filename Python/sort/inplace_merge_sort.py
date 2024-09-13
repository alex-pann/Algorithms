class SizeError(Exception):
    pass

def lower_bound(array, x):  # return index of the first element >= x in array 
    i = 0
    while (array[i] < x and i < len(array)-1):
        i+=1
    return i

def reverse(array): # change the order of array elements to reveced
    n = len(array)
    for i in range(0, n//2):
        array[i], array[n-i-1] = array[n-i-1], array[i]
    return array

def rotate(array, na, nb): # swap two parts the array with na and nb sizes  (different lenght, without using extra space)
    try:
        if (na + nb != len(array)):
            raise SizeError()
        array = reverse(array)
        array[0:nb] = reverse(array[0:nb])
        array[nb:(na+nb)] = reverse(array[nb:(na+nb)])
        return array
    except SizeError:
        print("Error: Subarray sizes must fit the whole array")
        print(array, na, nb)

def inplace_merge(array, na, nb):
    # A = array[0:na]
    # B = array[na:na+nb]

    # assert (na + nb == len(array)), "Parts sizes must fit the whole array"

    if (na == 0 or nb == 0):
        return array
    if (na == 1 and nb == 1):
        if (array[0]>array[1]):
            array[0], array[1] = array[1], array[0]
            return array
        else:
            return (array)

    if (nb >= na):
        rotate(array, na, nb)
        na, nb = nb, na 

    x = array[na//2]
    j = lower_bound(array[na:na+nb], x)
    rotate(array[(na//2):(na+j+1)], na//2, j+1)
    inplace_merge(array[0:(na//2 + j+1)], na//2, j+1)
    inplace_merge(array[(na//2 + j+1):na+nb], na//2, nb-j-1)

    return array



def merge_sort(nums):
    n = len(nums)
    i = 1
    while i < n: # i refers to the size of pieces that will be merged on current step
        for j in range(0, n-i, 2*i): # j points to the first element of first of merging piece
            temp = inplace_merge(nums[j:min(j+2*i, n)], i, min(j+2*i, n) - i)
            nums[j:min(j+2*i, n)] = temp
        i*=2
    return nums


# nums = []
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#     elem = int(input())
#     nums.append(elem)
 
# print(nums) 
# print(merge_sort(nums))

# a = [1, 3, 5, 6, 7, 9, 0, 2, 4, 6]
a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
inplace_merge(a, 6, 4)
print(a)



# a = [0, 2, 4, 6]
# print(lower_bound(a, 6))