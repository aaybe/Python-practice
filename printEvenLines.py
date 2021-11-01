def printEven(filename):
    f = open(filename, 'r')
    i = 1
    for line in f.readlines():
        if ( i % 2 == 0):
            print(line.strip())
        i += 1

nameFile = input("Name of file: ")
printEven(nameFile)
