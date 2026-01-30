
class BookStore:
    NoOfBooks=0

    def __init__(self,Name,Author):

        self.Name=Name
        self.Author=Author

        BookStore.NoOfBooks=BookStore.NoOfBooks+1

    def Display(self):
        print(self.Name ,"by", self.Author  )
        print("No of books:",BookStore.NoOfBooks)

b1 = BookStore("Linux System Programming", "Robert Love")
b1.Display()

b2 = BookStore("C Programming", "Dennis Ritchie")
b2.Display()