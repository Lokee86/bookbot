from functools import lru_cache
from contextlib import redirect_stdout

# path is read and the results cached
@lru_cache
def read_book():
    #path variable is globalized in main()
    global file_name
    if path.split(".")[-1] == "txt":
        try:
            with open(path) as f:
                book = f.read()
                file_name = path.split("/")[-1]
        except Exception:
            print("Invalid file path, analyzing entry instead")
            book = path
            file_name = "Input String"
    else:
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
def character_lists(option = True):
    upper_chars = []
    lower_chars = []
    number_chars = []
    other_chars = []
    invis_chars = []
    for character in count_characters(option):
        if character[0].isalpha() and character[0].isupper():
            upper_chars.append(character)
        elif character[0].isalpha() and character[0].islower():
            lower_chars.append(character)
        elif character[0].isdecimal():
            number_chars.append(character)
        elif character[0] != " " and character[0] != "\n":
            other_chars.append(character)
        else:
            invis_chars.append(character)
    return upper_chars, lower_chars, number_chars, other_chars, invis_chars

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

# allows for a choice of output report
def choose_report():
    print("""    
    1. All uppercase letters and their frequency.
    2. All lowercase letters and their frequency.
    3. All numerals and their frequency.
    4. All non-alphanumeric ASCII characters and their frequency.
    5. All spaces and newline characters (returns) and their frequency.
    6. All unique words and their frequency. (Recommend outputting to file"
    7. All letters and their frequency.
    8. All of the above choices. (Excluding #7)
    """)
    return input("Please choose what you would like to report from the above list. (May only choose 1) ")

# produces an output based on the selected option
def print_data(option = 8, order = True):
    read_book()
    print(f"----------------Beginning Report of {file_name}----------------------")
    print(f"There are {obtain_counts()[0]} lines of text, {obtain_counts()[1]} words\n{obtain_counts()[2]} unique words, and {obtain_counts()[3]} title lines\nin the document.")
    match int(option):
        case 1:
            for letter in character_lists(order)[0]:
                print(f"The uppercase letter '{letter[0]}' appears {letter[1]} times.")
        case 2:
            for letter in character_lists(order)[1]:
                print(f"The lowercase letter '{letter[0]}' appears {letter[1]} times.")
        case 3:
            for number in character_lists(order)[2]:
                print(f"The number '{number[0]}' appears {number[1]} times.")
        case 4:
            for char in character_lists(order)[3]:
                print(f"The character '{char[0]}' appears {char[1]} times.")
        case 5:
            for char in character_lists(order)[4]:
                if char[0] == " ":
                    print(f"There are {char[1]} spaces.")
                else:
                    print(f"There are {char[1]} newline characters or returns.")
        case 6:
            for word in count_words(order)[0]:
                if word[0] == "i":
                    print(f"The word 'I' was used {word[1]} times.")
                else:
                    print(f"The word '{word[0]}' was used {word[1]} times.")
        case 7:
            for letter in all_letter_counts(order):
                print(f"The letter '{letter[0]}' appears {letter[1]} times.")
        case 8:
            for index, ls in enumerate(character_lists(order)):
                for letter in ls:
                    match index:
                        case 0: print(f"The uppercase letter '{letter[0]}' appears {letter[1]} times.")
                        case 1: print(f"The lowercase letter '{letter[0]}' appears {letter[1]} times.")
                        case 2: print(f"The number '{letter[0]}' appears {letter[1]} times.")
                        case 3: print(f"The character '{letter[0]}' appears {letter[1]} times.")
                        case 4: 
                            if letter[0] == " ":
                                print(f"There are {letter[1]} spaces.")
                            else:
                                print(f"There are {letter[1]} newline characters or returns.")
            for word in count_words(order)[0]:
                if word[0] == "i":
                    print(f"The word 'I' was used {word[1]} times.")
                else:
                    print(f"The word '{word[0]}' was used {word[1]} times.")
    print("---------------------------End of Report--------------------------------")

# creates and output file with a given or default name, will add numerical suffix if file exists
def output_file(option, option2 = True, name_file = "report", suffix = 0):
    if suffix == 0:
        file_name = f"{name_file}.txt"
    else:  
        file_name = f"{name_file}({suffix}).txt"
        
    try:
        with open(file_name, "x") as file:
            with redirect_stdout(file):
                print_data(option, option2)
            return "File created"
    except FileExistsError:
        output_file(option, option2, name_file, suffix + 1)
    except OSError as e:
        print("An OSError occured: " + e)
        return

# searches the input for instances of any word, case insensitive
def search(term):
    if term.lower().strip() in count_words()[1]:
        print(f"The word '{term}' occurs {count_words()[1][term]} times.")
    else:
        print(f"The word '{term}' could not be found.")
    return

def main():
    global path
    
    while True:
        path = input("Please enter a path to a .txt file or enter a string to analyze: ").replace("\\", "/")
        alpha_freq = input("Would you like to sort the results alphabetically (1), or by frequency (2)? ")
        while True:        
            match alpha_freq:
                case "1":
                    alpha_freqtf = False
                    break
                case "2":
                    alpha_freqtf = True
                    break
                case _:
                    alpha_freq = input("Please enter a valid option. (1 or 2)")
                    continue
        
        report = choose_report()
        while True:
            try:
                if not 8 >= int(report) >= 1:
                    report = input("Please choose a valid option. ")
                    continue
                else:
                    break
            except ValueError:
                report = input("Please choose a valid option. ")
                continue
            

        write_file  = input("Would you like to write the results of this report to a seperate file? (y/N) ").lower().strip()
        if write_file != "y":
            print_data(report, alpha_freqtf)
        elif write_file == "y":
            file_name = input("Please choose a name for the report file. (Default is 'report') ").strip()
            if file_name == "":
                print_data(report, alpha_freqtf)
                output_file(report, alpha_freqtf)
            else:
                print_data(report, alpha_freqtf)
                output_file(report, alpha_freqtf, file_name)

        search_inquiry = input("Would you like to search for a word in the document? (y/N) ").lower().strip()
        if search_inquiry != "y":
            pass
        else:
            search(input("Enter word to search for: ").lower().strip())
            while True:
                another_search = input("Continue searching? (y/N) ")
                if another_search != "y":
                    break
                else:
                    search(input("Enter another word to search for: ").lower().strip())
                    continue
        
        continue_on = input("Would you like to process another document? (y/N) ").lower().strip()
        if continue_on == "y":
            clear_cache()
            continue
        else:
            print("Session Ended. Thank you for using Bookbot!")
            return
        
if __name__ == "__main__":
    main()
