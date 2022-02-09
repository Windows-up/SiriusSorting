import difflib

a = "приэет"
b = "привет"

cases = [(a, b)]

for a, b in cases:
    print('{} => {} \n'.format(a, b))
    for i, s in enumerate(difflib.ndiff(a, b)):
        operation = ""
        if s[0] == ' ':
            continue
        elif s[0] == '-':
            operation = f'Delete "{s[-1]}" from position {i}'

        elif s[0] == '+':
            operation = f'Add "{s[-1]}" to position {i}'



        print(operation)
