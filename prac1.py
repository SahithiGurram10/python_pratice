# Question - Accept a five digit number as input and print the sum of its digits as output.
# sample input - 11111
# sample output - 5
n=input("Enter a five digit number to get the sum - ") # To take input
sum=0
isinteger = True # using boolean values
try: # try and except 
    int(n)
    # if any error in try code, it will go to except code. 
    # Hence, here we are checking if the string is actually an integer or not. If it's an integer it won't go to 
    # except. BUt, if it's not an integer it will go the except code and makes the boolean false. 
except:
    print("only enter 5 digits integer.")
    isinteger = False

if len(n)==5 and isinteger:
    for g in n:
        sum = sum + int(g)
    print(sum)
else:
    print("only 5 digits allowed")