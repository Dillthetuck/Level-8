from functions import *

def main():
    #intro text + user name
    print("Welcome to the Bank of Tucker!")
    name = input("Please enter your name: ")

    #initialize bank account instance
    account = BankAccount(name)

    #shows the main menu and function select, asnwer will call the chosen function
    go = True
    while go == True:
        go = account.main_menu()
            


if __name__ == "__main__":
    main()