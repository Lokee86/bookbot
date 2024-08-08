from functools import lru_cache

# path is read and the results cached
@lru_cache
def read_book():
    #path argument is globalized in main()
    global file_name
    try:
        with open(path) as f:
            book = f.read()
            file_name = path.split("/")[-1]
    except Exception:
        print("Invalid file path, analyzing entry instead")
        book = path
        file_name = "Input String"
    return book

# obtain and cache counts for line, words, unique words, and the number of title lines present
@lru_cache
def obtain_counts():
    chapters = 0
    lines = read_book().split("\n")
    line_count = len(lines)
    words = len(read_book().split())
    unique_words = len(set(count_words()[0]))
    for line in lines:
        if line.istitle():
            chapters += 1
    return line_count, words, unique_words, chapters

# create and cache an ordered list of (character, count) tuples
# True option returns list sorted in descending order by count value
# False option returns list sorted alphabetically by character value
@lru_cache
def count_characters(option = True):
    character_counts = {}
    for character in read_book():
        if character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    if option:
        return sorted(list(character_counts.items()), key=lambda x: x[1], reverse=True)
    return sorted(list(character_counts.items()), key=lambda x: x[0])

# create and cache an ordered list of (WORD, count) tuples
# functions as above
@lru_cache
def count_words(option = True):
    word_counts = {}
    stripping_chars = ""
    for char in character_lists()[3]:
        stripping_chars += char[0]
    for word in read_book().split():
        if "." not in word:
            stripped_word = word.lower().strip(stripping_chars)
            if stripped_word not in word_counts:
                word_counts[stripped_word] = 1
            else:
                word_counts[stripped_word] += 1
    if option:
        return sorted(list(word_counts.items()), key=lambda x: x[1], reverse=True), word_counts
    return sorted(list(word_counts.items()), key=lambda x: x[0]), word_counts

# sorts and caches counted characters into seperate lists of numbers, letters,
# ASCII characters, and invisible characters (spaces and newlines)
@lru_cache
def character_lists():
    upper_chars = []
    lower_chars = []
    number_chars = []
    other_chars = []
    invis_chars = []
    for character in count_characters():
        if character[0].isalpha() and character[0].isupper():
            upper_chars.append(character)
        elif character[0].isalpha():
            lower_chars.append(character)
        elif character[0].isdecimal():
            number_chars.append(character)
        elif character[0] != " " and character[0] != "\n":
            other_chars.append(character)
        else:
            invis_chars.append(character)
    return upper_chars, lower_chars, number_chars, other_chars, invis_chars,

# combines upper and lower case, returns total counts
def all_letter_counts(option = True):
    total_letters = {}
    for char in count_characters():
        if char[0].isalpha():
            lower = char[0].lower()
            if lower not in total_letters:
                total_letters[lower] = char[1]
            else:
                total_letters[lower] += char[1]
    if option:
        return sorted(list(total_letters.items()), key=lambda x: x[1], reverse=True)
    return sorted(list(total_letters.items()), key=lambda x: x[0]) 

# clears lru_caches when the program is reset
def clear_cache():
    cache_list = [read_book, obtain_counts, count_characters, count_words, character_lists]
    for func in cache_list:
        func.cache_clear()

# produces an output based on the selected option
def print_data(option = True):
    read_book()        
    print(f"-----------------Beginning Report of {file_name}-----------------------")
    print(f"There are {obtain_counts()[0]} lines of text, {obtain_counts()[1]} words\n{obtain_counts()[2]} unique words, and {obtain_counts()[3]} title lines\nin the document.")
    match option:
        case 1:
            for letter in character_lists()[0]:
                print(f"The uppercase letter '{letter[0]}' appears {letter[1]} times.")
        case 2:
            for letter in character_lists()[0]:
                print(f"The uppercase letter '{letter[0]}' appears {letter[1]} times.")
        case 3:
            for number in character_lists()[2]:
                print(f"The number '{number[0]}' appears {number[1]} times.")
        case 4:
            for char in character_lists()[3]:
                print(f"The character '{char[0]}' appears {char[1]} times.")
        case 5:
            for char in character_lists()[4]:
                if char[0] == " ":
                    print(f"There are {char[1]} spaces.")
                else:
                    print(f"There are {char[1]} newline characters or returns.")
        case 6:
            for word in count_words()[0]:
                if word[0] == "i":
                    print(f"The word 'I' was used {word[1]} times.")
                else:
                    print(f"The word '{word[0]}' was used {word[1]} times.")
        case 7:
            for letter in all_letter_counts(option):
                print(f"The letter '{letter[0]}' appears {letter[1]} times.")
        # Code is repeated here, because I determined it would take the same amount of code to avoid repeating it.
        case 8:
            for letter in character_lists()[0]:
                    print(f"The letter '{letter[0]}' appears {letter[1]} times.")
            for number in character_lists()[2]:
                    print(f"The number '{number[0]}' appears {number[1]} times.")
            for char in character_lists()[3]:
                    print(f"The character '{char[0]}' appears {char[1]} times.")
            for char in character_lists()[4]:
                if char[0] == " ":
                    print(f"There are {char[1]} spaces.")
                else:
                    print(f"There are {char[1]} newline characters or returns.")
            for word in count_words()[0]:
                if word[0] == "i":
                    print(f"The word 'I' was used {word[1]} times.")
                else:
                    print(f"The word '{word[0]}' was used {word[1]} times.")
        case _:
                print("Invalid Option, Please Choose a Valid Option.")
                return
    print("---------------------------End of Report--------------------------------")

def output_file():
    pass

def search(term):
    if term in count_words()[1]:
        print(f"The word '{term}' occurs {count_words()[1][term]} times.")
    else:
        print(f"The word '{term}' could not be found.")

def main():
    global path
    path = "books/frankenstein.txt"
    #path = input("Enter Path:").replace("\\", "/")
    print_data(1)

main()