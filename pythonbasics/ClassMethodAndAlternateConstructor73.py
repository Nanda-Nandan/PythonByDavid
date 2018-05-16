
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
    #here cls is Port Object(empty)
    @classmethod
    def overloadedconstructor(cls,more,name,city,business,salary):
        cls.more=more
        return cls(name,city,business,salary)

h=Port.overloadedconstructor('more','nanda','pune',56,567)
