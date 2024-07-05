def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = ord(char) + shift_amount
            if char.islower():
                if new_char > ord('z'):
                    new_char -= 26
                encrypted_message += chr(new_char)
            elif char.isupper():
                if new_char > ord('Z'):
                    new_char -= 26
                encrypted_message += chr(new_char)
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = ord(char) - shift_amount
            if char.islower():
                if new_char < ord('a'):
                    new_char += 26
                decrypted_message += chr(new_char)
            elif char.isupper():
                if new_char < ord('A'):
                    new_char += 26
                decrypted_message += chr(new_char)
        else:
            decrypted_message += char
    return decrypted_message

def main():
    while True:
        choice = input("Would you like to encrypt or decrypt a message? (enter 'encrypt' or 'decrypt', or 'exit' to quit): ").lower()
        if choice == 'exit':
            break
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'encrypt':
            result = caesar_cipher_encrypt(message, shift)
            print("Encrypted message:", result)
        elif choice == 'decrypt':
            result = caesar_cipher_decrypt(message, shift)
            print("Decrypted message:", result)
        else:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
