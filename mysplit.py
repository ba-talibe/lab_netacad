def mysplit(string):
    if not ' ' in string:
        return []
    lst = []
    curstring = string.strip()
    while ' ' in curstring and len(curstring):
        lst.append(curstring[:curstring.index(' ')])
        curstring = curstring[curstring.index(' ') +1:]
    if ' ' not in curstring and len(curstring) != 0:
        lst.append(curstring)
    return lst

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))