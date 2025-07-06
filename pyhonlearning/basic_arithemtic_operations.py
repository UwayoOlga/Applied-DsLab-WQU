# ask the user to input two numbers and print their sum, difference, product, and quotient.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = "Undefined (division by zero)"
print("Quotient:", quotient_result)