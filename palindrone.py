def list_to_string(lst):
    s = ""
    for i in lst:
        s += i
    return s

def palindrome(s):
    l = list(i for i in s)
    s1 = ""
    for i in range(len(l)):
        s1 += l[-len(l) +i] 
    print(s1)
    if s == s1:
        return True
    else:
        return False

def palindrome1(s):
    l = list(i for i in s)
    l.reverse()
    if s == list_to_string(l):
        return True
    else:
        return False

chaine = input("Donner un chaine : ")

if palindrome(chaine):
    print(chaine, "est bien un palindrone")
else:
    print(chaine, "n'est pas un palindrone")