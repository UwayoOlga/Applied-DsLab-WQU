# Python Exercise Solutions
# Complete solutions for all exercises

# =============================================================================
# EXERCISE 1: CONDITIONS - SOLUTIONS
# =============================================================================

# 1.1: Number Classifier
def classify_number(num):
    """Classify a number as positive, negative, or zero"""
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

# 1.2: Grade Calculator
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

# 1.3: Age Category
def age_category(age):
    """Categorize age into groups"""
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

# =============================================================================
# EXERCISE 2: FUNCTIONS - SOLUTIONS
# =============================================================================

# 2.1: Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# 2.2: Temperature Converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit: F = C * 9/5 + 32"""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius: C = (F - 32) * 5/9"""
    return (fahrenheit - 32) * 5/9

# 2.3: Area Calculator
def rectangle_area(length, width):
    return length * width

def circle_area(radius):
    """Use π ≈ 3.14159"""
    return 3.14159 * radius * radius

def triangle_area(base, height):
    return 0.5 * base * height

# =============================================================================
# EXERCISE 3: LOOPS - SOLUTIONS
# =============================================================================

# 3.1: Number Patterns
def print_numbers(n):
    """Print numbers from 1 to n"""
    for i in range(1, n + 1):
        print(i)

def print_even_numbers(n):
    """Print even numbers from 2 to n"""
    for i in range(2, n + 1, 2):
        print(i)

def print_reverse(n):
    """Print numbers from n down to 1"""
    for i in range(n, 0, -1):
        print(i)

# 3.2: Sum and Average
def sum_numbers(n):
    """Calculate sum of numbers from 1 to n"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
    # Alternative: return sum(range(1, n + 1))

def calculate_average(numbers):
    """Calculate average of numbers in a list"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# 3.3: Multiplication Table
def multiplication_table(num, limit=10):
    """Print multiplication table for num up to limit"""
    for i in range(1, limit + 1):
        result = num * i
        print(f"{num} x {i} = {result}")

# =============================================================================
# EXERCISE 4: STRINGS - SOLUTIONS
# =============================================================================

# 4.1: String Analysis
def count_vowels(text):
    """Count number of vowels in text"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def count_words(text):
    """Count number of words in text"""
    return len(text.split())

def is_palindrome(text):
    """Check if text reads the same forwards and backwards"""
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# 4.2: String Manipulation
def reverse_string(text):
    """Return reversed string"""
    return text[::-1]

def title_case(text):
    """Convert to title case"""
    return text.title()

def remove_spaces(text):
    """Remove all spaces from text"""
    return text.replace(" ", "")

# 4.3: String Search and Replace
def find_all_positions(text, substring):
    """Find all starting positions of substring in text"""
    positions = []
    start = 0
    while True:
        pos = text.find(substring, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

def replace_all(text, old, new):
    """Replace all occurrences of old with new"""
    return text.replace(old, new)

# =============================================================================
# EXERCISE 5: COMBINED CHALLENGES - SOLUTIONS
# =============================================================================

# 5.1: Password Validator
def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    if not has_upper:
        return False, "Password must contain at least one uppercase letter"
    if not has_lower:
        return False, "Password must contain at least one lowercase letter"
    if not has_digit:
        return False, "Password must contain at least one digit"
    
    return True, "Password is valid"

# 5.2: Number Guessing Game
def number_guessing_game():
    """Simple number guessing game"""
    import random
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("Guess the number between 1 and 100!")
    print(f"You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess == target:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                return
            elif guess < target:
                print("Too low!")
            else:
                print("Too high!")
                
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts left.")
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"Game over! The number was {target}")

# 5.3: Text Statistics
def text_statistics(text):
    """Return dictionary with text statistics"""
    # Count characters (excluding spaces)
    char_count = len(text.replace(" ", ""))
    
    # Count words
    word_count = len(text.split())
    
    # Count sentences (rough estimate)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    # Find most common letter
    letter_freq = {}
    for char in text.lower():
        if char.isalpha():
            letter_freq[char] = letter_freq.get(char, 0) + 1
    
    most_common_letter = max(letter_freq, key=letter_freq.get) if letter_freq else ""
    
    # Count vowels and consonants
    vowel_count = count_vowels(text)
    consonant_count = char_count - vowel_count
    
    return {
        'character_count': char_count,
        'word_count': word_count,
        'sentence_count': sentence_count,
        'most_common_letter': most_common_letter,
        'vowel_count': vowel_count,
        'consonant_count': consonant_count
    }

# 5.4: List Processor
def process_names(names):
    """Process list of names and return formatted results"""
    # Filter names longer than 3 characters
    filtered_names = [name for name in names if len(name) > 3]
    
    # Convert to title case
    title_names = [name.title() for name in filtered_names]
    
    # Sort alphabetically
    sorted_names = sorted(title_names)
    
    # Add numbering
    numbered_names = []
    for i, name in enumerate(sorted_names, 1):
        numbered_names.append(f"{i}. {name}")
    
    return numbered_names

# =============================================================================
# BONUS EXERCISES - SOLUTIONS
# =============================================================================

# B1: Fibonacci Sequence
def fibonacci(n):
    """Generate first n numbers in Fibonacci sequence"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_num)
    
    return fib_sequence

# B2: Prime Number Checker
def is_prime(num):
    """Check if number is prime"""
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

# B3: Word Frequency Counter
def word_frequency(text):
    """Count frequency of each word in text"""
    words = text.lower().split()
    frequency = {}
    
    for word in words:
        # Remove punctuation
        clean_word = ""
        for char in word:
            if char.isalpha():
                clean_word += char
        
        if clean_word:
            frequency[clean_word] = frequency.get(clean_word, 0) + 1
    
    return frequency

# B4: Simple Encryption (Caesar Cipher)
def caesar_cipher(text, shift):
    """Encrypt text using Caesar cipher"""
    result = ""
    
    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Handle lowercase letters
            else:
                shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

# =============================================================================
# TESTING SECTION
# =============================================================================

if __name__ == "__main__":
    print("=== TESTING SOLUTIONS ===\n")
    
    # Test Exercise 1: Conditions
    print("1. CONDITIONS:")
    classify_number(5)    # Should print "Positive"
    classify_number(-3)   # Should print "Negative"
    classify_number(0)    # Should print "Zero"
    print(f"Grade for 95: {get_grade(95)}")  # Should return "A"
    print(f"Age category for 25: {age_category(25)}")  # Should return "Adult"
    print()
    
    # Test Exercise 2: Functions
    print("2. FUNCTIONS:")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"100°F to Celsius: {fahrenheit_to_celsius(100):.1f}°C")
    print(f"Circle area (radius 5): {circle_area(5):.2f}")
    print()
    
    # Test Exercise 3: Loops
    print("3. LOOPS:")
    print("Numbers 1-5:")
    print_numbers(5)
    print(f"Sum of numbers 1-10: {sum_numbers(10)}")
    print(f"Average of [1,2,3,4,5]: {calculate_average([1,2,3,4,5])}")
    print()
    
    # Test Exercise 4: Strings
    print("4. STRINGS:")
    print(f"Vowels in 'Hello World': {count_vowels('Hello World')}")
    print(f"Is 'racecar' a palindrome: {is_palindrome('racecar')}")
    print(f"Reverse 'Python': {reverse_string('Python')}")
    print(f"Positions of 'll' in 'Hello World': {find_all_positions('Hello World', 'll')}")
    print()
    
    # Test Exercise 5: Combined
    print("5. COMBINED:")
    is_valid, message = validate_password("MyPass123")
    print(f"Password validation: {is_valid} - {message}")
    
    stats = text_statistics("Hello world! How are you today?")
    print(f"Text statistics: {stats}")
    
    names = ["john", "alice", "bob", "charlie"]
    processed = process_names(names)
    print(f"Processed names: {processed}")
    print()
    
    # Test Bonus Exercises
    print("BONUS:")
    print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
    print(f"Is 17 prime: {is_prime(17)}")
    print(f"Is 18 prime: {is_prime(18)}")
    
    freq = word_frequency("hello world hello python world")
    print(f"Word frequency: {freq}")
    
    encrypted = caesar_cipher("Hello World", 3)
    print(f"Caesar cipher 'Hello World' with shift 3: {encrypted}")
