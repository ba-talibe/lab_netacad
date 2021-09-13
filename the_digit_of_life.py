n = input(">>>")
def digit(n):
    if len(n) == 1:
        return int(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return digit(str(sum))
    
print(digit(n))
        