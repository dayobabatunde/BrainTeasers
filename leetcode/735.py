# Given array of integers asteroids
# if two asteroids meet, the smaller explodes
# if both are the same size they both explode
# two asteroids moving in the same direction (same sign) will never meet

def collide(asteroids: list[int]) -> list[int]:
    stack = []
    index = 0

    while index < len(asteroids):
        if not stack:
            stack.append(asteroids[index])
            index += 1
        else:
            if asteroids[index] < 0 and stack[len(stack) - 1] > 0:
                if -asteroids[index] > stack[len(stack) - 1]:
                    stack.pop()
                elif -asteroids[index] == stack[len(stack) - 1]:
                    stack.pop()
                    index += 1
                else:
                    index += 1
            else:
                stack.append(asteroids[index])
                index += 1
  
    return stack

def test():
    assert collide([1, 2, -1]) == [1, 2]
    assert collide([1, 2, -5]) == [-5]
    assert collide([1000, -1000]) == []
    assert collide([1, 10, 3, -5, -20, 1]) == [-20, 1]
    print("All tests passed")

test()


