def encrypt(text,shift):
    encrypt_text = ""
    for char in text:
        if char.isalpha(): # Check if character is in the alphabet 
            if char.islower(): 
                encrypt_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a')) 
                """
                1. Measure the distance between th base char a and the char and add the shift 
                2. Get Modulus in the instance that the distance is greater than the whole alphabet. 
                Ex. Shift = 3 Char = z result would be 28. Adding 28 to the ord('a') would make } instead of c
                3. Add the distance to base char to get the letter for the shift

                """
            else:
                encrypt_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypt_text += char
    return encrypt_text

def decrypt(text,shift): #To decrypt, algo is the same, just go backwards 
    decrypt_text = encrypt(text,-shift)
    return decrypt_text


def main():
    choice = input("Would like like to Encrypt or Decrypt? (E/D) :")
    text = input("Enter the secret text: ")
    shift = int(input("Enter the shift value: "))

    if choice == "E":
        encrypt_text = encrypt(text,shift)
        print("Encrypted text:", encrypt_text)
    else:
        decrypt_text = decrypt(text,shift)
        print("Dencrypted text:", decrypt_text)


if __name__ == "__main__":
    main()

