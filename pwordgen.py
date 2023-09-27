import secrets
import string

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

# Generate and print a secure password
secure_password = generate_password()
print(secure_password)
