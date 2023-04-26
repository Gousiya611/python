class Library:
    books=['the wings of fire', 'geetanjali']
    booksandauthor={'the wings of fire':'Dr.A.P.J.Abdul Kalam','Geetanjali':'Rabindranath Tagor'}
    subscribers=['gousiya','ameen']
    availablebooks=['the wings of fire']
    authors=['Dr.A.P.J.Abdul Kalam','Rabindranath tagore']
    author_book={"pablo":["escobar","escobar returns","escobar part3"]
                 }
    def getAllBooks(namebook):
        
        print(books)
#pass
    def addBooks():
        books.append(input())
        print(books)
        #pass
    def getBookByAuthorName():
        for key in author_book:
            if key== authorname:
                print(author_book[key])
        print(booksandauthor)
        #pass
    def sortBookInTopologicalOrder():
        books.sort()
        #pass
    def getAllSubscribers():
        print(subscribers)
        #pass
    def getAllEarnings():

        pass
    def getUnavailableBooks(bookname):
        #for i in books:
            if namebook==bookname:
                print("book is available")
            else:
                print("book is unavailable")
                #pass
    def mapAuthorWithBook():
        pass
class My_Library(Library):
    def getFavouriteBook():
        pass
Library.sortBookInTopologicalOrder()
    
