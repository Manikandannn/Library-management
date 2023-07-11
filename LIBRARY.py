# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 20:49:52 2023

@author: ManiKanDaN
"""
class Library:
    def __init__(self,books):
        self.books=books
        
    def list_books(self):
        print("Avialable books:")
        for book in self.books:
            print(book)
    def barrowbook(self,barrowbook):
        if barrowbook in self.books:
            print("Get your book now")
            self.books.remove(barrowbook)
        else:
            ("book not avialable")
    def recievebook(self,recievebook):
        print("you have returned the borrowed book ")
        self.books.append(recievebook)
        
books=['c','c++','python','java','css']
o=Library(books)
msg="""1.DISPLAY THE BOOKS
       2.BARROW BOOK
       3.RETURN BOOK"""
print(msg)
while True:
    ch=int(input("enter yours choice:"))
    if ch==1:
        o.list_books()
    elif ch==2:
        book=(input("enter your barrow book name:" ))
        o.barrowbook(book)
    elif ch==3:
        book=input("enter the recieve book name:")
        o.recievebook(book)
    else:
        print("thank u buddy come again")
    quit()