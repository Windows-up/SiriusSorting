import time
from fuzzywuzzy import fuzz
from rapidfuzz.distance import Indel

from lib import damerau_levenshtein_distance
from tests.two_errors_test import check2

counter = 0

output = ""

dictionary = open("dict.txt", "r").read().split("\n")
queries = open("queries.txt", "r").read().split("\n")

for word in queries:
        start_time = time.time()
        counter += 1


        # Find origindwdwdwdwdwd
        # word = queries[10]
        original = dictionary[0]

#        minimum = -50
        minimum = 0

        if word in dictionary:
            original = word
        else:
            minimum = 0
            for original_word in dictionary:
                if abs(len(original_word)-len(word)) <= 2:
                        dist = Indel.normalized_similarity(word, original_word, score_cutoff=0.6) * 100
                        if dist > minimum:
                            original = original_word
                            minimum = dist


        word_dist = damerau_levenshtein_distance(word,original)

        if word_dist == 0:
            output += f"{word} 0\n"
            print(f"{counter}) {word} 0\n")
        elif word_dist == 1:
            output += f"{word} 1 {original}\n"
            print(f"{counter}) {word} 1 {original}\n")
        elif word_dist == 2:
            result = check2(word,original)
            if result is None:
                output += f"{word} 2 {original}\n"
                print(f"{counter}) {word} 2 {original}\n")
            else:
                output += f"{result}\n"
                print(f"{counter}) {result}")
        elif word_dist >=3:
            output += f"{word} 3+\n"
            print(f"{counter}) {word} 3+\n")
#        print(time.time()-start_time)


with open("out_test.txt", "w") as file:
    file.write(output)





