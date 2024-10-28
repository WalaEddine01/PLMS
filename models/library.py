#!/bin/python3
"""
Library Model
"""

class Library:
    """
    Library class
    """

    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.members = []
        self.books = []
    
    def addMember(self, member):
        """
        Add a member
        """
        if member not in self.members:
            self.members.append(member)
        else:
            print("Member already exists")
    
    def addBook(self, book):
        """
        Add a book
        """
        if book not in self.books:
            self.books.append(book)
        else:
            print("Book already exists")
    
    def searchBook(self, title):
        """
        Search for a book
        """
        for book in self.books:
            if book.__title == title:
                print("Book found")
                return book
        print("Book not found")
        return None

    def display(self):
        """
        Display library details
        """
        print(f"Name: {self.__name}")
        print(f"Address: {self.__address}")
        print('---------------------------------')
        print("Members:")
        for member in self.members:
            member.display()
        print('---------------------------------')
        print("Books:")
        for book in self.books:
            book.display()
        print('---------------------------------')
    
    

