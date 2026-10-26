from functions import *

def main():
    #intro text + user name
    print("Welcome to the Bank of Tucker!")
    name = input("Please enter your name: ")

    #initialize bank account instance
    account = BankAccount(name)



if __name__ == "__main__":
    main()