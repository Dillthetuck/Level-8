

class BankAccount:

    def __init__(self,name):
        self.name = name
        self.balance = 0
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

            answer = input().strip()

            if answer == '1':
                #self.make_deposit(self)
                pass
            elif answer == '2':
                #self.make_withdrawal(self)
                pass
            elif answer == '3':
                #self.view_info(self)
                pass
            elif answer =='4':
                #self.exit(self)
                pass
            else:
                print('Invalid choice. Please try again. Please print only the number')
                

    # **Make a deposit:** Ask how much money they would like to add to the account. 
    # Make sure deposits change the account balance correctly.
    def make_deposit(self):
        pass

    # **Make a withdrawal:** 
    # Ask how much money they would like to withdraw. 
    # The program should not allow the customer to withdraw more money than they currently 
    # have in the account. Make sure withdrawals change the account balance correctly.
    def make_withdrawl(self):
        pass

    # **View account information:** 
    # Display the customer’s name, account number, and current balance.
    def view_info(self):
        pass
