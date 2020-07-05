# inheritance is useful as we can create subclass and get all the functionality as our parent class
# we can override or add new functionality without affecting the parent class
from Employees import Employees

class Developer (Employees):
    raise_amt = 1.10

# prog language was added as a new argument which will be added to Developer class but not Employee class
    def __init__(self, first, last, salary, prog_lang):
        # we do not want to retype self.first,etc so we add super!
        super().__init__(first, last, salary)
        # new method for this class
        self.prog_lang = prog_lang


# instances from Employee class
dev_1 = Developer("Anna", "Smith", "35000", "Python")
dev_2 = Developer("James", "Barry", "45000", "Java")

# added a new developer
dev_3 = Developer("John", "Brown", "65000", "Python ")
print(dev_1.email)
print(dev_1.prog_lang)
print(dev_3.email)


# print()

