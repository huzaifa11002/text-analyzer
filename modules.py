def words_counter(text):
    words = text.split()
    num_words = len(words)
    return num_words

def char_counter(text):
    num_chars = len(text)
    return num_chars

def vowels_counter(text):
    vowels = sum([1 for char in text if char.lower() in "aeiou"])
    return vowels

def title_case(text):
    title_case = text.title()
    return title_case

def lower_case(text):
    lower_case = text.lower()
    return lower_case

def upper_case(text):
    upper_case = text.upper()
    return upper_case