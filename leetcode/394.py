def decode(s: str) -> str:
    stringStack = []
    string = []
    numberStack = []
    digits = set("123456789")

    for char in s:
        if char in digits:
            numberStack.append(int(char))
        elif char == "]":

            extendedString = []

            print(string)
            print(numberStack)

            for _ in range(numberStack.pop()):
                extendedString.extend(string)

            print(extendedString)

            if stringStack:
                previous = stringStack.pop()
                previous.extend(extendedString)
                extendedString = previous

            stringStack.append(extendedString)
            string = extendedString

        elif char == "[":
            if string:
                stringStack.append(string.copy())
                string.clear()
        else:
            string.append(char)

    print(stringStack)
        
    return "".join(stringStack.pop())

def test():
    # assert decode("3[a]") == "aaa"
    assert decode("3[a2[b]]") == "abbabbabb"

    print("All tests passed")

test()


