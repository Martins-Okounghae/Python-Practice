# python oop method
import datetime
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount


    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True




emp_1 = Employee('Monday', 'Mlastname', 100000)
emp_2 = Employee('Tuesday','Tlastname', 200000)
emp_3 = Employee('Wednesday','Wlastname',300000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'


new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)





print(new_emp_1.email)
print(new_emp_1.pay)

print(new_emp_2.email)
print(new_emp_2.pay)

print(new_emp_3.email)
print(new_emp_3.pay)

may_date = datetime.date(1975,3,26)

print(Employee.is_workday(may_date))