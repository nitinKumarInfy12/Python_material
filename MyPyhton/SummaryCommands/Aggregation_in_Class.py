class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self, ):
        return (self.pay*12) + self.bonus


class Employee:
    def __init__(self, name, age, Salary):
        self.name = name
        self.age = age
        # self.obj_salary = Salary # lets remove the instance from here and put in the partametrs section
        self.obj_salary = Salary

    def total_salary(self):
        return self.obj_salary.annual_salary()


salary = Salary(15000,2000) # instance of the Salary class
emp = Employee('Max', 20, salary)
print(emp.total_salary())

"""
emp = Employee('Max', 20, 15000, 20000) # constructor of the 
print(emp.total_salary())
"""

# aggregation represents Has-A relation
# unidirectional association
# objects are independent of each other
