def rot13(text):
    """ROT13 - Cryptographic Algorithm"""
    
    result = []

    for char in text:
        # Lowercase letters
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        # Uppercase letters
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        # Non-alphabetical characters
        else:
            result.append(char)

    return ''.join(result)

message = input("Enter the message: ")

# Encryption
cipher = rot13(message)
print("Encrypted message: ", cipher)

# Decryption
message = rot13(cipher)
print("Decrypted message: ", message)