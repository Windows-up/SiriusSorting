import copy

from lib import damerau_levenshtein_distance


a = "абЫобаЫ"
b = "абоба"

# Ver 1.0 Удаление лишних букв
#
#
#
#
#
#
#
#
def check2(word,dict):
    default_dist = damerau_levenshtein_distance(word,dict)
    if default_dist != 2:
        return False # Неправильные данные, код выхода 0

    #преоразование строки в список
    word_dict = []
    dict_dict = []
    word_dict += word
    dict_dict += dict

    #Удаление лишних букв
    for i in range(0,len(word)):
        temp = copy.copy(word_dict)
        temp[i] = ''
        string_temp = ''.join(temp) #Преобразование массива в строку
        print(string_temp)
        if damerau_levenshtein_distance(string_temp,dict) < default_dist:
            return f"{word} 2 {string_temp} {dict}"



print(check2(a,b))