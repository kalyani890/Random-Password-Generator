
# Task 3: Random Password Generator

import random
import string

while True:
    print("\n===== RANDOM PASSWORD GENERATOR =====")

    # Get password length
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8.")
            continue

    except ValueError:
        print("Error: Please enter a valid whole number.")
        continue

    # Select character types
    print("\nChoose at least TWO character types:")
    print("1. Uppercase letters (A-Z)")
    print("2. Lowercase letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Symbols (!@#$ etc.)")

    choices = input("Enter choices separated by commas (e.g. 1,2,3,4): ")

    selected = set(choices.replace(" ", "").split(","))

    if not selected.issubset({"1", "2", "3", "4"}):
        print("Error: Choose only options 1, 2, 3, and 4.")
        continue

    if len(selected) < 2:
        print("Error: Select at least TWO character types.")
        continue

    # Build character groups
    groups = []

    if "1" in selected:
        groups.append(string.ascii_uppercase)

    if "2" in selected:
        groups.append(string.ascii_lowercase)

    if "3" in selected:
        groups.append(string.digits)

    if "4" in selected:
        groups.append(string.punctuation)

    # Ensure the password can contain every selected type
    if length < len(groups):
        print("Error: Password length is too short.")
        continue

    # Guarantee at least one character from each selected type
    password_chars = [random.choice(group) for group in groups]

    # Fill the remaining positions
    all_chars = "".join(groups)

    for _ in range(length - len(password_chars)):
        password_chars.append(random.choice(all_chars))

    # Shuffle the password characters
    random.shuffle(password_chars)

    password = "".join(password_chars)

    print("\nGenerated Password:", password)

    # Generate another password if required
    again = input("\nGenerate another password? (yes/no): ").strip().lower()

    if again not in ("yes", "y"):
        print("Exiting the password generator program.")
        break
