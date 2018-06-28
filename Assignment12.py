class AgeError(Exception):
    pass

try:
    count=0
    while(count<18):
        a = int(input("enter age"))
        if(a<18):
         raise AgeError
except ValueError:
    print("please enter Int")
except AgeError:
    print("age is nt right")
