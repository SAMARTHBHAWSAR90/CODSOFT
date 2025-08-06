import random 
import string

class PasswordGenerator:
    def __init__(self):
        self.uppercase_letter = string.ascii_uppercase
        self.lowercase_letter = string.ascii_lowercase
        self.digits = string.digits
        self.symbols = string.punctuation

        self.character_pool = (
            self.uppercase_letter +
            self.lowercase_letter + 
            self.digits + 
            self.symbols
        )

    def generate_password(self, length):
        if length < 4:
            print("Password length should be at least 4 characters.")
            return ""
        
        password_chars = random.choices(self.character_pool, k=length)

        password = ''.join(password_chars)
        return password
    
if __name__ == "__main__":
    print("Welcome to the Python Password Generator")

    try:
        user_input = input("Enter desired password length:")
        length = int(user_input)

        generator = PasswordGenerator()

        password = generator.generate_password(length)

        if password:
            print(f"Your generated password: {password}")

    except ValueError:
        print("Invalid input! Please enter a numeric value")    