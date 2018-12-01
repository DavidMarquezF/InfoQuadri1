def matriu():
    i = 0
    while i < 10:
        i+=1
        printLinia(i)

def printLinia(num):
    i = num-1
    while i < num + 9:
        i+=1
        print i,
    print""

def askNum():
    uinput = -1
    total = 0
    while uinput != 0:
        uinput = input("Write a number: ")
        total += uinput
    print "The sum of the numbers you have written is", total

matriu()
askNum()