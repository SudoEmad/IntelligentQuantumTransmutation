import base64
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    try:
        decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
        return decrypted_message
    except Exception as e:
        return str(e)

def main():
    print("Welcome to Quantum Decryption Simulator")

    # Generate a key (in a real scenario, you'd use a known key)
    key = generate_key()
    print(f"Generated key (use this for encryption/decryption): {key.decode()}")

    # Input encrypted message
    encrypted_message = input("Enter the encrypted message to decrypt: ")
    
    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, key)
    
    # Output the decrypted message
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
