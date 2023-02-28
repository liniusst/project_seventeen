from typing import Dict

class Book:

    def __init__(self, title: str, author: str) -> str:
        self.title = title
        self.author = author
    
    def get_title(self):
        return "Title: " + self.title
    
    def get_author(self):
        return "Author: " + self.author
    
    def initialize(self):
        capitalized = ""
        for char in self.title:
            if char.isupper():
                capitalized += char
        return capitalized

book_one = Book(title= "Pride and Prejudice", author= "Jane Austen")
book_two = Book(title= "Hamlet", author= "William Shakespeare")
book_tree = Book(title= "War and Peace", author= "Leo Tolstoy")

print(f" {book_one.get_title()} - {book_one.get_author()} ({book_one.initialize()})" )
print(f" {book_two.get_title()} - {book_two.get_author()} ({book_two.initialize()})" )
print(f" {book_tree.get_title()} - {book_tree.get_author()} ({book_tree.initialize()})" )
