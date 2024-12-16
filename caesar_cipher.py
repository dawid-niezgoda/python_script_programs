def caesar_cipher(text, shift):
    """Caesar Cipher - Cryptographic Algorithm"""
    
    result = []

    for char in text:
        # Lowercase letters
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        # Uppercase letters
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        # Non-alphabetical characters
        else:
            result.append(char)
    
    return ''.join(result)

message = input("Enter the message: ")
shift = int(input("Enter the shift: "))

# Encryption
cipher = caesar_cipher(message, shift)
print("Encrypted message: ", cipher)

# Decryption
message = caesar_cipher(cipher, -shift)
print("Decrypted message: ", message)