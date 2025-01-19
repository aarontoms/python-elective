
def encrypt():
    text = input("Enter text to encrypt: ")
    crypt = int(input("Enter key: "))
    encrypted = ""
    for char in text:
        ascii = ord(char)
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            ascii += crypt
            if 'A' <= char <= 'Z' and ascii > 90:
                ascii -= 26
            elif 'a' <= char <= 'z' and ascii > 122:
                ascii -= 26
        
        encrypted += chr(ascii)
    
    print(encrypted + "\n")

def decrypt():
    text = input("Enter text to decrypt: ")
    crypt = int(input("Enter key: "))
    decrypted = ""
    for char in text:
        ascii = ord(char)
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            ascii -= crypt
            if 'A' <= char <= 'Z' and ascii < 65:
                ascii += 26
            elif 'a' <= char <= 'z' and ascii < 97:
                ascii += 26
        
        decrypted += chr(ascii)
    
    print(decrypted + "\n")

while True:
    ch = int(input("---MENU---\n 1. Encrypt\n 2. Decrypt\n 3. Exit\nEnter choice: "))
    if ch == 1:
        encrypt()
    elif ch == 2:
        decrypt()
    elif ch == 3:
        break