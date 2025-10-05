# Given binary array (flowerbed) - 0 = empty; 1 = flower
# n number of flowers to be placed
# flowers cannot not be placed next to each other
# return boolean that represents if amount of lfowers can be placed

# Determine if given amount of flowers can be placed in a flowerbed

def determinePlant(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True
    
    for index, spot in enumerate(flowerbed):
        if spot == 0:
            if index == 0 and index == len(flowerbed) - 1:
                flowerbed[index] = 1
                n -= 1
            elif index == 0:
                if flowerbed[index + 1] == 0:
                    flowerbed[index] = 1
                    n -= 1
            elif index == len(flowerbed) - 1:
                if flowerbed[index - 1] == 0:
                    flowerbed[index] = 1
                    n -= 1
            else:
                if flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0:
                    flowerbed[index] = 1
                    n -= 1
            
            if n == 0:
                return True
    
    return False

def test():
    assert determinePlant([1], 1) == False
    assert determinePlant([0], 1) == True
    assert determinePlant([0, 0, 1], 1) == True
    assert determinePlant([0, 1, 0, 0, 0], 1) == True
    assert determinePlant([0, 1, 0, 0, 1], 1) == False
    assert determinePlant([0, 1, 1, 0, 0], 1) == True
    assert determinePlant([0, 1, 1, 0, 0], 2) == False
    print("All tests passed")

test()

