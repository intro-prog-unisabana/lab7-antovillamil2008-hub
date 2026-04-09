import csv
from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""     
    with open(filename, "r") as archivo:  
        contraseña=archivo.read().strip()
    constraseña_encriptada=caesar_encrypt(contraseña)
    with open (filename, "w")as archivo:
        archivo.write(constraseña_encriptada)

 
    

def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    with open(filename, "r" ) as archivo: 
        for linea in archivo: 
            print(linea)


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass

encrypt_single_pass('example1.txt')

encrypt_passwords_in_file('examples/example2.csv')