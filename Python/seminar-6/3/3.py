# Написать функцию, 
# аргументы имена сотрудников, 
# возвращает словарь, 
# ключи — первые буквы имён, 
# значения — списки, содержащие имена, 
# начинающиеся с соответствующей буквы.

def thesaurus(names):
    res = {}
    for name in names:
        key = name[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res

names = input("Enter names separated by spaces: ").split()
names.sort(key=lambda x: x.lower())
print(thesaurus(names))