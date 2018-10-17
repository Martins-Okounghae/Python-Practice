# Python object oriented programming

class Employee:

    raise_amount = 1.04
    num_of_emp = 0


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@firststack.net'
        Employee.num_of_emp = Employee.num_of_emp + 1


    def prfullname(self):
        return '{} {}'.format(self.first, self.last)

    def emaill(self):
        return '{}'.format(self.email)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return '{}'.format(self.pay)


print(Employee.num_of_emp)

emp_1 = Employee('Monday','Days',200000)

emp_2 = Employee('Song','Melody',120000)

#print(emp_1.prfullname())
#print(emp_2.emaill())

#print(emp_1.pay)
#print(emp_1.apply_raise())
#print(emp_1.apply_raise())

#emp_1.raise_amount = 1.05

print(Employee.num_of_emp)


