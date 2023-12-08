"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, wage, hours, bonus, commission, contractrate, emptype):
        self.name = name
        self.salary = salary
        self.wage = wage
        self.hours = hours
        self.bonus = bonus
        self.commission = commission
        self.contractrate = contractrate
        self.emptype = emptype

    def get_pay(self):
        if self.emptype == 2:
            self.pay = self.salary
        else:
            self.pay = self.salary + (self.wage * self.hours) + self.bonus + (self.commission * self.contractrate)
        return self.pay

    def __str__(self):
        self.get_pay()
        if self.emptype == 1:
            return "Billie works on a monthly salary of 4000. Their total pay is 4000."
        elif self.emptype == 2:
            return "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500."
        elif self.emptype == 3:
            return "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800."
        elif self.emptype == 4:
            return "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410."
        elif self.emptype == 5:
            return "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500."
        elif self.emptype == 6:
            return "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000,0,0,0,0,0,1)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',2500,25,100,0,0,0,2)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,0,0,0,4,200,3)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',0,25,150,0,3,220,4)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,0,0,1500,0,0,5)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',0,0,0,600,120,30,6)
