#libarary management system using class and file handling
import os
class EmptyLibraryException(Exception):
    pass
class Book:
    def __init__(self, title, author, status='available'):
        self.title=title
        self.author=author
        self.status=status
class Library:
    def __init__(self,filename='library.txt'):
        self.filename=filename
        self.books=[]
        self.loadbooks()
    def loadbooks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    parts=line.strip().split(',')
                    if len(parts)==3:
                        title, author, status = parts
                        self.books.append(Book(title, author, status))
    def savebooks(self):
        with open(self.filename, 'w') as file:
            for book in self.books:
                file.write(f'{book.title},{book.author},{book.status}\n')
    def addbook(self, title, author):
        new_book=Book(title, author)
        self.books.append(new_book)
        self.savebooks()
        print(f'Book "{title}" by {author} added to the library.')
    def removebook(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                self.savebooks()
                print(f'Book "{title}" removed from the library.')
                return
        print(f'Book "{title}" not found in the library.')
    def borrowbook(self, title):
        for book in self.books:
            if book.title==title:
                if book.status=='available':
                    book.status='borrowed'
                    self.savebooks()
                    print(f'You have borrowed "{title}".')
                    return
                else:
                    print(f'Sorry, "{title}" is currently borrowed.')
                    return
        print(f'Book "{title}" not found in the library.')
    def returnbook(self, title):
        for book in self.books:
            if book.title==title:
                if book.status=='borrowed':
                    book.status='available'
                    self.savebooks()
                    print(f'You have returned "{title}".')
                    return
                else:
                    print(f'Book "{title}" was not borrowed.')
                    return
        print(f'Book "{title}" not found in the library.')
    def displaybooks(self):
        if not self.books:
            raise EmptyLibraryException('The library is empty.')
        print('Books in the library:')
        for book in self.books:
            status = 'Available' if book.status == 'available' else 'Borrowed'
            print(f'Title: {book.title}, Author: {book.author}, Status: {status}')
library = Library()
library.addbook('The Great Gatsby', 'F. Scott Fitzgerald')
library.addbook('1984', 'George Orwell')
library.removebook('1984')
library.removebook('The Great Gatsby')
library.displaybooks()


