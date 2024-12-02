def rot13(message):
    """Cryptographic Algorithm - ROT13. Encryption and Decryption User-Entered Message."""
    result = []

    for char in message:
        # Uppercase letters
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        # Lowercase letters
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        # Non-alphabetical characters
        else:
            result.append(char)

    return ''.join(result)

user_message = input("Enter a message: ")

# Encryption
cipher = rot13(user_message)
print("Encrypted message:", cipher)

# Decryption
message = rot13(cipher)
print("Decrypted message:", message)