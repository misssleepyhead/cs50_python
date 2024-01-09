books = []

#Add three books to your shelf
for i in range(3):
    book = dict()
    book["title"] = input("Title: ").strip().capitalize()
    book["author"] = input("Author ").strip().capitalize()

    books.append(book)

print(books)
