def find_first_occurrence(string, letter):
    try:
        index = string.index(letter) + 1 
        return index
    except ValueError:
        return 0


word = input("Введіть слово: ")
letter = input("Введіть літеру: ")

word_leter = find_first_occurrence(word, letter)
print(word_leter)
