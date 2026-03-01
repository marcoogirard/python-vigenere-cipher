text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

def main():
    print("\n=== Vigenère Cipher ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")

    choice = input("\nChoose an option (1 or 2): ").strip()

    if choice not in ('1', '2'):
        print("Invalid option. Please choose 1 or 2.")
        return

    message = input("Enter your message: ").strip()
    key = input("Enter your key: ").strip().lower()

    if not key.isalpha():
        print("The key must contain only letters.")
        return

    if choice == '1':
        result = encrypt(message, key)
        print(f"\nOriginal message : {message}")
        print(f"Key              : {key}")
        print(f"Encrypted text   : {result}\n")
    else:
        result = decrypt(message, key)
        print(f"\nEncrypted message : {message}")
        print(f"Key               : {key}")
        print(f"Decrypted text    : {result}\n")


if __name__ == "__main__":
    main()


