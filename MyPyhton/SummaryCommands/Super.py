# super function allows to use super class in the child class

class Parent:
    def __init__(self, name):
        print('Parent__init__',name)

class Parent2:
    def __init__(self, name):
        print('Parent2__init__',name)


class Child(Parent, Parent2):
    def __init__(self):
        print('Child__init__')
        super().__init__('Max')

        # in case of multiple inheritance, Super function will not work fine.
        # so need to manually call the parnt functions
        Parent.__init__(self,'Tom')
        Parent2.__init__(self, 'Julie')

child = Child()

# method resolution order
print(Child.__mro__)