#Accept the sequence of five single digit number separated by commas as input.
#print the product of all five numbers.
# sample input - 1,2,3,4,5
# sample output - 120
values=input("enter a five single digit:")
numlist=values.split(",")
product=1
if len(numlist)==5: 
    try:
        for num in numlist:
            product*=int(num)
            print(product) 
    except:
        print("only integers allowed.")   
else:
    print("only 5 is allowed:")    
    