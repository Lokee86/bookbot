#Add feature to allow for searching for the number of times any given word is used.
#should return 0 if none are found.

def path_input():
    path = input("Enter a path to a text file(Enter q to quit):").strip().lower()
    if path == "":
        raise ValueError("No path entered. Must enter a valid file path.")
    elif path.lower() == "q":
        return None
    else:
        return path

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

def print_report(characters):
    char_list = []
    for c in characters:
        char_list.append((c, characters[c]))
    filter_list = char_list[:]
    for char, count in char_list:
        if not char.isalpha():
            filter_list.remove((char, count))
    def sort(filter_list):
        return filter_list[1]
    filter_list.sort(key=sort, reverse=True)
    return filter_list
    
def word_search(search_term, text):
    count = 0
    search_text = [word.lower() for word in text.split()]
    for word in search_text:
        if word == search_term:
            count += 1
    return count, search_term

def main():
    while True:
        try:
            path = path_input().strip().lower()
            if path is None:
                return print("Session Ended")
            try:
                text = read_book(path)
            except FileNotFoundError:
                print(f"An error occured: Bad path or file does not exist.")
                return print("Session Ended")
        except ValueError as e:
            print(e)
            return print("Session Ended") 
        except Exception as e:
            print(f"An error occured:{e}")
            return print("Session Ended")
        
        count = word_count(text)
        characters = characters_used(text)
        
        print(f"--- Begin report of {path} ---")
        print(f"{count} words found in the document")
        
        for char, count in print_report(characters):
            print(f"The '{char}' character was found {count} times")
    
        print("--- End report ---")

        while True:
            search_term = input("Search for a word search: ").strip().lower()
            counted_words, search_term = word_search(search_term, text)
            print(f"{counted_words} instances of {search_term}")
            
            search_again = input("Search for another word?(y/n)): ").strip().lower()
            if search_again != "y":
                break

        continue_loop = input("Do you want to analyze another file? (y/n): ").strip().lower()
        if continue_loop != "y":
            print("Session Ended")
            break

main()