def caesar_encrypt():
    print()
    print('Caesar Encryption')
    print()

    cipher = ''
    
    plain = input('Enter the plain text: ')

    while True:
        try:
            key = int(input('Enter the key value (1~25): '))
            if 1 <=  key <= 25:
                break
            else:
                print('Invalid input. Key must be an integer between 1 and 25.')
        except ValueError:
            print('Invalid input. Please enter an integer.')

    for i in plain:
        if 'A' <= i <= 'Z':
            cipher += chr((ord(i) + key - ord('A')) % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            cipher += chr((ord(i) + key - ord('a')) % 26 + ord('a'))
        else:
            cipher += i

    print('Encrypting...\n.\n.\n.')
    print('Encrypted text:', cipher)
    print()

    main()

def vigenere_encrypt():
    print()
    print('Vigenere Encryption')
    print()

    cipher = ''

    plain = input('Enter the plain text: ').upper()
    key = input('Enter the key value (key length MUST be the same as plain text length): ').upper()

    while len(plain) != len(key):
        print('key length MUST be the same as plain text length\n(e.g., if plain text = HELLO, key should be APPLE or ABCDE)')
        key = input('Enter the key value: ').upper()

    plain_numberize = [ord(x) - 65 for x in plain]
   
    key_numberize = [ord(x) - 65 for x in key]

    for i in range(len(plain)):
        if plain[i] == ' ':
            cipher += ' '
        else:
            cipher += chr((plain_numberize[i] + key_numberize[i % len(key)]) % 26 + 65)

    print('Encrypting...\n.\n.\n.')
    print('Encrypted text:', cipher)
    print()

    main()

def sub_encrypt():
    print()
    print('Substitution Encryption')
    print()

    mapping = {'A': 'N', 'B': 'K', 'C': 'Y', 'D': 'G', 'E': 'J', 'F': 'S', 'G': 'D', 
               'H': 'U', 'I': 'L', 'J': 'E', 'K': 'B', 'L': 'I', 'M': 'X', 'N': 'A', 
               'O': 'P', 'P': 'O', 'Q': 'W', 'R': 'V', 'S': 'F', 'T': 'Z', 'U': 'H', 
               'V': 'R', 'W': 'Q', 'X': 'M', 'Y': 'C', 'Z': 'T'}
    
    cipher = ''

    plain = input('Enter the plain text: ')

    for i in plain:
        if 'A' <= i <= 'Z':
            cipher += mapping[i]
        elif 'a' <= i <= 'z':
            cipher += mapping[i.upper()].lower()
        else:
            cipher += i
    
    print('Encrypting...\n.\n.\n.')
    print('Encrypted text:', cipher)
    print()

    main()

def morse_encrypt():
    print()
    print('Morse Code Encryption')
    print()

    morse_code = {'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-··', 'E': '·', 'F': '··-·', 'G': '--·', 
                  'H': '····', 'I': '··', 'J': '·---', 'K': '-·-', 'L': '·-··', 'M': '--', 'N': '-·', 
                  'O': '---', 'P': '·--·', 'Q': '--·-', 'R': '·-·', 'S': '···', 'T': '-', 'U': '··-', 
                  'V': '···-', 'W': '·--', 'X': '-··-', 'Y': '-·--', 'Z': '--··'}
    
    cipher = ''

    plain = input('Enter the plain text: ')

    for i in plain.upper():
        if 'A' <= i <= 'Z':
            cipher += morse_code[i] + ' '
        else:
            cipher += '   '
    
    print('Encrypting...\n.\n.\n.')
    print('Encrypted text:', cipher)
    print()

    main()

def caesar_decrypt():
    print()
    print('Caesar Decryption')
    print()

    plain = ''
    
    cipher = input('Enter the cipher text: ')

    while True:
        try:
            key = int(input('Enter the key value (1~25): '))
            if 1 <=  key <= 25:
                break
            else:
                print('Invalid input. Key must be an integer between 1 and 25.')
        except ValueError:
            print('Invalid input. Please enter an integer.')

    for i in cipher:
        if 'A' <= i <= 'Z':
            plain += chr((ord(i) - key - ord('A')) % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            plain += chr((ord(i) - key - ord('a')) % 26 + ord('a'))
        else:
            plain += i

    print('Decrypting...\n.\n.\n.')
    print('Decrypted text:', plain)
    print()

    main()

def vigenere_decrypt():
    print()
    print('Vigenere Decryption')
    print()

    plain = ''

    cipher = input('Enter the cipher text: ').upper()
    key = input('Enter the key value (key length MUST be the same as cipher text length): ').upper()

    while len(cipher) != len(key):
        print('key length MUST be the same as cipher text length\n(e.g., if cipher text = HELLO, key should be APPLE or ABCDE)')
        key = input('Enter the key value: ').upper()

    cipher_numberize = [ord(x) - 65 for x in cipher]
   
    key_numberize = [ord(x) - 65 for x in key]

    for i in range(len(cipher)):
        plain += chr((cipher_numberize[i] - key_numberize[i % len(key)] + 26) % 26 + 65)

    print('Decrypting...\n.\n.\n.')
    print('Decrypted text:', plain)
    print()

    main()

def sub_decrypt():
    print()
    print('Substitution Decryption')
    print()

    mapping = {'A': 'N', 'B': 'K', 'C': 'Y', 'D': 'G', 'E': 'J', 'F': 'S', 'G': 'D', 
               'H': 'U', 'I': 'L', 'J': 'E', 'K': 'B', 'L': 'I', 'M': 'X', 'N': 'A', 
               'O': 'P', 'P': 'O', 'Q': 'W', 'R': 'V', 'S': 'F', 'T': 'Z', 'U': 'H', 
               'V': 'R', 'W': 'Q', 'X': 'M', 'Y': 'C', 'Z': 'T'}
    
    plain = ''

    cipher = input('Enter the plain text: ')

    for i in cipher:
        if 'A' <= i <= 'Z':
            plain += mapping[i]
        elif 'a' <= i <= 'z':
            plain += mapping[i.upper()].lower()
        else:
            plain += i
    
    print('Decrypting...\n.\n.\n.')
    print('Decrypted text:', plain)
    print()

    main()

def morse_decrypt():
    print()
    print('Morse Code Decryption')
    print()

    morse_code = {'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-··', 'E': '·', 'F': '··-·', 'G': '--·', 
                  'H': '····', 'I': '··', 'J': '·---', 'K': '-·-', 'L': '·-··', 'M': '--', 'N': '-·', 
                  'O': '---', 'P': '·--·', 'Q': '--·-', 'R': '·-·', 'S': '···', 'T': '-', 'U': '··-', 
                  'V': '···-', 'W': '·--', 'X': '-··-', 'Y': '-·--', 'Z': '--··'}
    
    morse_code_for_decrypt = {v: k for k, v in morse_code.items()}
    
    plain = ''

    cipher = input('Enter the plain text: ')

    words = cipher.strip().split('   ')

    for word in words:
        letters = word.strip().split(' ')
        for i in letters:
            plain += morse_code_for_decrypt.get(i)
        plain += ' '
    
    print('Encrypting...\n.\n.\n.')
    print('Encrypted text:', plain.strip())
    print()

    main()

def main():
    while True:
        option = input('Would you like to encrypt or decrypt? ')
        
        if option.lower().strip() == 'encrypt' or option.lower().strip() == 'decrypt':
            break
        else:
            print('Invalid input. Please enter \'encrypt\' or \'decrypt\'. ')

    if option.lower().strip() == 'encrypt':
        while True:
            encrypt_type = int(input('\nWhich cipher are you using? \n1. Caesar Cipher \n2. Vigenere Cipher \n3. Substitution Cipher \n4. Morse Code \nPlease enter the number (1~4): '))

            if encrypt_type in [1, 2, 3, 4]:
                break
            else:
                print('Invalid input. Please enter a number between 1~4. ')

        if encrypt_type == 1:
            caesar_encrypt()
        elif encrypt_type == 2:
            vigenere_encrypt()
        elif encrypt_type == 3:
            sub_encrypt()
        elif encrypt_type == 4:
            morse_encrypt()

    if option.lower().strip() == 'decrypt':
        while True:
            decrypt_type = int(input('Which cipher are you using? \n1. Caesar Cipher \n2. Vigenere Cipher \n3. Substitution Cipher \n4. Morse Code \nPlease enter the number (1~4): '))

            if decrypt_type in [1, 2, 3, 4]:
                break
            else:
                print('Invalid input. Please enter a number between 1~4. ')

        if decrypt_type == 1:
            caesar_decrypt()
        elif decrypt_type == 2:
            vigenere_decrypt()
        elif decrypt_type == 3:
            sub_decrypt()
        elif decrypt_type == 4:
            morse_decrypt()

print()
print('-' * 10)
print('| Cipher |')
print('-' * 10)
print()

main()

print()
