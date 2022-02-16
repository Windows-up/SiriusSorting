import time
import enchant
from lib import damerau_levenshtein_distance

output = ""

#
# def checkTrue(words):
#     dicts = enchant.Dict("ru_RU")
#     suggestions = dicts.suggest(words)
#     if len(suggestions) != 0:
#         return suggestions[0]
#     else:
#         return "ERR"
#
#
dictionary = open("dict.txt", "r").read().split("\n")
queries = open("queries.txt", "r").read().split("\n")
#
# start = time.time()
#
# for word in range(0, len(queries)):
#
#     if queries[word] in dictionary:
#         print(f"{queries[word]} 0  {word}")
#         output += f"{queries[word]} 0  {word} \n"
#     else:
#         temp = checkTrue(queries[word])
#         if temp in dictionary:
#             dist = damerau_levenshtein_distance(queries[word], temp)
#             if dist >= 3:
#                 print(f"{queries[word]} 3+")
#                 output += f"{queries[word]} 3+ \n"
#             else:
#                 print(f"{queries[word]} {dist} {temp} {word}")
#                 output += f"{queries[word]} {dist} {temp} \n"
#         else:
#             print(f"{queries[word]} 3+ {word}")
#             output += f"{queries[word]} 3+ \n"
#
# end = time.time()
# print(end - start)

for i in queries:
    print(f"{i} 0\n")
    output+= f"{i} 0\n"
with open("out.txt", "w") as file:
    file.write(output)
