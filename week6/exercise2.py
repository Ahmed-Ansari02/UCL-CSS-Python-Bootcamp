#["ahmed", "abdullah", "wira"]

def countString(strings):
    newList = []
    length = len(strings)
    print(length)
    for i in range(len(strings)):
        
        string = strings[i]
        print(f"{i}: {string}")
        if len(string) >= 4:
            newList.append(string)
    return newList

input = ["Abdullah", "Ahmed", "Hello world", "Vegetable", "1234"]
output = countString(input)
print(output)