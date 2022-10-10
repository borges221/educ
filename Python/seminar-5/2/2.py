# Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах


with open('textForRLECode.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Write the text needed for compression: '))
with open('textForRLECode.txt', 'r') as file:
    text = file.readline()
    textCompres = text.split()

print(text)


def rle_encode(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding


textCompres = rle_encode(text)

with open('textRLECode.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{textCompres}')
print(textCompres)