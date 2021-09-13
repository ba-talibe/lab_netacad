def l100kmtompg(liters):
    mpg = (100000/1609.344)/(liters/3.785411784)
    return mpg
# put your code here
#

def mpgtol100km(miles):
    km = 3.785411784/((miles*1609.344*(10**(-3)))/100)
    return km
#
# put your code here
#

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
