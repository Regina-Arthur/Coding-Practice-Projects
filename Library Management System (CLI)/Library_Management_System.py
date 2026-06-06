# =====================================
# LIBRARY MANAGEMENT SYSTEM
# =====================================

# STEP 1: Create a welcome message
# ---------------------------------
# Display a title for the program.
#
# Python concepts:
# - print()


# STEP 2: Create the main data storage
# ------------------------------------
# Create a dictionary to store books.
#
# Each book should have:
# - title
# - author
# - available copies
#
# Research:
# - dictionaries
# - nested dictionaries
#
# Example idea:
# books = {
#     "Book Title": {
#         "author": "...",
#         "copies": ...
#     }
# }


# STEP 3: Create storage for borrowed books
# -----------------------------------------
# Create a structure that tracks:
# - who borrowed a book
# - what book they borrowed
#
# Research:
# - dictionaries
# - lists inside dictionaries


# STEP 4: Create the main menu
# ----------------------------
# Continuously display:
#
# 1. Add Book
# 2. View Books
# 3. Borrow Book
# 4. Return Book
# 5. View Borrowed Books
# 6. Exit
#
# Ask the user for a choice.
#
# Research:
# - while loops
# - input()
# - if/elif/else


# STEP 5: Add a book
# ------------------
# Ask the user for:
# - title
# - author
# - number of copies
#
# Store the information in the books dictionary.
#
# Research:
# - dictionary assignment
# - nested dictionaries
# - int()


# STEP 6: Display all books
# -------------------------
# Show all books in a table.
#
# Columns:
# - Title
# - Author
# - Copies Available
#
# Research:
# - for loops
# - dictionary.items()
# - f-string formatting
# - alignment (<15, >15, etc.)


# STEP 7: Borrow a book
# ---------------------
# Ask:
# - user name
# - book title
#
# Check:
# - does the book exist?
# - are copies available?
#
# If yes:
# - decrease available copies
# - record that the user borrowed the book
#
# Research:
# - dictionary lookup
# - membership testing (in)
# - updating dictionary values


# STEP 8: Prevent invalid borrowing
# ---------------------------------
# Handle situations where:
# - book does not exist
# - no copies remain
#
# Display helpful messages.
#
# Research:
# - if statements
# - comparison operators


# STEP 9: Return a book
# ---------------------
# Ask:
# - user name
# - book title
#
# Check:
# - did this user actually borrow the book?
#
# If yes:
# - increase available copies
# - remove the book from their borrowed list
#
# Research:
# - list.remove()
# - dictionary updates


# STEP 10: View borrowed books
# ----------------------------
# Display:
# - each user
# - books they currently have
#
# Research:
# - dictionary.items()
# - nested loops


# STEP 11: Search for a book
# --------------------------
# Ask for a title.
#
# If found:
# - display details
#
# Research:
# - dictionary membership
# - string methods


# STEP 12: Display statistics
# ---------------------------
# Show:
# - total books in library
# - total available copies
# - total borrowed books
#
# Research:
# - counters
# - loops
# - accumulation variables


# STEP 13: Exit the program
# -------------------------
# Allow the user to leave the application safely.
#
# Research:
# - break
# - while loops