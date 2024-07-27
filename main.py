def main():    
    def read_book():
        with open("books/frankenstein.txt") as b:
            book_contents = b.read()
        return book_contents    

    print(read_book())

    def word_count():
        count = read_book().split()
        return len(count)

    print(word_count())

main()