#Given an array of ints, return the number of 9's in the array.

def num9inArray(nums):
    count = 0

    for i in range(len(nums)):
        if nums[i] == 9:
            count += 1
    return count


print(num9inArray([15, 9,9,0,9,1,8,7,9,10]))