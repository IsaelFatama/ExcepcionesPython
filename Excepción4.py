my_dict = {'a': 1, 'b': 2}

try:
    value = my_dict['c']
    print(value)
except KeyError:
    print("La clave 'c' no existe en el diccionario.")
