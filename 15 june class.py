'''t=[1,2,3,4]
print(len(t))

l=[1,2,3]
print (tuple(l))
print(list(t))

t=(1,2,3)
del t
print(t)'''

#set
a=set([1,2,3])
b=set ([3,4,5])
print(a&b) #intersection
print(a|b) #union

a.add("apple")
print(a)
a.update(["a","b","c"])
print(a)
a.pop()
print(a)

c=set([1,2,3])
c.remove(2)
c.discard(2)
print(c)


a=set([1,2,3,4,5])
b=set([3,4,5])
print(a<=b)
print(b<=a)
print(a>=b)

#dictionary
d={'name': 'megha',
    'age':  20}
print(d)
d['name']='roi'
print(d)

#functions of dictionary
del d['name']
print(d)
d.clear()
print(d)
del d
print(d)
