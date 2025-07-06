#Write a program that asks the user for a number and prints its multiplication table up to 10. 
number = int(input("Enter a number: "))

for i in range(1, 11):

    print(f"{number} x {i} = {number * i}")
