# Write a Python program to manage a library's collection of books. Your program should:

# Take the names of N books as input from the user (store them in a list).
# Display the total number of books in the library.
# Search for a specific book (input from the user) to see if it exists.
# Add a new book to the collection.
# Insert a new book at a specific position (input from the user).
# Remove a specific book from the collection (input from the user).
# Sort the books alphabetically in ascending and descending order.
# Reverse the order of the books.
# Count how many times a specific book title (input from the user) appears in the collection.
# Display the second book in the alphabetical order after sorting the list.

n=int(input("Enter the no. of books = "))
books=[]
for i in range(0,n):
    book=input(f"Enter the name of book {i+1}=")
    books.append(book)
print("1.)original order",books)
books.reverse()
print("2.)reverse order",books)
print("3.)total no. of books=",n)
search=input("search any book=")
if search in books:
    print("4.)available")
else:
    print("4.)Sorry,not available")
books.append("death on the nile")
print("5.)list after append function=",books)
insert1=int(input("enter the postition of the book you want to insert="))
insert2=input("enter the name of the book you want to insert=")
books.insert(insert1,insert2)
print("6.)list after insert function=",books)
remove1=input("enter the name of the book you want to remove=")
books.remove(remove1)
print("7.)list after remove function=",books)
books.sort()
print("8.)Ascending=",books)
books.sort(reverse=True)
print("9.)Descending=",books)
count=input("Enter a specific element to find out how many times it has occured=")
g=0
if count in books:
    g+=1
    print("10.)No. of times it has occured=",g)
else:
    print("Entered element not present")
print(books.sort())
print("11.)",books[1])





