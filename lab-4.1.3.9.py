def isPrime(num):
    cpt = 0
    for i in range(2,num):
        if num % i == 0:
            cpt += 1
    if cpt == 0:
        return True
    else:
        return False
#
# put your code here
#

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()