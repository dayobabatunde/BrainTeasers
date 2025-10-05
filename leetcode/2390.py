# Given a string s which contains stars (*)
# Remove the closest non-star character to its left, as well as remove the star itself

def removeStars(s: str) -> str:
    
    stack = []
    index = 0

    while index < len(s):
        char = s[index]
        if char == '*':
            stack.pop()
        else:
            stack.append(char)
        index += 1

    return ''.join(stack)

def test():
    assert removeStars("abcde") == "abcde"
    assert removeStars("abcde*") == "abcd"
    assert removeStars("a*b*c*de*") == "d"
    assert removeStars("abcde****") == "a"

    print("All tests passed")

test()