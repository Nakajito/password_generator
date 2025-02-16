import random
import string

def password_generator(length):
    """
    Genera una contraseña segura de longitud especificada.

    Args:
        length (int): La longitud de la contraseña a generar.

    Returns:
        str: Una contraseña generada aleatoriamente con letras, números y caracteres especiales.
    """
    
    symbols = "!@#$%^&*()_+"
    
    password = ''
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + symbols)
    return password


try:
    length = int(input('Ingresa la longitud de la contraseña (Se recomienda mayor a 8 caracteres): '))
    if length < 1:
        raise ValueError('La longitud debe ser mayor a 0.')
    else:
        print(password_generator(length))
        
except ValueError as e:
    print(f'Error: {e}')