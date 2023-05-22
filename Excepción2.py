#Excepción2: ValueError:
def convert_to_integer(value):
    try:
        number = int(value)
        return number
    except ValueError as e:
        print("Error:", str(e))
        print("Se produjo un ValueError. El valor ingresado no es un número entero válido.")
        return None

user_input = input("Ingrese un número entero: ")
converted_number = convert_to_integer(user_input)
if converted_number is not None:
    print("El número convertido es:", converted_number)