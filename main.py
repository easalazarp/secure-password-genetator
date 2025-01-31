import secrets
import string


print("*** Bienvedino al Generador de contraseñas seguras ***")
print("Por favor ingrese la longitud con un mínimo de 8 y máximo 16 caracteres")
length = int(input("Longitud: "))
print("¿Qué caracteres desea agregar?")
print("(1) Números (2) Caracteres especiales (3) Números y caracteres especiales")
character = int(input("Ingrese una opción: "))

# Proceso
letters = string.ascii_letters

match character:
    case 1:
        letters += string.digits
    case 2:
        letters += string.punctuation
    case 3:
        letters += string.digits + string.punctuation
    case _:
        print("Ingrese una opción válida")
secure_password = ''.join(secrets.choice(letters) for _ in range(length))
print(f"Contraseña segura: {secure_password}")


