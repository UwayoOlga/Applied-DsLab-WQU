#  Simple Encryption (Caesar Cipher)


def caesar_cipher(text, shift):
    """Encrypt text using Caesar cipher"""
    result = ""
    for char in text:
        if char.isalpha(): 
            base = ord('A') if char.isupper() else ord('a') 
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else: 
            result += char
    return result
