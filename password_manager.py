import csv
from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""     
    with open(filename, "r") as archivo:  
        contraseña=archivo.read().strip()
    contraseña_encriptada=caesar_encrypt(contraseña)
    with open (filename, "w")as archivo:
        archivo.write(contraseña_encriptada)

 
def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    with open(filename, "r" ) as archivo: 
        l=csv.reader(archivo)
        data=[]
        for linea in l:
            if len(linea)>0:
                data.append(linea)
    for index, linea in enumerate(data):
        if index!=0:
            linea[2]=caesar_encrypt(linea[2])
    with open(filename, "w") as archivo:
        escritor=csv. writer(archivo)
        escritor.writerows(data)


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    data=[]
    encontrado=False
    with open(filename, "r") as archivo:
        lector=csv.reader(archivo)
        for linea in lector:
            if len(linea) >0:
                if linea[0]==website:
                    linea[2]=caesar_encrypt(password)
                    encontrado=True
                data.append(linea)
    if encontrado== False:
        return False
    with open(filename, "w", newline='') as archivo:
        escritor=csv.writer(archivo)
        escritor.writerows(data)
        return 

def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass


if __name__ == "_main_":
    encrypt_single_pass('example1.txt')
    encrypt_passwords_in_file('examples/example2.csv')
    change_password("example3.csv", "nonexistent.com", "randompass")