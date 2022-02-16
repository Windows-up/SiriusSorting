from numba import njit
from fuzzywuzzy import fuzz

@njit(fastmath=True)
def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # deletion
                d[(i, j - 1)] + 1,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + 1)  # transposition

    return d[lenstr1 - 1, lenstr2 - 1]


output = ""
counter = 0

dictionary = open("universities.txt", "r").read().split("\n")
queries = open("queries.txt", "r").read().split("\n")

for i in queries:
    counter += 1
    mininum = -50
    original = []
    for j in dictionary:
        fix_i = i.lower()
        fix_j = j.lower()
        split_i = fix_i.split()
        split_j = fix_j.split()


        if split_j[0][0] == split_i[0][0]:

            dist = fuzz.ratio(fix_i, fix_j)

            if dist > mininum:
                original.append(j)
                mininum = dist

    mininum = 999999
    good_word = ""
    for b in original:
        lower_b = b.lower()
        dist = damerau_levenshtein_distance(fix_i, lower_b)

        if dist < mininum:
            good_word = b
            mininum = dist
    print([i, good_word,mininum, counter])
    output += f"{good_word}\n"

with open("out.txt", "w") as file:
    file.write(output)
