import re

# load the book
with open("miracle_in_the_andes.txt", "r", encoding='utf-8') as file:
    book = file.read()

print(book.count("Chapter"))

pattern = re.compile("Chapter [0-9]*", re.UNICODE)
findings = re.findall(pattern, book)
print(findings)

# which are the sentences where "love" was used?
pattern = re.compile("[A-Z][^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
findings = re.findall(pattern, book)
print(findings)

# what are the most used words?
