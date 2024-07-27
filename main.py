def main():    
    path = "books/frankenstein.txt"
    text = read_book(path)
    count = word_count(text)
    print(read_book(path))
    print(f"This document contains {count} words.")

def read_book(path):
    with open(path) as b:
        text = b.read()
    return text    

def word_count(text):
    count = text.split()
    return len(count)

main()