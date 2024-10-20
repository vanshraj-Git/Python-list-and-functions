# Write a Python program that:

# Takes marks of N students as input from the user (store them in a list).
# Displays the sum of all marks.
# Finds and prints the highest and lowest marks.
# Appends 5 bonus marks to the last student’s score.
# Inserts a new student's mark at the second position.
# Removes a specific student’s mark (input from the user).
# Reverses the list of marks.
# Sorts the marks in ascending and descending order.
# Counts the number of times a given mark (input from user) appears in the list.
# Checks if a specific mark (input from user) exists in the list.
# Finds the second highest mark


# marks=list(map(int,input("enter elements= ").split()))  marks of n no. students input line 
# marks=[marks for marks in range(70,90)]


marks=[84, 60, 8, 49, 93, 47, 4, 88, 76 ,26, 35, 13, 64, 54, 58, 76,50, 29, 31, 87, 43,76]
print("1.)My list=",marks)
marks[-1]+=5
sum=sum(marks)
maximum=max(marks)
min=min(marks)
marks.insert(1,90)
print("2.)sum of the list=",sum)
print("3.)largest no. in the list=",maximum,"\n4.)smallest no. in the list=",min)
marks.remove(4)
marks.reverse()
print("5.)Reverse list=",marks)
marks.sort()
print("6.)Ascending order=",marks)
marks.sort(reverse=True)
print("7.)Descending order=",marks)
count=marks.count(76)
print("8.)no. of times 76 appeared",count)
if 77 in marks:
    print("9.)77 is someone marks")
else:
    print("9.)none of the student scored 77 marks")
marks.remove(max(marks))
max2=max(marks)
print("10.)second highest no. in the list=",max2)
print("11.)My list=",marks)
