class Bookshelf():
    class Book():
        def __init__(self, name, file):
            self.name = name
            self._file = file
    
        def readBook(self):
            text = open(self._file, 'r')
            print(text.read())
            text.close()
            
    library = {"Pride and Predjudice": "pandp.txt", "Grapes of Wrath": "gofw.txt"}
    
    def __init__(self):
        self._books = []
        
    
    def addBook(self, bookName):
        if bookName in self.library:
            self._books.append(self.Book(bookName, self.library[bookName]))
        else:
            print("Book not avaliable")
    
    def addAllBooks(self):
        for each in self.library:
            self.addBook(each)
    
    def removeBook(self, bookName):
        for each in self._books:
            if each.name == bookName:
                self._books.remove(each)
                return
        print(bookName, "not in bookshelf.")
    
    def getBooks(self):
        return self._books
    
    def getBookNames(self):
        bookList = []
        for each in self._books:
            bookList.append(each.name)
        return bookList

def main():
    purchased = Bookshelf()
    store = Bookshelf()
    store.addAllBooks()
    
    while(True):
        print('')
        print("1: Buy a book")
        print("2: View books")
        print("3: Read a book")
        
        action = input("What do you want to do? ")  
        print('')
        
        if(action != '1' and action !='2' and action != '3'):
            print("ERROR! That is not a valid option.")
            continue
        if(action == '1'):
            avaliableBooks = store.getBookNames()
            if len(avaliableBooks) == 0:
                print("You have bought all of the books!")
                continue
            i = 1
            for each in avaliableBooks:
                print(str(i)+":"+ each)
                i+=1
            print('')
            chosen = input("Which book would you like to buy? ")
            store.removeBook(avaliableBooks[int(chosen)-1])
            purchased.addBook(avaliableBooks[int(chosen)-1])
            print(avaliableBooks[int(chosen)-1], "bought!")
        else:
            avaliableBooks = purchased.getBookNames()
            if len(avaliableBooks) == 0:
                print("You have purchased no books!")
                continue
            for each in avaliableBooks:
                print(each)
            
            if(action == '3'):
                if len(avaliableBooks) == 1):
                    purchased.getBooks()[0].readBook()
                    return 
                bookToRead = input("Enter a book to read: ")

main()
    
    
        
    