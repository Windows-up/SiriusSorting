from lib import *

dictionary = open("dict.txt", "r").read().split("\n")
queries = open("queries.txt", "r").read().split("\n")


def main():

    for i in range(0, len(queries)):

        # Find original word
        word = queries[i]
        original = dictionary[i]

        minimum = 999
        for original_word in dictionary:

            dist = damerau_levenshtein_distance(word, original_word)
            if dist < minimum:
                original = original_word
                minimum = dist

        check = check2(word, original)

        if minimum >= 3:
            minimum = "3+"

        elif minimum == 0 and check:
            print(check)

        else:
            result = f"{word} {minimum} {original}"
            print(result)


if __name__ == "__main__":
    main()
