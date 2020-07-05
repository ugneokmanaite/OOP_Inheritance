# inheritance is useful as we can create subclass and get all the functionality as our parent class
# we can override or add new functionality without affecting the parent class
from employees import Employees

class Developer (Employees):
    raise_amt = 1.10

    def __init__(self, first, last, salary, prog_lang):
        # we do not want to retype self.first,etc so we add super!
        super().__init__(first, last, salary)
        # new method for this class
        self.prog_lang = prog_lang


# this was instance from Employee class
dev_1 = Developer('Corey', 'Schafer', 50000, "Python")
dev_2 = Developer('Test', 'Employee', 60000, "Java")
print(dev_1.email)
print(dev_1.prog_lang)

# to use Employee class if we want to check the bonus payment
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


# however what if we want to change the bonus (raise) amount we need to make some changes!
# at the top of Developer class we change this amount!


# print(help(Developer))

# first it looked in our developer class for the init method
# when it wasn't found it went to employee class and executed it
# if it didnt find it in Employee class it would of looked at builtins.object
#

# print(dev_1.raise_amt)
# dev_1.apply_raise()
# print(dev_1.raise_amt)

