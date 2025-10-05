# Given s, reverse order of words (words will be separated by a space)
# Return a string
# s can contain leading and trailing whitespace
# there should not be any leading or trailing whitespace in output

def reverseWords(s: str) -> str:
    wordArray = s.split()
    print(wordArray)

    front = 0
    back = len(wordArray) - 1

    while front < back:
        wordArray[front], wordArray[back] = wordArray[back], wordArray[front]
        front += 1
        back -= 1
    
    return ' '.join(wordArray)

def test():
    assert reverseWords("I Like Water") ==  "Water Like I"
    assert reverseWords("    I    Like  Water    ") ==  "Water Like I"
    assert reverseWords("I   Like  A  Water  ") ==  "Water A Like I"
    print("All tests passed")

test()