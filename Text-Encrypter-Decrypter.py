print("\n------------------ Caesar Cipher -----------------------")
print("\nWant to encrypt or decrypt?")
while True:
    def encrypt():
        text = input("\nEnter text for encrypting : ")
        shift = int(input("How many shifts : "))
        final = ""
        for x in text:

            if x.isupper():
                asciii = ord(x)
                final = final + chr((asciii + shift - 65) % 26 + 65)
            elif x.islower():
                asciii = ord(x)
                final = final + chr((asciii + shift - 97) % 26 + 97)

        print(final)


    def decrypt():
        text = input("\nEnter text for decrypting : ")
        shift = int(input("How many shifts : "))
        final = ""
        for x in text:

            if x.isupper():
                asciii = ord(x)
                final = final + chr((asciii - shift - 65) % 26 + 65)
            elif x.islower():
                asciii = ord(x)
                final = final + chr((asciii - shift - 97) % 26 + 97)

        print(final)


    option = int(input("\n[+] Enter 1 for Encryption, 2 for Decryption and 3 for Exit : "))

    if option == 1:
        encrypt()
    elif option == 2:
        decrypt()
    elif option == 3:
        break
