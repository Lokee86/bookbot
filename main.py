path = "books/frankenstein.txt"

def read_book():
    with open(path) as f:
        book = f.read()
        return book

def obtain_counts(book):
    chapters = 0
    lines = book.split("\n")
    line_count = len(lines)
    words = len(book.split())
    unique_words = len(set(book.split()))
    for line in lines:
        if line.istitle():
            chapters += 1
    return line_count, words, unique_words, chapters


print(obtain_counts(read_book()))