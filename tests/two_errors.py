from lib import damerau_levenshtein_distance
import copy
import time


def check2(word, dict):
    ALFABET = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    default_dist = damerau_levenshtein_distance(word, dict)
    if default_dist != 2:
        return False  # Неправильные данные, код выхода 0

    # преоразование строки в список
    word_dict = []
    dict_dict = []
    word_dict += word
    dict_dict += dict

    # Удаление лишних букв

    for i in range(0, len(word)):
        temp = copy.copy(word_dict)
        temp[i] = ''
        string_temp = ''.join(temp)  # Преобразование массива в строку
        if damerau_levenshtein_distance(string_temp, dict) < default_dist:
            return f"{word} 2 {string_temp} {dict}"

    # Перестанвка соседних букв

    for i in range(0, len(word) - 1):
        temp = copy.copy(word_dict)
        temp_firts_element = temp[i]
        temp[i] = temp[i + 1]
        temp[i + 1] = temp_firts_element

        string_temp = ''.join(temp)  # Преобразование массива в строку
        if damerau_levenshtein_distance(string_temp, dict) < default_dist:
            return f"{word} 2 {string_temp} {dict}"

    # Замена букв

    for i in range(0, len(word) - 1):
        if word[i] != dict[i]:
            for j in dict:
                temp = copy.copy(word_dict)
                temp[i] = j
                string_temp = ''.join(temp)  # Преобразование массива в строку
                if damerau_levenshtein_distance(string_temp, dict) < default_dist:
                    return f"{word} 2 {string_temp} {dict}"

    # Если ничего не помогло
    return False


if __name__ == '__main__':
    a = "абЫбЫ"
    b = "абоба"

    start_time = time.time()
    print(check2(a, b))
    print(time.time() - start_time)
