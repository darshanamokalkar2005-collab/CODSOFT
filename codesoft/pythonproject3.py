import random
import string

def generate_password(length=12):
    # Defining character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password from the characters
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password

# Example: Generate a password of length 16
password = generate_password(16)
print("Generated password:", password)
