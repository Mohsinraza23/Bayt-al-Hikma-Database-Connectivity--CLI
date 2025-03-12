
import json
import os

data_file = 'library.txt'

# ✅ Load Library Data
def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

# ✅ Save Library Data
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

# ✅ Add a Book
def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of the book: ")
    genre = input("Enter the genre of the book: ")
    read = input("Have you read the book? (yes/no): ").lower() == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(new_book)
    save_library(library)
    print(f'✅ Book "{title}" added successfully.')

# ✅ Remove a Book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    updated_library = [book for book in library if book["title"] != title]

    if len(updated_library) < len(library):
        save_library(updated_library)
        print(f'🗑️ Book "{title}" removed successfully.')
    else:
        print(f'❌ Book "{title}" not found.')

# ✅ Search Books
def search_library(library):
    search_by = input("Search by (title/author): ").lower()
    if search_by not in ["title", "author"]:
        print("❌ Invalid search type. Use 'title' or 'author'.")
        return

    search_term = input(f"Enter the {search_by}: ").lower()
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "read" if book["read"] else "not read"
            print(f'📚 {book["title"]} by {book["author"]} ({book["year"]}) - {status}')
    else:
        print(f'❌ No books found matching "{search_term}".')

# ✅ Display All Books
def display_books(library):
    if not library:
        print("📭 The library is empty.")
        return

    print("\n📖 Library Collection:")
    for book in library:
        status = "read" if book["read"] else "not read"
        print(f'📘 {book["title"]} by {book["author"]} ({book["year"]}) - {status}')

# ✅ Display Statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    perc_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f'📊 Total books: {total_books}')
    print(f'📖 Books read: {read_books}')
    print(f'📈 Percentage read: {perc_read:.2f}%')

# ✅ Main Function
def main():
    library = load_library()

    while True:
        print("\n📚 Library Menu:")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search Books")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# ✅ Run the Program
if __name__ == "__main__":
    main()
