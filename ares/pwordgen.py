import secrets
import string
import pyperclip
import sys

def generate_password():
    # Define character sets for different types of characters
    lowercase_characters = string.ascii_lowercase
    uppercase_characters = string.ascii_uppercase
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    alphanumeric_characters = string.digits + lowercase_characters + uppercase_characters

    # Initialize the password with at least one character from each category
    password = (
        secrets.choice(lowercase_characters) +
        secrets.choice(uppercase_characters) +
        secrets.choice(special_characters)
    )

    # Generate the rest of the password
    remaining_length = 20 - len(password)
    for _ in range(remaining_length):
        character_set = alphanumeric_characters + special_characters
        password += secrets.choice(character_set)

    # Shuffle the password to make it more secure
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    return password

def copy_to_clipboard(text):
    try:
        pyperclip.copy(text)
        print("Password copied to clipboard.")
    except pyperclip.PyperclipException as e:
        print(f"Error copying to clipboard: {e}")

def main():
    # Generate a secure password
    secure_password = generate_password()

    # Copy the password to the clipboard
    copy_to_clipboard(secure_password)

if __name__ == "__main__":
    main()
