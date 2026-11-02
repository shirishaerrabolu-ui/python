books = {
    "Harry Potter": "Available",
    "Python Basics": "Issued",
    "Maths": "Available"
}

while True:
    name = input("\nEnter book name (or exit): ")

    if name == "exit":
        break
    elif name in books:
        print(name, ":", books[name])
    else:
        print("Book not found!")