#assignment 1

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:

        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

value = ["Alex", "John", "Mary", "Steve", "John", "Steve"]
result = remove_duplicates(value)
print(result)


#assignment2
print(max(value))

#assignment3
print(min(value))


#assignment4
k = 0
rows = 10
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k != (2*i-1):
        print("* ", end="")
        k = k + 1
    k = 0
    print()
