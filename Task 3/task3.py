import random
import string
import pyperclip

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        print("--------------------PASSWORD GENERATOR--------------------")
        print("Made By :- Rajib Bishal")
        print("-----------------------------------------------------------")
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Length must be greater than 0.")
            main()
        password = generate_password(length)
        print("Generated Password: ", password)

        pyperclip.copy(password)
        print("Password copied to clipboard.")
    except ValueError:
        print("Invalid input. Please enter a valid length (a positive integer).")
        main()

if __name__ == "__main__":
    main()
