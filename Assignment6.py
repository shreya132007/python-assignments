"""
Develop a Library class that has instance variables like book_name , author and availability status. The class should provide methods to check out a book , return a book and display available books. Use the __init__ constructor to initialize book details for each object.
"""

class Library :
    def __init__(self , book_name , author , available=True):

        self.book_name = book_name
        self.author = author
        self.available = available

    def check_out(self) :
        if self.available :
            self.available = False
            print(f"'{self.book_name}' has been check out")
        else :
            print (f"Sorry , '{self.book_name}' is currently not available")

    def return_book(self) :
        if not self.available :
            self.available = True
            print("f'{self.book_name}' has been returned. Thank You!")
        else :
            print("f'{self.book_name}' was not chceked out")

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"Book: {self.book_name} , Author: {self.author} , Status: {status}")

# Creating library book objects
book1 = Library("The Alchemist" , "Paulo")
book2 = Library(1984 , "George")
book3 = Library("To kill a mockingbird" , "Hurger Lee")

# Display all books
book1.display_info()
book2.display_info()
book3.display_info()
print()

# Check not a book
book2.check_out()
book2.display_info()
print()

# Try to check out the same book again
book2.check_out()
print()

# Return the book
book2.return_book()
book2.display_info()

# class Library:
#     def __init__(self, book_name, author, available=True):
#         self.book_name = book_name
#         self.author = author
#         self.available = available

#     def check_out(self):
#         if self.available:
#             self.available = False
#             print(f"'{self.book_name}' has been checked out.")
#         else:
#             print(f"Sorry, '{self.book_name}' is currently not available.")

#     def return_book(self):
#         if not self.available:
#             self.available = True
#             print("f'{self.book_name}' has been returned. Thank you!")
#         else:
#             print("f'{self.book_name}' was not checked out.")

#     def display_info(self):
#         status = "Available" if self.available else "Not Available"
#         print(f"Book: {self.book_name}, Author: {self.author}, Status: {status}")


# # Creating library book objects
# book1 = Library("The Alchemist", "Paulo Coelho")
# book2 = Library("1984", "George Orwell")
# book3 = Library("To Kill a Mockingbird", "Harper Lee")

# # Display all books
# book1.display_info()
# book2.display_info()
# book3.display_info()
# print()

# # Check out a book
# book2.check_out()
# book2.display_info()
# print()

# # Try to check out the same book again
# book2.check_out()
# print()

# # Return the book
# book2.return_book()
# book2.display_info()
