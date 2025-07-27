import art
print(art.logo)

print("~~~ Welcome To Caisar Cipher Program ~~~")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt text, type 'decode' to decrypt text : \n").lower()
text = input("Type your message :\n").lower()
shift = int (input ("Type the shift number: \n"))


def caesar(text_user, shift_amount):
    encrypted_chars = []
    if direction == "encode" :
        text_user = list(text_user)
        for char in text_user :
            if char in alphabet :
                index = alphabet.index(char)
                result = (index + shift_amount) % 26
                final = alphabet[result]
                encrypted_chars.append(final)
            else :
                encrypted_chars.append(char)
        encrypted_text = ''.join(encrypted_chars)
        print(f"Your encrypted result is : {encrypted_text}")

    elif direction == "decode" :
        text_user = list(text_user)
        for char in text_user :
            if char in alphabet :
                index = alphabet.index(char)
                result = (index - shift_amount) % len(alphabet)
                final = alphabet[result]
                encrypted_chars.append(final)
            else :
                encrypted_chars.append(char)
        encrypted_text = ''.join(encrypted_chars)
        print(f"Your decoded result is : {encrypted_text}")

caesar(text_user=text, shift_amount=shift)

reload = input("Type \"yes\" if u want to reload the program. Otherwise type \"no\"\n").lower()

while reload == "yes" :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n").lower()
    text = input("Type your message :\n").lower()
    shift = int (input ("Type the shift number: \n"))

    if direction == "encode" or "decode":
        caesar(text_user=text, shift_amount=shift)
    
    reload = input("Type \"yes\" if u want to reload the program. Otherwise type \"no\"\n").lower()

if reload == "no" :
    print("~~Good Bye!~~")




