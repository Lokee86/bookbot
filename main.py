def main():    
    path = "books/frankenstein.txt"
    text = read_book(path)
    count = word_count(text)
    characters = characters_used(text)
    print(read_book(path))
    print(f"This document contains {count} words.")
    print(characters)

def read_book(path):
    with open(path) as b:
        text = b.read()
    return text    

def word_count(text):
    count = text.split()
    return len(count)

def characters_used(text):
    counted_characters = {}
    text = text.lower()
    for c in text:
        if c in counted_characters:
            counted_characters[c] += 1
        else:
            counted_characters[c] = 1
    return counted_characters


main()