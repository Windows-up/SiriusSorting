dictionary = open("dict.txt", "r").read().split("\n")
queries = open("queries.txt", "r").read().split("\n")

output = ""


for i in range(0, len(queries)):
    output += f"{queries[i]} 0\n"


