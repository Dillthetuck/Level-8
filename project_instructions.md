# IS 303 – Level #8 Assignment: Bank Account
**Instructor:** Hilton

## Project Specifications

Create a Python banking program for a customer who wants to manage a simple bank account. 

### Core Requirements
*   **Account Initialization:** Ask the customer for their name and then create an account for them. You may assign a random account number. The account should begin with a balance of **$0.00**.
*   **Object-Oriented Design:** Your program must use a `BankAccount` class to represent the customer’s account.
*   **File Structure:** Organize your program into **at least two Python files** so that the class and the main program are separate.

### Menu Options
The customer should be able to choose from the following menu:
1.  **Make a deposit:** Ask how much money they would like to add to the account. Make sure deposits change the account balance correctly.
2.  **Make a withdrawal:** Ask how much money they would like to withdraw. The program should **not** allow the customer to withdraw more money than they currently have in the account. Make sure withdrawals change the account balance correctly.
3.  **View account information:** Display the customer’s name, account number, and current balance.
4.  **Quit:** Exit the program.

### Program Logic & Formatting Notes
*   **Functions:** Use one function for each of the first three menu options.
*   **Input Validation:** If the customer enters an invalid menu choice, display an appropriate message and allow them to try again. Continue displaying the menu until the customer chooses to quit.
*   **Formatting:** Format monetary amounts as dollar values with two decimal places (e.g., `$0.00`).
*   **Naming Conventions:** Use meaningful variable and method names.
*   **Testing:** Test your program with several deposits, withdrawals, invalid choices, and attempted withdrawals that exceed the account balance.
*   **Submission:** Submit your PUBLIC GitHub link via Canvas.

---

## Sample Output

*Note: Your output does not need to match the sample session exactly, but it should provide equivalent information.*

```text
Welcome to the Bank of Spencer!
Please enter your name:
Spencer Hilton

Please choose an option:
1. Make a deposit
2. Make a withdrawal
3. View account information
4. Quit
Hello

Invalid choice. Please try again.
5

Invalid choice. Please try again.
1

How much would you like to deposit?
100

Please choose an option:
1. Make a deposit
2. Make a withdrawal
3. View account information
4. Quit
2

How much would you like to withdraw?
35

Please choose an option:
1. Make a deposit
2. Make a withdrawal
3. View account information
4. Quit
3

Name: Spencer Hilton
Account #: 12345
Balance: $65.00

Please choose an option:
1. Make a deposit
2. Make a withdrawal
3. View account information
4. Quit
4

Thank you for your business!
```