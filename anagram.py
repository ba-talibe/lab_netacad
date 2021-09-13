def anagram(s, n):
    s = s.lower()
    n = s.lower()
    if all(s.count(i) == n.count(i) for i in s):
        return True
    return False

s = input(">>>")
n = input(">>>")

if anagram(s, n):
    print("Anagrams")
else:
    print("Not Anagrams")