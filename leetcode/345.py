# we have a string s that consist only of printable ASCII characters (no spaces)

# We need to reverse only the vowels: a, e, i, o, u (lower or uppercase)

def reverseVowels(s: str) -> str:
    sArray = list(s)
    print(sArray)
    vowels = set(['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'])

    indexFront = 0
    indexBack = len(sArray) - 1

    while indexFront < indexBack:
        if not sArray[indexFront] in vowels:
            indexFront += 1
        
        if not sArray[indexBack] in vowels:
            indexBack -= 1
        
        if sArray[indexFront] in vowels and sArray[indexBack] in vowels:
            intermediate = sArray[indexFront]
            sArray[indexFront] = sArray[indexBack]
            sArray[indexBack] = intermediate

            indexFront += 1
            indexBack -= 1
        
    return ''.join(sArray)
    
def test():
    assert reverseVowels("i") == "i"
    assert reverseVowels("wwiwE") == "wwEwi"
    assert reverseVowels("awwiwE") == "Ewwiwa"
    print("All tests passed")
    
test()
        
