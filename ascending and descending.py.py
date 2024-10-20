a=[10,20,90,0,8,7,45,345,879,1,23,43,99999,100000]
a.reverse()             #reverse of the list without sorting    
print("My list=",a)
a.sort()                #ascending 
print("My list=",a)
a.sort(reverse=True)    #descending
print("My list=",a)
a.reverse()             #reverse of descending bcz of the above function
print("My list=",a)     