path = "books/frankenstein.txt"

def read_book():
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

def count_characters():
    character_counts = {}
    for character in read_book():
        if character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    return sorted(list(character_counts.items()), key=lambda x: x[1], reverse=True)

def character_lists():
    alpha_chars = []
    number_chars = []
    other_chars = []
    for character in count_characters():
        if character[0].isalpha():
            alpha_chars.append(character)
        elif character[0].isdecimal():
            number_chars.append(character)
        elif character[0] != " " and character[0 != "\n"]:
            other_chars.append(character)
    return alpha_chars, number_chars, other_chars

print(obtain_counts())
print(count_characters())
print (character_lists())