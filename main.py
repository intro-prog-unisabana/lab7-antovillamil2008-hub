from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""
    filename= input("Enter the CSV file name:")
    encrypt_passwords_in_file(filename)
    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        opcion=input().strip()
        if opcion=="1":
            datos=input("Enter the website and the new password:").split()
            if len(datos)<2:
                print("Input is in the wrong format!")
            elif len(datos[1]) < 12:
                print("Password is too short!")
            else:
                exito = change_password(filename, datos[0], datos[1])
                if exito:
                    print("Password changed.")
                else:
                    print("Website not found! Operation failed.")
        elif opcion=="2":
            datos=input("Enter the website, username, and password:").split()
            if len(datos) < 3:
                print("Input is in the wrong format!")
            elif len(datos[2]) < 12:
                print("Password is too short!")
            else:
                add_login(filename, datos[0], datos[1], datos[2])
                print("Login added.")
        elif opcion=="3":
            break
        else: 
            print("Invalid option selected!")




if __name__ == "__main__":
    main()
