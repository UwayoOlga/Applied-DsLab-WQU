# Python Practice Exercises
# Topics: Conditions, Functions, Loops, Strings

# =============================================================================
# EXERCISE 1: CONDITIONS
# =============================================================================

# 1.1: Number Classifier
# Write a program that takes a number and prints whether it's positive, negative, or zero
def classify_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

# Test cases
classify_number(5)   # Should print "Positive"
classify_number(-3)  # Should print "Negative"
classify_number(0)   # Should print "Zero"



# 1.2: Grade Calculator
# Write a function that takes a score (0-100) and returns the letter grade
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
def get_grade(score):
    """Convert numeric score to letter grade"""
    # YOUR CODE HERE
    pass

# Test: get_grade(95) should return "A"
# Test: get_grade(75) should return "C"


# 1.3: Age Category
# Write a function that categorizes age: Child (0-12), Teen (13-19), Adult (20-59), Senior (60+)
def get_grade(score):
    """Convert numeric score to letter grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test cases
print(get_grade(95))  # Should return "A"
print(get_grade(75))  # Should return "C"


# =============================================================================
# EXERCISE 2: FUNCTIONS
# =============================================================================

# 2.1: Calculator Functions
# Create basic calculator functions
def add(a, b):
    return(sum(a,b))

def subtract(a, b):
    return a - b

def multiply(a, b):
 return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"


# 2.2: Temperature Converter
# Create functions to convert between Celsius and Fahrenheit
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit: F = C * 9/5 + 32"""
    return (celsius * 9 / 5 + 32)


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius: C = (F - 32) * 5/9"""
    return (fahrenheit - 32) * 5 / 9


# 2.3: Area Calculator
# Create functions to calculate area of different shapes
def rectangle_area(length, width):
    return length * width

def circle_area(radius):
    """Use π ≈ 3.14159"""
    return radius * radius * 3.14159

def triangle_area(base, height):
    return 0.5 * base * height

# =============================================================================
# EXERCISE 3: LOOPS
# =============================================================================

# 3.1: Number Patterns
# Print numbers from 1 to n
def print_numbers(n):
    """Print numbers from 1 to n"""
    for i in range(1, n + 1):
        print(i)
      

# Print even numbers from 2 to n
def print_even_numbers(n):
    """Print even numbers from 2 to n"""
    for i in range(2, n+1):
        print(i)


# Print numbers in reverse from n to 1
def print_reverse(n):
    """Print numbers from n down to 1"""
    # range(start, stop, step)
    for i in range(n, 0, -1):
        print(i)


# 3.2: Sum and Average
# Calculate sum of numbers from 1 to n
def sum_numbers(n):
    """Calculate sum of numbers from 1 to n"""
    return sum(range(1, n + 1))


# Calculate average of a list of numbers
def calculate_average(numbers):
    """Calculate average of numbers in a list"""
    if not numbers:  # Check if the list is empty
        return 0  # or return None, depending on your use case
    return sum(numbers) / len(numbers)



# 3.3: Multiplication Table
# Print multiplication table for a given number
def multiplication_table(num, limit=10):
    """Print multiplication table for num up to limit"""
    for i in range(1, limit + 1):
        print(f"{num} x {i} = {num * i}")


# =============================================================================
# EXERCISE 4: STRINGS
# =============================================================================

# 4.1: String Analysis
# Count vowels in a string
def count_vowels(text):
    """Count number of vowels in text"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Count words in a string
def count_words(text):
    words = text.split()
    return len(words)

# Check if string is palindrome
def is_palindrome(text):
    """Check if text reads the same forwards and backwards""" 
    cleaned_text = text.lower().replace(" ", "")
    # return boolean  
    return cleaned_text == cleaned_text[::-1]


# 4.2: String Manipulation
# Reverse a string
def reverse_string(text):
    """Return reversed string"""
    return text[::-1]

# Capitalize first letter of each word
def title_case(text):
    """Convert to title case"""
    return text.title()

# Remove all spaces from string
def remove_spaces(text):
        return text.replace(" ", "")


# 4.3: String Search and Replace

# Find all positions of a substring
def find_all_positions(text, substring):
    """Find all starting positions of substring in text"""
    positions = []
    index = text.find(substring)
    while index != -1:
        positions.append(index) 
        index = text.find(substring, index + 1)
    return positions


# Replace all occurrences of old with new
def replace_all(text, old, new):
    """Replace all occurrences of old with new"""
    return text.replace(old, new)


# =============================================================================
# EXERCISE 5: COMBINED CHALLENGES
# =============================================================================

# 5.1: Password Validator
# Check if password meets criteria:
# - At least 8 characters long
# - Contains at least one uppercase letter
# - Contains at least one lowercase letter  
# - Contains at least one digit
def validate_password(password):
    """Validate password strength"""
    # YOUR CODE HERE - return True/False and reason
    pass


# 5.2: Number Guessing Game
# Create a simple number guessing game
def number_guessing_game():
    """Simple number guessing game"""
    import random
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("Guess the number between 1 and 100!")
    print(f"You have {max_attempts} attempts.")
    
    # YOUR CODE HERE
    # Use while loop, input(), conditions
    pass


# 5.3: Text Statistics
# Analyze text and return statistics
def text_statistics(text):
    """Return dictionary with text statistics"""
    # YOUR CODE HERE
    # Return dict with: character_count, word_count, sentence_count, 
    # most_common_letter, vowel_count, consonant_count
    pass


# 5.4: List Processor
# Process a list of strings with various operations
def process_names(names):
    """Process list of names and return formatted results"""
    # YOUR CODE HERE
    # 1. Filter names longer than 3 characters
    # 2. Convert to title case
    # 3. Sort alphabetically
    # 4. Add numbering (1. Name, 2. Name, etc.)
    pass


# =============================================================================
# BONUS EXERCISES
# =============================================================================

# B1: Fibonacci Sequence
def fibonacci(n):
    """Generate first n numbers in Fibonacci sequence"""
    # YOUR CODE HERE
    pass

# B2: Prime Number Checker
def is_prime(num):
    """Check if number is prime"""
    # YOUR CODE HERE
    pass

# B3: Word Frequency Counter
def word_frequency(text):
    """Count frequency of each word in text"""
    # YOUR CODE HERE - return dictionary
    pass

# B4: Simple Encryption (Caesar Cipher)
def caesar_cipher(text, shift):
    """Encrypt text using Caesar cipher"""
    # YOUR CODE HERE
    pass

# =============================================================================
# TESTING SECTION
# =============================================================================

# Uncomment and run these tests to check your solutions
if __name__ == "__main__":
    # Test your functions here
    print("Testing section - uncomment tests as you complete exercises")
    
    # Example tests:
    # print(classify_number(5))
    # print(get_grade(85))
    # print(count_vowels("Hello World"))
    # print(is_palindrome("racecar"))
    
    pass