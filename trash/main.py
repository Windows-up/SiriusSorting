import time
from numba import njit
from lib import damerau_levenshtein_distance


dictionary = open("dict.txt", "r").read().split("\n")
queries = open("queries.txt", "r").read().split("\n")

# f = open("out.txt", "w+")

def main():

    for i in range(0, len(queries)):
        start_time = time.time()


        # Find original word
        word = queries[i]
        original = dictionary[i]

        minimum = 999
        for original_word in dictionary:
            if minimum:
                if abs(len(word) - len(original_word)) <=2:
                    dist = damerau_levenshtein_distance(word, original_word)


                    if dist < minimum:
                        original = original_word
                        minimum = dist


        if minimum >= 3:
            minimum = "3+"

        if minimum == 0 :
            print(f"{word} 0 {original}")


        elif minimum == 2:
            # f.write(check2(word, original) + "\n")
            print(f"{word} 2 {original}")


        else:
            result = f"{word} {minimum} {original} \n"
            print(result)


        print(i)
        print(time.time()-start_time)


if __name__ == "__main__":
    main()

