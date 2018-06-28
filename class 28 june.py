#exception handling
'''
try:
    import megha
    a=3
    b=3/a
except ZeroDivisionError:
    print("no is divisible by 0")
else:
    print(b)
#finally:
  #  print("i will execute")
  '''
try:
    import megha
    a=[1,2,3]
    print(a[3])
except IndexError:
    print("Index does not exist")
except ImportError:
    print("file is not import ")

class AgeError(Exception):
    pass
try:
    a=int(input("enter age"))
    if(a<18):
        raise AgeError
except ValueError:
    print("please enter Int")
except AgeError:
    print("age is nt right")
else:
    print("please enter Int")

#assginment question3
try:
    raise NameError("hi there")
except NameError:
    print("An exception")
