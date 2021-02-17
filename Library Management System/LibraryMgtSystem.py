class Library():
    def __init__(self,list_of_books, library_name):
        self.list_of_books=list_of_books
        self.lirary_name=library_name
        self.lendDict={}

    def displayBooks(self):
        print (f"Welcome To {self.lirary_name} books are")
        for book in self.list_of_books:
            print (book)
    def lendbook(self,user,book):
        if book not  in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Book is Available and You can Take it")
        else:
            print(f"This book is Already in use of {self.lendDict[book]}")

    def addBook(self,name_of_book):
        self.list_of_books.append(name_of_book)
        return f"{self.name_of_book} is added successfully"

    def returnBook(self,book):
        self.lendDict.pop(book)
        print ("Book is returned..")

if __name__ == '__main__':
    saim= Library(['Python','Harry Potter','One Last Hope','Come Fly'], "Saim")
    while(True):
        print(f"Welcome To {saim.lirary_name} Library\n Enter your choice... ")
        print("1. for Display Book")
        print("2. for Lend Book")
        print("3. for Add Book")
        print("4. for Return Book")
        choice1=int(input())
        if choice1==1:
            saim.displayBooks()
        elif choice1==2:
            name=input("Enter Your Name\n")
            book=input("Enter Book\n")
            saim.lendbook(name,book)
        elif choice1==3:
            bookname=int("Enter Name of book")
            saim.addBook(bookname)
        elif choice1==4:
            bookname =input("Enter Name of book\n")
            saim.returnBook(bookname)
        else:
            print("Invalid Choice")

        print("Enter c to continue and q to quit")
        choice2=input()
        while choice2 != "c" and choice2 != "q":
            if choice2=="c":
                continue
            elif choice2=="q":
                exit()

