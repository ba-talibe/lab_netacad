cipher = input("Enter your ciphered message: ")
shift = int(input("enter the shift value between 1-25 : "))
while not 1 <= shift <= 25:
    shift = int(input("enter the shift value between 1-25 : "))

#a 97 #z122 #A 64 #Z 90
def decrypt(cipher, shift):
    text = ''
    for char in cipher:
        if char == " ":
            text += ' '
        if not char.isalpha():
            continue
        if char.islower():
            min = ord('a')
            max = ord('z')
        else:
            min = ord('A')
            max = ord('Z')
        code = ord(char) - shift
        if code < min:
            text += chr(max -(min - code - 1))
        else:
            text += chr(code)
    return text

print(decrypt(cipher, shift))
