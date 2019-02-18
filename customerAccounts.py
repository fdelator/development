# python3
# fdelator@github.com

# script performs object-oriented programming to create customer banking accounts, as shown:
# 1a) Customer class is defined; accepts strings for 'name', 'lastname', and 'ssn'
# 1b) __str__ is overloaded for desired return behavior
# 2a) BankAccount class is defined; accepts a Customer class object, accountNumber and balance as ints
# 2b) BankAccount class has two functions: deposit and withdraw
# 2c) __str__ is also overloaded for desired return behavior
# 3a) CheckingAccount and SavingAccount are defined as subclasses of BankAccount
# 3b) Both subclasses inherit the attributes from BankAccount
# 3c) Each subclass has a version of the function applyAnnualInterest


# random number generator needed for base class BankAccount
import random

# define class Customer
class Customer:
    # initialize the attribute names for Customer() class
    # class Customer() takes attribute arguments 'name', 'lastname', and 'ssn' as strings
    # when Customer() is assigned, it becomes an object of class Customer()
    # for a Customer() object, the arguments inside must be assigned to instance variables
    def __init__(self, name, lastname, ssn):
        # store the arguments of Customer() class as instance variables
        self.name = name
        self.lastname = lastname
        self.ssn = ssn
    
    # overload the string operator with desired behavior
    # when Customer() objects are printed, they are strung in the following way:
    def __str__(self):
        return '{} {} (ssn: {})'.format(self.name, self.lastname, self.ssn)

# define class BankAccount
# BankAccount is the base class for subclasses CheckingAccount and SavingAccount
class BankAccount:
    # initialize attribute names
    # argument 'customer' is an object of class Customer()
    # accountNumber and balance are assigned default values, if no values are given
    def __init__(self, customer, accountNumber = int(), balance = int(0)):
        # store arguments are instance variables
        self.customer = customer
        self.accountNumber = accountNumber
        self.balance = balance
        
        # if no accountNumber entered
        if not self.accountNumber:
            # generate a random 10-digit integer between range
            # smallest 10-digit integer is 1000000000
            # largest 10-digit interger is 9999999999
            self.accountNumber = random.randint(1000000000,9999999999)
        #print(self.accountNumber)
    
    # define new function deposit() of class BankAccount
    # newDeposit should be an integer
    # default newDeposit set to 0
    def deposit(self, newDeposit = int(0)):
        # update self.balance by adding newDeposit
        self.balance = self.balance + newDeposit
        #print(self.balance)
    
    # define new function withdraw
    # default newWithdraw set to 0
    def withdraw(self, newWithdraw = int(0)):
        # if the newWithdraw is larger than the self.balance...
        if newWithdraw > self.balance:
            # only attributes from the BankAccount() class can be used in print()
            # recall that __str__ is overloaded in Customer() class
            # when self.customer is printed, the __str__ overload is used
            print("{}, insufficient funds to withdraw ${}".format(self.customer, newWithdraw))
        # if newWithdraw is less than or equal to balance
        else:
            # update the balance
            self.balance = self.balance - newWithdraw
            #print(self.balance)
    # overload __str__ for class BankAccount
    def __str__(self):
        # when print(BankAccount) is used, follow this scheme
        # only use attributes of the BankAccount class
        return '{}, account number {}, balance ${}'.format(self.customer, self.accountNumber, self.balance)

# define first subclass, CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, customer, accountNumber = int(), balance = int(0)):
        # inherit the instance variables from the base class
        # also known as 'superclass', hence super()
        super().__init__(customer, accountNumber, balance)
    
    # define new function applyAnnualInterest() for CheckingAccount subclass
    # for CheckingAccount, applyAnnualInterest applies 2% on balances over 10k
    # if self.balance is less than 10k, then pass
    def applyAnnualInterest(self):
        if self.balance >= 10000:
            self.balance = self.balance + (self.balance - 10000)*(0.02)
            #print(self.balance)
        else:
            # if self.balance is less than 10k
            # pass any update to self.balance
            pass

# define second subclass, SavingAccount
class SavingAccount(BankAccount):
    def __init__(self, customer, accountNumber = int(), balance = 0):
        # again, inherit all instance variables from superclass
        super().__init__(customer, accountNumber, balance)
    
    # define applyAnnualInterest for SavingAccount subclass
    # for SavingAccount, applyAnnualInterest applies 5% on entire balance
    def applyAnnualInterest(self):
        # update self.balance with 5% multiple of self.balance, and adding 
        self.balance = self.balance + (self.balance*0.05)
        #print(self.balance)

def main():
    # 'alin' and 'mary' are instances of class Customer
    # 'instance of class' also called an 'object'
    alin = Customer('Alin', 'Smith', '111-11-1111')
    mary = Customer('Mary', 'Lee', '222-22-2222')
    
    # alinAccnt is class CheckingAccount, that inherits from baseclass BankAccount
    # maryAccnt is class SavingAccount, that inherits from baseclass BankAccount
    # base and subclasses can accept additional arguments, accountNumber and balance
    # to achieve desired accountNumber output from prompt, specify accountNumber
    #alinAccnt = CheckingAccount(alin, accountNumber = 1702660396)
    #maryAccnt = SavingAccount(mary, accountNumber = 2552619508)
    # otherwise, a random accountNumber is generated
    alinAccnt = CheckingAccount(alin)
    maryAccnt = SavingAccount(mary)
    
    # alinAccnt has deposit, withdraw, and applyAnnualInterest functions available
    # alinAccnt is object of CheckingAccount class
    alinAccnt.deposit(20000)
    print(alinAccnt)
    alinAccnt.withdraw(5000)
    print(alinAccnt)
    alinAccnt.applyAnnualInterest()
    print(alinAccnt)
    
    # same goes for maryAccnt
    maryAccnt.deposit(10000)
    print(maryAccnt)
    maryAccnt.withdraw(15000)
    print(maryAccnt)
    maryAccnt.applyAnnualInterest()
    print(maryAccnt)
    
if __name__ == '__main__': main()