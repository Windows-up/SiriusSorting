import difflib



a = "прээет"
b = "привет"

cases = [(a, b)]

position = 0

for a, b in cases:
    operations = []
    print('{} => {} \n'.format(a, b))
    for i, s in enumerate(difflib.ndiff(a, b)):
        res = ""
        if s[0] == ' ':
            continue
        elif s[0] == '-':
            res = f'Delete "{s[-1]}" from position {i}'
            operations.append(["-",s[-1],i])
            position += 1

        elif s[0] == '+':
            res = f'Add "{s[-1]}" to position {i}'
            operations.append(["+", s[-1], i])



        #print(res)

#print(*operations)
last_operation = [0,0,0]

massive = []
for i in a:
    massive.append(i)
#print(massive)

itr = []
itog = ""
for operation in operations:
    if last_operation[0] == "-" and last_operation[2] == operation[2] - 1 :
        itr.append(['/',operation[1],operation[2]])
        # massive[operation[2]-position] = operation[1]
        # print(massive)
    last_operation = operation
    #print(itr[-1:])
    itog = ['/',operation[1],operation[2]]
    #print(f"itog = {itog}")

#print(itog)
massive[itog[2]-position] = itog[1]
print(*a)
print(*massive)
print(*b)


