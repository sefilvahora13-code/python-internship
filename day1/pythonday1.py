##what is programming?
    progrmming is a set of instruction that can solve a complex problem.In easy way we can say that how human and computer can talk to each other
##real life example:
    1. ATM Machine
        When you withdraw money:
        - Enter your PIN.
        - Check your account balance.
        - Enter withdrawal amount.
        - ATM checks whether you have enough money.
        - Machine gives you cash.
          
          EXAMPLE OF PYTHON PROGRAMMING:
            balance = 5000
            
            pin = int(input("Enter your PIN: "))
            
            if pin == 1234:
                amount = int(input("Enter withdrawal amount: "))
            
                if amount <= balance:
                    balance = balance - amount
                    print("Please collect your cash")
                    print("Remaining balance:", balance)
                else:
                    print("Insufficient balance")
            else:
                print("Wrong PIN")
