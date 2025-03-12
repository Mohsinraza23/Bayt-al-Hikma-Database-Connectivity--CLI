# Library Management System

## 📌 Overview
This is a simple **Library Management System** built using **Python** that allows users to:

✅ Add books  
✅ Remove books  
✅ Search books  
✅ Display books  
✅ Show statistics  

## 🛠 Technologies Used
- Python
- JSON (for storing data)
- OS module (for file handling)

## 📥 Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/library-management.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd library-management
   ```
3. **Run the script**:
   ```bash
   python library.py
   ```

---

## 📌 Step-by-Step Explanation

### 🛠 Step 1: Import Required Modules
```python
import json
import os
```
- `json` → Stores and retrieves data in JSON format.
- `os` → Checks if the file (library.txt) exists before reading it.

### 🗂 Step 2: Define the Data File
```python
data_file = 'library.txt'
```
- This file stores book data.
- The program reads from and writes to this file.

### 📥 Step 3: Load Library Data
```python
def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []
```
📌 **Functionality:**
- Checks if `library.txt` exists.
- Loads data if the file exists; returns an empty list otherwise.

### 💾 Step 4: Save Library Data
```python
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)
```
📌 **Functionality:**
- Saves the updated book list to `library.txt` in JSON format.

### ➕ Step 5: Add a Book
```python
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
```
📌 **Functionality:**
- Takes book details as input.
- Saves the new book to the library.

### 🗑️ Step 6: Remove a Book
```python
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    updated_library = [book for book in library if book["title"] != title]

    if len(updated_library) < len(library):
        save_library(updated_library)
        print(f'🗑️ Book "{title}" removed successfully.')
    else:
        print(f'❌ Book "{title}" not found.')
```
📌 **Functionality:**
- Removes a book based on title input.

### 🔍 Step 7: Search for Books
```python
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
```
📌 **Functionality:**
- Searches books by title or author.
- Displays matching results.

### 📖 Step 8: Display All Books
```python
def display_books(library):
    if not library:
        print("📭 The library is empty.")
        return

    print("\n📖 Library Collection:")
    for book in library:
        status = "read" if book["read"] else "not read"
        print(f'📘 {book["title"]} by {book["author"]} ({book["year"]}) - {status}')
```
📌 **Functionality:**
- Displays all books in the library.

### 📊 Step 9: Display Statistics
```python
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    perc_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f'📊 Total books: {total_books}')
    print(f'📖 Books read: {read_books}')
    print(f'📈 Percentage read: {perc_read:.2f}%')
```
📌 **Functionality:**
- Shows total books, books read, and percentage read.

### 🚀 Step 10: Main Menu System
```python
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
```
📌 **Functionality:**
- Provides an interactive menu for managing the library.

### 🏁 Step 11: Start the Program
```python
if __name__ == "__main__":
    main()
```
📌 **Functionality:**
- Runs the program only when executed directly.

---

## 🔥 Summary
📌 This **Library Management System** allows users to manage their book collection easily. It supports adding, removing, searching, displaying, and analyzing books stored in a JSON file.

🚀 **Now, run the script and start managing your library!**

---

## 🏆 Author
[Your Name](https://github.com/Mohsinraza23)

📧 Contact: 03452615590

