#takes user name and birthdate as string input
name =raw_input("Enter your first name: ")
birthdate =raw_input("Enter your birth date: ")

#file name and creates file if non-existent
fileName = name + ".txt"
f = open(fileName, 'a+')

#writes birthdate on file
f.write(birthdate)

#closes file
f.close()
