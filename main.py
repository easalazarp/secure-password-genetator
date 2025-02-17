import secrets
import string
print("*** Bienvenido al Generador de contraseñas seguras ***")

# Validar que se ingrese una loginitud correcta
def password_length():
    length = 0
    while True:
        try:
            print("Por favor ingrese la longitud con un mínimo de 8 y máximo 16 caracteres")
            length = int(input("Longitud: "))
            if 8 <= length <= 16:
                break
            else:
                print("*** Ingrese una número entre 8 a 16 ***")
        except ValueError:
            print("*** Ingrese un número entre 8 a 16 ***")

    return length

# Validar que solo se puedan agregar opciones disponibles
def add_characters():
    character = 0
    while True:
        try:
            print("¿Qué caracteres desea agregar?")
            print("(1) Números (2) Caracteres especiales (3) Números y caracteres especiales")
            character = int(input("Ingrese una opción: "))
            if 1 <= character <= 3:
                break
            else:
                print("*** Debe seleccionar al menos una opción válida ***")
        except ValueError:
            print("*** Ingrese una opción válida ***")
    return character


def password_generator():
    letters = string.ascii_letters
    length = password_length()
    character = add_characters()

    match character:
        case 1:
            letters += string.digits
        case 2:
            letters += string.punctuation
        case 3:
            letters += string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(letters) for _ in range(length))
    print(f"Contraseña segura: {secure_password}")
    print("**********************************************************************")

def processed_password():
    except_activated = False
    # Controla si el usuario requiere regenerar nuevamente una contraseña
    while True:
        try:
            # except_activated  controla que solo llama a esta función cuando ingrese
            # por primer vez o cuando el usuario quiere generar otra contraseña
            if not except_activated:
                password_generator()
            print("Desea generar otra contraseña:")
            print("(1) Generarar otra contraseña (0) Salir")
            option = int(input("Ingrese una opción: "))
            if  option == 0:
                break
            elif option == 1:
                except_activated = False
                continue
            else:
                print("**** Ingrese una opción válida ****")
                except_activated = True
        except ValueError:
            print("*** Ingrese una opción válida ***")
            except_activated = True

if __name__ == "__main__":
    processed_password()
