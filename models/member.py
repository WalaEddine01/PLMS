#!/bin/python3
"""
Member Model
"""
import datetime
from uuid import uuid4
from .book import Book

class Member:
    """
    Member class
    """

    def __init__(self, name, age, address):
        self.__id = uuid4()
        self.__name = name
        self.__age = age
        self.__address = address
        self.books = []
        self.__registeredAt = datetime.datetime.now()
    
    def borrow(self, book):
        """
        Borrow a book
        """
        if isinstance(book, Book):
            self.__books.append(book)
            self.__lastUpdatedAt = datetime.datetime.now()
        else:
            print("Invalid book")
    
    def disply(self):
        """
        Display member details
        """
        print(f"ID: {self.__id}")
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Address: {self.__address}")

