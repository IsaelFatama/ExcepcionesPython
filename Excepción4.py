#Excepción 4: KeyError
def get_value_by_key(dictionary, key):
    try:
        return dictionary[key]
    except KeyError as e:
        print("Error:", str(e))
        print("Se produjo un KeyError. La clave no existe en el diccionario.")
        return None

my_dict = {'a': 1, 'b': 2}
key = 'c'
result = get_value_by_key(my_dict, key)
if result is not None:
    print("El valor asociado con la clave", key, "es:", result)