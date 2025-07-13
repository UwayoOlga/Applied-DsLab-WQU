# Function to process and return list of characters
def get_characters_from_texts(text1, text2):
    combined_text = text1 + text2
    char_list = [char for char in combined_text]
    return char_list

# Main program
def main():
    text1 = input("Enter first text: ")
    text2 = input("Enter second text: ")
    
    characters = get_characters_from_texts(text1, text2)
    print("List of characters from combined text:", characters)
    
    print("\nThank you for using my application after processing the input.")

 
