# -*- coding: utf-8 -*-
"""
@author: Kandidatnr: 77
Question 2.
"""

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self._checked_out = False
    
    def is_available(self):
        return not self._checked_out
    
    # If the book is checked out, mark it as available (True).  
    # If not, return as not available (False)
    def check_in(self):
        if self._checked_out:
            self._checked_out = False
            return True
        return False
    
    def check_out(self):
        if not self._checked_out:
            self._checked_out = True
            return True
        return False
    

class Library:
    def __init__(self):
        self._books = []
        
    def add_book(self, book):
        self._books.append(book)
        print(f'Added "{book.title}" to library')
        
    def remove_book(self, title):
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                print(f'Removed "{title}" from library')
                return
        print(f'"{title}" not found')
        
    def check_in(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_in():
                    print(f'Checked in "{title}"')
                else:
                    print(f'Book "{title}" was not checked out')
                return
        print(f'Book "{title}" was not found')        
        
    def check_out(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f'Checked out "{title}"')
                    return
                else:
                    print(f'"{title}" is already checked out')
                return
        print(f'"{title}" not found')
            
    def show_books(self):
        if not self._books:
            print("No books in the library")
            return
        print("\nTitles in the library:")
        for i in range(len(self._books)):
            book = self._books[i]
            print(f'{i+1}. "{book.title}" by {book.author}')
            

def test_script():
    test_library = Library()
    
    books = [
        Book("Tomorrow, and Tomorrow, and Tomorrow", "Gabrielle Zevin", 401),
        Book("My Year of Rest and Relaxation", "Ottessa Moshfegh", 304),
        Book("Beautiful World, Where Are You", "Sally Rooney", 337)
        ]
        
    for book in books:
        test_library.add_book(book)
        
    print("\nTesting check out:")
    test_library.check_out("Beautiful World, Where Are You")
    test_library.check_out("Beautiful World, Where Are You")
    test_library.check_out("Unknown Book")
    
    print("\nTesting check in:")
    test_library.check_in("Beautiful World, Where Are You")
    test_library.check_in("Beautiful World, Where Are You")
    test_library.check_in("Unknown Book")
    
    print("\nTesting removal:")
    test_library.remove_book("My Year of Rest and Relaxation")
    test_library.remove_book("Unknown Book")
    
    print("\nTesing show books:")
    test_library.show_books()
    
test_script()