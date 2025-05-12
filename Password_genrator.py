import random

def generate_passwords(password_lengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for length in password_lengths:
        password = ''.join(random.choice(alphabet) for _ in range(length))
        password = replace_with_number(password)
        password = replace_with_uppercase(password)
        passwords.append(password)

    return passwords

def replace_with_number(password):
    num_replacements = random.randint(1, 2)
    for _ in range(num_replacements):
        index = random.randrange(len(password) // 2)
        digit = str(random.randint(0, 9))
        password = password[:index] + digit + password[index + 1:]
    return password

def replace_with_uppercase(password):
    num_replacements = random.randint(1, 2)
    for _ in range(num_replacements):
        index = random.randrange(len(password) // 2, len(password))
        password = password[:index] + password[index].upper() + password[index + 1:]
    return password

def main():
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    print(f"Generating {num_passwords} passwords.")
    print("Minimum length of each password should be 3.")

    password_lengths = []
    for i in range(num_passwords):
        try:
            length = int(input(f"Enter the length of Password #{i + 1}: "))
            if length < 3:
                print("Length too short. Setting to minimum length 3.")
                length = 3
            password_lengths.append(length)
        except ValueError:
            print("Invalid input. Using default length 8.")
            password_lengths.append(8)

    passwords = generate_passwords(password_lengths)

    for i, pwd in enumerate(passwords, start=1):
        print(f"Password #{i}: {pwd}")

if __name__ == "__main__":
    main()
