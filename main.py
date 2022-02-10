from lib import damerau_levenshtein_distance
from twoWordTesting import check2

dictionary = open("dict.txt", "r").read().split("\n")
queries = open("queries.txt", "r").read().split("\n")



def main():

    for i in range(0, len(queries)):
        file = open("out.txt", "w")

        # Find original word
        word = queries[i]
        original = dictionary[i]

        minimum = 999
        for original_word in dictionary:
            if minimum:
                dist = damerau_levenshtein_distance(word, original_word)


                if dist < minimum:
                    original = original_word
                    minimum = dist


        if minimum >= 3:
            minimum = "3+"

        if minimum == 0 :
            print(f"{word} 0 {original}")
            file.write(f"{word} 0 {original} \n")

        elif minimum == 2:
            print(check2(word,original))
            file.write(check2(word,original) + "\n")

        else:
            result = f"{word} {minimum} {original} \n"
            print(result)
            file.write(result)

        print(i)
        file.close()


if __name__ == "__main__":
    main()

