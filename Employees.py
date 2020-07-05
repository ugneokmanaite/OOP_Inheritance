# class is created
class Employees:

# class variable whose value is shared among all instances of this class
# this can be accessed as Employee.empCount from inside or outside the class

    employee_count = 0
# initialization method required when creating new class
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        # an email
        self.email = first_name + "." + last_name + "@company.com"

# %d is placeholder for numeric or decimal values
    def display_count(self):
        print ("Total Employee %d" % Employees.employee_count)

    def display_name(self):
        print("Employee's full name is {} {}".format(self.first_name, self.last_name))

    def display_salary(self):
        print ("{} {} annual salary is {}".format(self.first_name, self.last_name, self.salary))

# instances for employees added

employee_1 = Employees ("Anna", "Smith", "35000")
employee_2 = Employees ("James", "Barry", "45000")

print(employee_1.email)
print(employee_2.email)
print(employee_1.display_name(), employee_1.display_salary())
