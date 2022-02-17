import time
from fuzzywuzzy import fuzz, process

dictionary = open("dict.txt", "r").read().split("\n")
queries = open("queries.txt", "r").read().split("\n")

query = queries[0]
print("Started")


print(fuzz.ratio("абоба","абооба"))
print(fuzz.ratio("абоба","абба"))