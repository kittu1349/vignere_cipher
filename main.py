import random
import string

def generate_random_key(length=10):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def vigenere_cipher(text, key, mode='encode'):
    key = [ord(k) - 65 for k in key.upper()]
    key_length = len(key)
    processed_text = []
    key_index = 0

    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            char_code = ord(char) - offset
            if mode == 'encode':
                char_code = (char_code + key[key_index % key_length]) % 26
            elif mode == 'decode':
                char_code = (char_code - key[key_index % key_length] + 26) % 26
            processed_text.append(chr(char_code + offset))
            key_index += 1
        else:
            processed_text.append(char)

    return ''.join(processed_text)

def main():
    while True:
        print("Vigenere Cipher Tool")
        print("1. Encode")
        print("2. Decode")
        print("3. Generate Random Key")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter text to encode: ")
            key = input("Enter key: ")
            encoded_text = vigenere_cipher(text, key, mode='encode')
            print(f"Encoded text: {encoded_text}")

        elif choice == '2':
            text = input("Enter text to decode: ")
            key = input("Enter key: ")
            decoded_text = vigenere_cipher(text, key, mode='decode')
            print(f"Decoded text: {decoded_text}")

        elif choice == '3':
            length = int(input("Enter length of random key: "))
            random_key = generate_random_key(length)
            print(f"Generated random key: {random_key}")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
