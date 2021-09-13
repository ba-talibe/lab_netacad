def readint(prompt, min, max):
    while True:
        try:
            n = int(input(prompt))
            assert min <= n <= max
            return n
        except:
            print("Error: wrong input")
        
v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)