# Given integer array nums
# Return array such that each index is equal to the product of all elements in nums except the current index
# Algorithm must be o(n)

def findProduct(nums: list[int]) -> list[int]:
    wholeProduct = 1
    numZeros = 0

    for val in nums:
        if val == 0:
            numZeros += 1
        else:
            wholeProduct *= val
    
    for index, val in enumerate(nums):
        if numZeros > 0:
            if nums[index] != 0:
                nums[index] = 0
            else:
                if numZeros > 1:
                    nums[index] = 0
                else:
                    nums[index] = wholeProduct
        else:
            nums[index] = wholeProduct / val
    
    return nums

def test():
    assert findProduct([1, 2, 3]) == [6, 3, 2]
    assert findProduct([1, 1, 0, 1]) == [0, 0, 1, 0]
    assert findProduct([1, 5, 10, 1]) == [50, 10, 5, 50]
    print("All tests passed")

test()

    
