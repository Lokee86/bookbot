def read_book(path):
    try:
        with open(path) as b:
            content = b.read()
    except Exception:
        print("Invalid file path: Analyzing entry instead...")
        content = path   
    characters = characters_used(content)    
    count = content.lower().split()
    return len(count), count, characters

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
    char_list = list(characters.items())
    filter_list = []
    for char, count in char_list:
        if char.isalpha():
            filter_list.append((char, count))
    def sort(filter_list):
        return filter_list[1]
    filter_list.sort(key=sort, reverse=True)
    return filter_list
    
def word_search(search_term, text):
    search_term = search_term.lower()
    count = 0
    for word in text:
        if word == search_term:
            count += 1
    return count

def main():
    while True:
        try:
            path = input("Enter a path to a text file(Enter q to quit):")
            if path == "q":
                return print("Session Ended.")
            elif path is None:
                print("Must enter a valid file path.")
                continue
            count, text, characters = read_book(path)
        except Exception as e:
            print(e)
            continue
        
        print(f"--- Begin report of {path[:25]} ---")
        print(f"{count} words found in the document")
        for char, count in print_report(characters):
            print(f"The '{char}' character was found {count} times")
        print("--- End report ---")

        while True:
            search_term = input("Search for a word search: ")
            counted_words = word_search(search_term, text)
            print(f"{counted_words} instances of {search_term}")
            
            search_again = input("Search for another word?(y/n)): ").strip().lower()
            if search_again != "y":
                break

        continue_loop = input("Do you want to analyze another file? (y/n): ").strip().lower()
        if continue_loop != "y":
            print("Session Ended")
            break

main()