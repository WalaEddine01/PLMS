#!/bin/python3
"""
Book Model
"""

class Book:
    """
    Book class
    """
    
    def __init__(self, title, author, editer):
        self.__title = title
        self.__author = author
        self.__editer = editer
    
    def display(self):
        """
        Display book details
        """
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Editer: {self.__editer}")
        print()
