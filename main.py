with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    words = file_contents.split()
    count = 0
    alphabet = {}
    for word in words:
        count += 1
    print(count)

