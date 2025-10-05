# Integer array candies (candies)
# Integer that represents extra candy (extraCandies)
# return boolean array (result) of length n

# For each index determine if it will have the max value after extraCandies is added to the value at that index

def maxCandies(candies: list[int], extraCandies: int) -> list[bool]:
    maxCandy = max(candies)
    result = []

    for numCandies in candies:
        result.append(numCandies + extraCandies >= maxCandy)
    
    return result

def test():
    assert maxCandies([5, 10, 4], 5) == [True, True, False]
    assert maxCandies([1, 10, 1 ], 1) == [False, True, False]
    print("All tests passed")

test()


