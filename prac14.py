rows=int(input("enter number of rows:"))#to print half pyramid using pattern
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")    
