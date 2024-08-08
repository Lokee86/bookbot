from functools import lru_cache
import re

path = "books/frankenstein.txt"

@lru_cache
def read_book():
    #nonlocal path
    with open(path) as f:
        book = f.read()
        return book

def obtain_counts():
    chapters = 0
    lines = read_book().split("\n")
    line_count = len(lines)
    words = len(read_book().split())
    unique_words = len(set(read_book().split()))
    for line in lines:
        if line.istitle():
            chapters += 1
    return line_count, words, unique_words, chapters

@lru_cache
def count_characters():
    character_counts = {}
    for character in read_book():
        if character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    return sorted(list(character_counts.items()), key=lambda x: x[1], reverse=True)

@lru_cache
def count_words():
    word_counts = {}
    for character in read_book().split():
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return sorted(list(word_counts.items()), key=lambda x: x[1], reverse=True)

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
            case _:
                print("Invalid Option, Please Choose a Valid Option.")
                return
    

def main():
    print_lists(1)
    print_lists(2)
    print_lists(3)
    print_lists(4)
    print_lists(5)
    print_lists(6)

main()