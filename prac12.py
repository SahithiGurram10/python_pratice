n=int(input())#to find count of the digits inn given number

count=0;sum=0;n1=n
while(n!=0):
    rem=n%10
    count+=1
    n//=10
while(n1!=0):
    rem=n1%10
    sum+=rem**count
    n1//10
if(sum==temp):
    print("armstrong")
else:
    print("not")    
         