from functools import lru_cache

@lru_cache
def read_book():
    #path argument is globalized in main()
    with open(path) as f:
        book = f.read()
        return book

@lru_cache
def obtain_counts():
    chapters = 0
    lines = read_book().split("\n")
    line_count = len(lines)
    words = len(read_book().split())
    unique_words = len(set(read_book().lower().split()))
    for line in lines:
        if line.istitle():
            chapters += 1
    return line_count, words, unique_words, chapters

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

@lru_cache
def count_words(option = True):
    word_counts = {}
    stripping_chars = ""
    for char in character_lists()[2]:
        stripping_chars += char[0]
    for word in read_book().split():
        stripped_word = word.lower().strip(stripping_chars)
        if stripped_word not in word_counts:
            word_counts[stripped_word] = 1
        else:
            word_counts[stripped_word] += 1
    if option:
        return sorted(list(word_counts.items()), key=lambda x: x[1], reverse=True)
    return sorted(list(word_counts.items()), key=lambda x: x[1])

@lru_cache
def character_lists():
    alpha_chars = []
    number_chars = []
    other_chars = []
    invis_chars = []
    for character in count_characters():
        if character[0].isalpha():
            alpha_chars.append(character)
        elif character[0].isdecimal():
            number_chars.append(character)
        elif character[0] != " " and character[0] != "\n":
            other_chars.append(character)
        elif character[0] == " " or character[0] == "\n":
            invis_chars.append(character)


    return alpha_chars, number_chars, other_chars, invis_chars

def print_lists(option):
        match option:
            case 1:
                for letter in character_lists()[0]:
                    print(f"The letter '{letter[0]}' appears {letter[1]} times.")
            case 2:
                for number in character_lists()[1]:
                    print(f"The letter '{number[0]}' appears {number[1]} times.")
            case 3:
                for char in character_lists()[2]:
                    print(f"The letter '{char[0]}' appears {char[1]} times.")
            case 4:
                for char in character_lists()[3]:
                    if char[0] == " ":
                        print(f"There are {char[1]} spaces.")
                    else:
                        print(f"There are {char[1]} newline characters or returns.")
            case 5:
                for word in count_words():
                    if word[0] == "i":
                        print(f"The word 'I' was used {word[1]} times.")
                    else:
                        print(f"The word '{word[0]}' was used {word[1]} times.")
            #Code is repeated here, because I determined it would take the same amount of code to avoid repeating it.
            case 6:
                for letter in character_lists()[0]:
                    print(f"The letter '{letter[0]}' appears {letter[1]} times.")
                for number in character_lists()[1]:
                    print(f"The number '{number[0]}' appears {number[1]} times.")
                for char in character_lists()[2]:
                    print(f"The character '{char[0]}' appears {char[1]} times.")
                for char in character_lists()[3]:
                    if char[0] == " ":
                        print(f"There are {char[1]} spaces.")
                    else:
                        print(f"There are {char[1]} newline characters or returns.")
                for word in count_words():
                    if word[0] == "i":
                        print(f"The word 'I' was used {word[1]} times.")
                    else:
                        print(f"The word '{word[0]}' was used {word[1]} times.")
            case _:
                print("Invalid Option, Please Choose a Valid Option.")
                return

def print_stats():
    print(
        f"There are {obtain_counts()[0]} lines of text, {obtain_counts()[1]} words\n{obtain_counts()[2]} unique words, and {obtain_counts()[3]} title lines\nin the document."
          )    

def main():
    global path
    path = "books/frankenstein.txt"
    #path = input("Enter Path:").replace("\\", "/")
    file_name = path.split("/")[-1]
    print_stats()
    print(character_lists())

main()