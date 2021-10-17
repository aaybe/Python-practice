#Exercise 1: Print First 10 natural numbers using while loop

num = 0
while (num <= 10):
    print(num)   
    num += 1
    
#Exercise 2: Print the following pattern
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5
for x in range(6):
    for j in range(x+1):
        print (j, end=" ")
    print(' ')
    
#Exercise 3: Calculate the sum of all numbers from 1 to a given number
result = 0
number = int(input("Enter number: "))
for x in range(number+1):
    result += x
print("Sum is: " + str(result))
