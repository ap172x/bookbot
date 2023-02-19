with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    words = file_contents.split()
    count = 0
    alphabet = {}
    for word in words:
        count += 1
        for letter in word:
            x = letter.lower()
            if x in alphabet:
                alphabet[x] += 1
            else:
                alphabet[x] = 1
    print(count)
    print(alphabet)

