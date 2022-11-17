
print("WELCOME TO RABIAMUHAMMAD BANK")
Trials = 3
userpin = 1234

while Trials != 0:
    pin = int(input("please Enter your 4 digit pin number: "))
    if pin != userpin:
        Trials -= 1
        print("wrong pin number, you have", Trials, "Trials left")
    else:
        userchoice = input("d: Deposit or w: Withdraw: ")
        if userchoice == "d":
            userDeposit = input("enter the Amount you would like to Deposit: ")
            print(userDeposit, "$ have been Deposited into your Account")
        if userchoice == "w":
            userWithdraw = input("enter the Amount you would like to Withdraw: ")
            print(userWithdraw, "$ have been withdraw from your account")
            userExit = input("would you like to continue? Y/N ")
        if userExit == "N":
            print("""*******thank you for banking with us
                      visit us next time*************""")
            break
        else:
             continue