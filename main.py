from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""
    filename= input("Enter the CSV file name:")
    encrypt_passwords_in_file(filename)
    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        opcion=input().strip()
        if opcion=="1":
            datos=input("Enter the website and the new password:")
            


if __name__ == "__main__":
    main()
