text = input("Enter your message: ")
shift = int(input("enter the shift value between 1-25 : "))
while not 1 <= shift <= 25:
    shift = int(input("enter the shift value between 1-25 : "))

#a 97 #z122 #A 64 #Z 90
def crypt(text, shift):
    cipher = ''
    for char in text:
        if char == " ":
            cipher += ' '
        if not char.isalpha():
            continue
        if char.islower():
            min = ord('a')
            max = ord('z')
        else:
            min = ord('A')
            max = ord('Z')
        code = ord(char) + shift
        if code > max:
            cipher += chr(min +(code - max - 1))
        else:
            cipher += chr(code)
    return cipher


    """
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)"""

print(crypt(text, shift))