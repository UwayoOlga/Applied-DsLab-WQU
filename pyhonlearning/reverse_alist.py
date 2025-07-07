#Given the list numbers = [4, 7, 2, 9, 5], write code to:
# ▪Print the list in reverse order.
# ▪Find and print the largest number.

numbers = [4, 7, 2, 9, 5]
 
print("Reversed list:", numbers[::-1])
largest_number = max(numbers)
print("Largest number:", largest_number)