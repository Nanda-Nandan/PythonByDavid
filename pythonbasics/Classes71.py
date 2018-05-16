#in prev examples we have read a csv file and return a dictionary for calculation
#in stead of storing data to dictionary we can make a object and store values to object
class Port(object):
    #constructor
    #self is like newly created empty object
    def __init__(self,name,city,business,salary):
        self.name=name
        self.city=city
        self.business=business
        self.salary=salary
    def cost(self):
        total=self.business+self.salary
        print(total)

    def testargument(self,x):
        self.x=x

