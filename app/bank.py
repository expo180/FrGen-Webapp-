import random
import string

def generate_bank_id():
    characters = string.ascii_letters + string.digits + "-"
    uppercase_characters = string.ascii_uppercase

    bank_id = ''.join(random.choice(characters) for _ in range(3)) + "-"  # Prefix
    bank_id += ''.join(random.choice(uppercase_characters) for _ in range(6)) + "-"  # Segment 1
    bank_id += ''.join(random.choice(uppercase_characters + string.digits) for _ in range(6)).lower()  # Segment 2

    return bank_id

# Example usage
bank_id = generate_bank_id()
print("Bank ID:", bank_id)
