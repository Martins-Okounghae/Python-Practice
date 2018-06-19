#Given an array of ints,
# return True if one of the first 4 elements in the array is a 9.
#The array length may be less than 4.

def num9_found(nums):
    lent = len(nums)

    if lent > 4:
        lent = 4


    for i in range(lent):
        if nums[i]== 9:
            print("Number 9 was found in the array")
            return True
    print("Number 9 wasn't found in the array")
    return False


print(num9_found([1,2,3,9]))

