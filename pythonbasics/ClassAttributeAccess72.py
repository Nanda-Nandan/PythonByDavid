import Classes71
#three things we can do using object in python
h=Classes71.Port('nanda','pune',56,567)
h.testargument(5)
#get attribute
print(h.x)
#set attribute
h.name="nanda1"
#delete attribute
del h.x
h.cost()#we can call by this or we can treat method as attribute
c=h.cost #get the attribute cost which is actually a method
c()
#predefined methods to get and det attribute
getattr(h,'name')
setattr(h,'y',65)