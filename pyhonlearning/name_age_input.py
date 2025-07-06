# Write a Python program that asks the user to input their name and age, then prints a message saying: "Hello [name], you are [age] years old." 
 
name = input("Please enter your name: ")
 
age = int(input("Please enter your age: "))

# Print the personalized message using f-strings for easy formatting
print(f"Hello {name}, you are {age} years old.")