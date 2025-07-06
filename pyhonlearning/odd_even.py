#Write a program that asks the user to enter a number. If the number is even, print "Even number", otherwise print "Odd number".

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")