import string
def caesar(text):
    text = text.lower()
    abc = string.ascii_lowercase
    abclist = []
    for letter in abc:
        abclist.append(letter)
    texts = text.split(" ")
    letterlist = []
    for text in texts:
        for letter in text:
            letterlist.append(abclist.index(letter + 1))
    text = ""
    for letter in letterlist:
        text.join(letter)
    return text
if __name__ == "__main__":
    print(caesar(text="Hallo Welt"))
