class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self ):
        return (self.pay*12) + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        # create a variable by intantiating the salary class inside the employee calss
        # employee class becomes container class, salary class becomes contain
        self.obj_salary = Salary(pay, bonus)

    def total_salary(self):
        return self.obj_salary.annual_salary()


emp = Employee('Max', 20, 15000, 20000)

print(emp.total_salary())

# composition: When one class deligates some responsibility to another class
# composition represents Part-of relationship
# salry object dies when emp object is deleted
# objects are interdependent on each other
