def caesar_cipher_manual(message, shift):
    """Cryptographic Algorithm - Caesar Cipher. Encryption and Decryption User-Entered Message."""
    result = []

    for char in message:
        # Uppercase letters
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        # Lowercase letters
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        # Non-alphabetical characters
        else:
            result.append(char)
    
    return ''.join(result)

user_message = input("Enter a message: ")
shift_value = int(input("Enter a shift value [1-25]: "))

# Encryption
cipher = caesar_cipher_manual(user_message, shift_value)
print("Encrypted message:", cipher)

# Decryption
message = caesar_cipher_manual(cipher, -shift_value)
print("Decrypted message:", message)