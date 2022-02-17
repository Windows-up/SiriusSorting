counter = 0

output = ""

queries = open("queries.txt", "r").read().split("\n")

for word in queries:
    output+= f"{word} 0\n"

with open("out.txt", "w") as file:
    file.write(output)





