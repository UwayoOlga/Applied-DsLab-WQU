# Intro to Big Data Analytics - Adventist University of Central Africa  
Teachine Assistant : Eric Maniraguha | [LinkedIn](https://www.linkedin.com/in/ericmaniraguha/)


## Beginner String Programming Problems with Solutions

## Problem 1: Find the Length of a String

**Problem:** Write a program to find the length of a string.

**Solution:**
```python
# Method 1: Using built-in len() function
text = "Hello World"
length = len(text)
print(f"Length of '{text}' is: {length}")

# Method 2: Manual counting (without len())
text = "Hello"
count = 0
for char in text:
    count += 1
print(f"Length of '{text}' is: {count}")
```

**Output:**
```
Length of 'Hello World' is: 11
Length of 'Hello' is: 5
```

---

## Problem 2: Check if a String is a Palindrome

**Problem:** Check whether a string reads the same forwards and backwards.

**Solution:**
```python
def is_palindrome(text):
    # Convert to lowercase and remove spaces
    text = text.lower().replace(" ", "")
    
    # Compare string with its reverse
    return text == text[::-1]

# Test cases
strings = ["madam", "hello", "race car", "A man a plan a canal Panama"]

for s in strings:
    if is_palindrome(s):
        print(f"'{s}' is a palindrome")
    else:
        print(f"'{s}' is not a palindrome")
```

**Output:**
```
'madam' is a palindrome
'hello' is not a palindrome
'race car' is a palindrome
'A man a plan a canal Panama' is a palindrome
```

---

## Problem 3: Count Vowels in a String

**Problem:** Count the number of vowels (a, e, i, o, u) in a string.

**Solution:**
```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    
    return count

# Test
text = "Hello World"
vowel_count = count_vowels(text)
print(f"Number of vowels in '{text}': {vowel_count}")

# Method 2: Using sets
def count_vowels_set(text):
    vowels = set("aeiouAEIOU")
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    
    return count

print(f"Using sets method: {count_vowels_set(text)}")
```

**Output:**
```
Number of vowels in 'Hello World': 3
Using sets method: 3
```

---

## Problem 4: Reverse Words in a String

**Problem:** Reverse the order of words in a given string.

**Solution:**
```python
def reverse_words(text):
    # Split string into words, reverse the list, then join back
    words = text.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

# Test
original = "Hello World Python"
reversed_text = reverse_words(original)
print(f"Original: {original}")
print(f"Reversed: {reversed_text}")

# One-liner version
def reverse_words_short(text):
    return " ".join(text.split()[::-1])

print(f"One-liner: {reverse_words_short(original)}")
```

**Output:**
```
Original: Hello World Python
Reversed: Python World Hello
One-liner: Python World Hello
```

---

## Problem 5: Convert String to Uppercase and Lowercase

**Problem:** Convert a string to uppercase and lowercase.

**Solution:**
```python
text = "Hello World Python"

# Convert to uppercase
upper_text = text.upper()
print(f"Uppercase: {upper_text}")

# Convert to lowercase
lower_text = text.lower()
print(f"Lowercase: {lower_text}")

# Capitalize first letter of each word
title_text = text.title()
print(f"Title case: {title_text}")

# Capitalize only first letter
capitalize_text = text.capitalize()
print(f"Capitalize: {capitalize_text}")
```

**Output:**
```
Uppercase: HELLO WORLD PYTHON
Lowercase: hello world python
Title case: Hello World Python
Capitalize: Hello world python
```

---

## Problem 6: Check if String Contains Only Numbers

**Problem:** Check if a string contains only digits.

**Solution:**
```python
def is_only_numbers(text):
    return text.isdigit()

# Test cases
test_strings = ["12345", "123abc", "hello", ""]

for s in test_strings:
    if is_only_numbers(s):
        print(f"'{s}' contains only numbers")
    else:
        print(f"'{s}' does not contain only numbers")

# Manual method
def is_only_numbers_manual(text):
    if not text:  # Empty string
        return False
    
    for char in text:
        if not char.isdigit():
            return False
    return True

print("\nUsing manual method:")
for s in test_strings:
    print(f"'{s}': {is_only_numbers_manual(s)}")
```

**Output:**
```
'12345' contains only numbers
'123abc' does not contain only numbers
'hello' does not contain only numbers
'' does not contain only numbers

Using manual method:
'12345': True
'123abc': False
'hello': False
'': False
```

---

## Problem 7: Remove Spaces from a String

**Problem:** Remove all spaces from a string and count length without spaces.

**Solution:**
```python
def remove_spaces(text):
    return text.replace(" ", "")

def count_without_spaces(text):
    return len(text.replace(" ", ""))

# Test
original = "Hello World Python Programming"
no_spaces = remove_spaces(original)
length_with_spaces = len(original)
length_without_spaces = count_without_spaces(original)

print(f"Original: '{original}'")
print(f"Without spaces: '{no_spaces}'")
print(f"Length with spaces: {length_with_spaces}")
print(f"Length without spaces: {length_without_spaces}")

# Alternative methods
def remove_spaces_join(text):
    return "".join(text.split())

def remove_spaces_loop(text):
    result = ""
    for char in text:
        if char != " ":
            result += char
    return result

print(f"Using join: '{remove_spaces_join(original)}'")
print(f"Using loop: '{remove_spaces_loop(original)}'")
```

**Output:**
```
Original: 'Hello World Python Programming'
Without spaces: 'HelloWorldPythonProgramming'
Length with spaces: 30
Length without spaces: 27

Using join: 'HelloWorldPythonProgramming'
Using loop: 'HelloWorldPythonProgramming'
```

---

## Problem 8: Convert Between String and List

**Problem:** Convert a string to a list of characters and convert a list back to a string.

**Solution:**
```python
# String to list of characters
text = "Hello"
char_list = list(text)
print(f"String: '{text}'")
print(f"List of characters: {char_list}")

# List to string
words = ["Hello", "World", "Python"]
joined_string = " ".join(words)
print(f"List: {words}")
print(f"Joined string: '{joined_string}'")

# Convert list of characters back to string
original_string = "".join(char_list)
print(f"Back to string: '{original_string}'")

# Split string into list of words
sentence = "Python is awesome"
word_list = sentence.split()
print(f"Sentence: '{sentence}'")
print(f"Word list: {word_list}")

# Split with custom separator
data = "apple,banana,orange"
fruit_list = data.split(",")
print(f"Data: '{data}'")
print(f"Fruit list: {fruit_list}")
```

**Output:**
```
String: 'Hello'
List of characters: ['H', 'e', 'l', 'l', 'o']
List: ['Hello', 'World', 'Python']
Joined string: 'Hello World Python'
Back to string: 'Hello'
Sentence: 'Python is awesome'
Word list: ['Python', 'is', 'awesome']
Data: 'apple,banana,orange'
Fruit list: ['apple', 'banana', 'orange']
```

---

## Practice Tips:

1. **Start Simple:** Begin with basic string operations like `len()`, `upper()`, `lower()`
2. **Use Built-in Methods:** Python has many helpful string methods - learn them!
3. **Practice Loops:** Many string problems require iterating through characters
4. **Test Your Code:** Always test with different inputs including edge cases
5. **Understand Indexing:** Learn how to access characters using `string[index]`
6. **Learn Slicing:** Master `string[start:end]` for extracting parts of strings

## Common String Methods to Remember:
- `len(string)` - get length
- `string.upper()` - convert to uppercase  
- `string.lower()` - convert to lowercase
- `string.split()` - split into list
- `" ".join(list)` - join list into string
- `string.replace(old, new)` - replace text
- `string.strip()` - remove whitespace
- `string.isdigit()` - check if all digits
- `string.isalpha()` - check if all letters