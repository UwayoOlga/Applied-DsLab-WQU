#Write a program that takes a sentence from the user and counts how many words it contains

def count_words(sentence):

    words = sentence.split()
    
    return len(words)