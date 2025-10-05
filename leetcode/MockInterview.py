# array of numbers (nums)
# find a number in the array, if the array is sorted

def findNum(nums, target):
    
    if not nums:
        return -1 
    
    front = 0
    end = len(nums) - 1

    while front <= end:

        middle = (front + end) // 2

        if nums[middle] < target:
            front = middle + 1
        elif nums[middle] > target:
            end = middle - 1
        else:
            return middle    
    
    return -1

def test():
    #assert findNum([1, 2, 8, 9], 8) == 2
    #assert findNum([], 8) == -1
    #assert findNum([1, 2, 8, 9], 3) == -1
    assert findNum([9, 8, 2, 1], 1) == -1 
    assert findNum([8, 9, 1, 2], 1)
    print("All tests passed")

test()
