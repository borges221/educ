# Напишите программу,
#  удаляющую из текста все слова, 
#  содержащие "абв". 
#  В тексте используется разделитель пробел.

text = input("Enter text separated by a space:\n")

def DelText(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)


text = DelText(text)
if len(text) == 0:
    print("All deleted or nothing entered! ")
print(text)