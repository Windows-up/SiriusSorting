import time
from fuzzywuzzy import fuzz
from lib import damerau_levenshtein_distance
from tests.two_errors import check2

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

        minimum = -50

        if word in dictionary:
            original = word
        else:
            for original_word in dictionary:
                if abs(len(original_word)-len(word)) <= 2:
                        dist = fuzz.ratio(word, original_word)

                        #print(f"{word} {dist} {original_word}")
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
            if result == False:
                output += f"{word} 2 {original}\n"
                print(f"{counter}) {word} 2 {original}\n")
            else:
                output += f"{result}\n"
                print(f"{counter}) {result}")


        elif word_dist >=3:
            output += f"{word} 3+\n"
            print(f"{counter}) {word} 3+\n")
        print(time.time()-start_time)


with open("out2.txt", "w") as file:
    file.write(output)





