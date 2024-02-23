def longer_string(str1, str2):
    word1 = len(str1)
    word2 = len(str2)

    if word1 > word2:
        return str1
    elif word2 > word1:
        return str2
    else:
        return "equally"


input_str1 = input("Введіть перший рядок: ")
input_str2 = input("Введіть другий рядок: ")

result = longer_string(input_str1, input_str2)

print(result)
