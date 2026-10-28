from random import randint

class BankAccount:

    def __init__(self,name):
        self.name = name
        self.balance = 100
        self.account_num = f"{randint(1,1000):04d}"
    # set default varibles for an empty account


    #shows the main menu and function select, asnwer will call the chosen function
    def main_menu(self):
        while True:

            print('''
Please choose an option:
1. Make a deposit
2. Make a withdrawal
3. View account information
4. Quit)''')

            answer = input('Enter only the number: ').strip()
            print()

            if answer == '1':
                self.make_deposit()

            elif answer == '2':
                self.make_withdrawal()
                
            elif answer == '3':
                self.view_info()

            elif answer =='4':
                print("Thank you for your business!")
                return False
            else:
                print('Invalid choice. Please try again. Please print only the number')
                

    # **Make a deposit:** Ask how much money they would like to add to the account. 
    # Make sure deposits change the account balance correctly.
    def make_deposit(self):
        while True:
            self.amount = input('How much would you like to deposit? ')

            try:
                self.amount = float(self.amount)
                self.balance += self.amount
                print(f'sucessfully deposited ${self.amount:.2f}')
                break

            except:
                print("Invalid input. Please enter a valid number. $")

    # **Make a withdrawal:** 
    # Ask how much money they would like to withdraw. 
    # The program should not allow the customer to withdraw more money than they currently 
    # have in the account. Make sure withdrawals change the account balance correctly.
    def make_withdrawal(self):
        while True:
            self.amount = input('How much would you like to withdraw? $')

            try:
                self.amount = float(self.amount)
                self.balance -= self.amount

                if self.balance < 0:
                    self.balance += self.amount
                    print('insufficient funds')

                else:
                    print(f'sucessfully withdrew ${self.amount:.2f}')
                
                break

            except:
                print("Invalid input. Please enter a valid number.")
                print()

    # **View account information:** 
    # Display the customer’s name, account number, and current balance.
    def view_info(self):
        print(f'Name: {self.name}\nAccount #:{self.account_num}\nBalance: ${self.balance:,.2f}')
