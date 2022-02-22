from lib import damerau_levenshtein_distance
import copy
import time


def check2(word : str, dict : str):
    #    ALFABET = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    default_dist = damerau_levenshtein_distance(word, dict)

    if default_dist != 2:
        return False  # Неправильные данные, код выхода 0

    # преоразование строки в список
    word_dict = []
    dict_dict = []
    word_dict += word
    dict_dict += dict

    # Удаление лишних букв

    min_dist = 999999
    best_word = ""
    best_temp = ""
    best_dict = ""
    for i in range(0, len(word)):
        temp = copy.copy(word_dict)
        temp[i] = ''
        string_temp = ''.join(temp)  # Преобразование массива в строку
        tmp_dist = damerau_levenshtein_distance(string_temp, dict)
        if tmp_dist < min_dist:
            best_temp = string_temp
            best_word = word
            best_dict = dict
            min_dist = tmp_dist
    #            return f"{word} 2 {string_temp} {dict}"

    # Перестанвка соседних букв

    for i in range(0, len(word) - 1):
        temp = copy.copy(word_dict)
        temp_firts_element = temp[i]
        temp[i] = temp[i + 1]
        temp[i + 1] = temp_firts_element

        string_temp = ''.join(temp)  # Преобразование массива в строку
        #        if damerau_levenshtein_distance(string_temp, dict) < default_dist:
        #            return f"{word} 2 {string_temp} {dict}"
        tmp_dist = damerau_levenshtein_distance(string_temp, dict)
        if tmp_dist < min_dist:
            best_temp = string_temp
            best_word = word
            best_dict = dict
            min_dist = tmp_dist

    # Замена букв

    len_word = len(word)
    dict_word = len(dict)
    diff = 0
    if len_word < dict_word:
        diff = dict_word - len_word
        for v in range(0, diff):
            word += " "
            word_dict += " "
    len_word = len(word)
    if len_word == dict_word:
        for i in range(0, len(word) - 1):
            if word[i] != dict[i]:
                for j in dict:
                    temp = copy.copy(word_dict)
                    temp[i] = j
                    string_temp = ''.join(temp)  # Преобразование массива в строку
                    #                if damerau_levenshtein_distance(string_temp, dict) < default_dist:
                    #                    return f"{word} 2 {string_temp} {dict}"
                    tmp_dist = damerau_levenshtein_distance(string_temp, dict)
                    if tmp_dist <= min_dist:
                        best_temp = string_temp
                        best_word = word
                        best_dict = dict
                        min_dist = tmp_dist

        word_dict = word_dict[:(diff)*-1]

        # Добавление букв
        for k in dict:
            for i in range(0, len(word)):
                temp = copy.copy(word_dict)
                temp.insert(i, k)
                string_temp = ''.join(temp)  # Преобразование массива в строку
                tmp_dist = damerau_levenshtein_distance(string_temp, dict)
                if tmp_dist <= min_dist:
                    best_temp = string_temp
                    best_word = word
                    best_dict = dict
                    min_dist = tmp_dist

    if min_dist <= default_dist:
        return f"{word} 2 {best_temp} {best_dict}"

    # Если ничего не помогло
    return None


if __name__ == '__main__':
    a = "абЫбЫ"
    b = "абоба"

    start_time = time.time()
    print(check2(a, b))
    print(time.time() - start_time)
