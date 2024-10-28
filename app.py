#!/bin/python3
"""
Python program that models a simple personal
library management system.
"""
from models.library import Library
from models.member import Member
from models.book import Book


def main():
    """
    Main function
    """
    while True:
        print("Welcome to Personal Library Management System")
        print()
        print("1. admin")
        print("2. member")
        print("3. exit")
        print()
        choice = input("Enter your choice: ")
        if choice == "1":
            libName = input("Enter library name: ")
            libAddress = input("Enter library address: ")
            library = Library(libName, libAddress)
            print("Library created successfully")
            print("Library information: {}".format(library.display()))
            bookTitle = input("Enter book title: ")
            bookAuthor = input("Enter book author: ")
            book = Book(bookTitle, bookAuthor)
            print("Book added successfully")
            print("Book information: {}".format(book.display()))
            bookTitle2 = input("Enter book title: ")
            bookAuthor2 = input("Enter book author: ")
            book2 = library.searchBook(bookTitle2, bookAuthor2)
            if book2 is not None:
                print("Book found: {}".format(book2.display()))
            else:
                print("Book not found")
        if choice == "2":
            memberName = input("Enter member name: ")
            memberAddress = input("Enter member address: ")
            member = Member(memberName, memberAddress)
        if choice == "3":
            print("Exiting...")
            break
            

main()

