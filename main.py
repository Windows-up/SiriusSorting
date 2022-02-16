from lib import damerau_levenshtein_distance
from twoWordTesting import check2

dictionary = open("dict.txt", "r").read().split("\n")
queries = open("queries.txt", "r").read().split("\n")

f = open("out.txt", "w+")

def main():

    for i in range(0, len(queries)):


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
            f.write(f"{word} 0 {original} \n")
            print(f"{word} 0 {original}")


        elif minimum == 2:
            f.write(check2(word, original) + "\n")
            print(check2(word,original))


        else:
            result = f"{word} {minimum} {original} \n"
            f.write(result)
            print(result)


        print(i)
        f.close()


if __name__ == "__main__":
    main()

