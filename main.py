def main():
    text = read_file(path)
    words = count_words(text)
    character_dictionary = create_dictionary(text)
    alphabet_dictionary = remove_nonalpha(character_dictionary)
    print("--- Begin report of {} ---".format(path))
    print("{} words found in the document".format(words))
    print_dict(alphabet_dictionary)
    print("--- End Report ---")

def read_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents.split()

def count_words(text):
    return len(text)

def create_dictionary(words):
    character = {}
    for word in words:
        for c in word:
            lowerc = c.lower()
            if lowerc in character:
                character[lowerc] += 1
            else:
                character[lowerc] = 1
    return character

def sort_on(x):
    return x["value"]

def remove_nonalpha(dict):
    sorted = []
    for ch in dict:
        if ch.isalpha():
            sorted.append({"char":ch, "value":dict[ch]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def print_dict(dict):
    for dict in dict:
        print("The '{}' character was found {} times".format(dict["char"], dict["value"]))

path = 'books/frankenstein.txt'

main()


