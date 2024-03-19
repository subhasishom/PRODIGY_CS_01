def caesar_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage
plaintext = "Hello, World! 123"
shift = 3

encrypted_text = caesar_encrypt(plaintext, shift)
print("Encrypted:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted:", decrypted_text)