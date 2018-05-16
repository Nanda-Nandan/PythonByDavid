class Parent(object):
    def __init__(self,value):
        self.value=value
    def parentmethod(self):
        print('parent class method')
    def run(self):
        print('parent running')
        self.parentmethod()
class Child(Parent):

    def childmethod(self):
        print('child class method')
    def run(self):
        print('child running')
        super().run()

class child1(Parent):
    def __init__(self,value,extravalue):
        self.extravalue=extravalue
        super().__init__(value)#when defining child constructor have to call internally parent class constructor to initialize
        #or else parent object wont create
    def run(self):
        print("child1 running")
        super().run()

c=Child(42)
c.run()
c1=child1(45,3)
