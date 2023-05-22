#Excepción 3: IndexError
def get_element_by_index(lst, index):
    try:
        return lst[index]
    except IndexError as e:
        print("Error:", str(e))
        print("Se produjo un IndexError. El índice está fuera del rango de la lista.")
        return None

my_list = [1, 2, 3]
index = 3
result = get_element_by_index(my_list, index)
if result is not None:
    print("El elemento en el índice", index, "es:", result)