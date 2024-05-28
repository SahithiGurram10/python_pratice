n=input("enter students roll no:")
isbranch=True
try:
    int(n)
except: 
    print("student belongs to data science or not:") 
    isbranch=False  