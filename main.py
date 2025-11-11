"""
Options:
- check the balance: prints current balance
- withdraw money:
    ask you how much to withdraw
    reduce the balance by that amount
    if you try to withdraw more than you have...
        print error don't update the balance
    don't withdraw a negative amount
- deposit money:
    ask you how to deposit
    increase the balance by that amount
    don't deposit a negative amount
- loop (with a while loop) until the user says "exit"
"""

# start with 1 million dollars
current_balance=1000000

print("HELLO THERE...")
while True:
    user_response=input("WOULD YOU LIKE TO: CHECK THE BALANCE OF YOUR ACCOUNT, WITHDRAW MONEY, OR DEPOSIT MONEY? please write in lower case letters: check the balance, withdraw money, or deposit money")
    if user_response=="check the balance":
        print(current_balance)
        x=input("WOULD YOU LIKE TO DO SOMETHING ELSE? Y/N")
        if x=="N":
            print("BYE!")
            if current_balance<0:
                print("HAVE FUN WITH YOUR DEBT!")
            break
    elif user_response=="withdraw money":
        response=input("HOW MUCH WOULD YOU LIKE TO WITHDRAW?")
        withdraw_number=int(response)
        if withdraw_number<0:
            print("ERROR")
        current_balance=current_balance-withdraw_number
        print(f"YOUR CURRENT BALANCE IS: {current_balance}")
        if current_balance<0:
            print("YOU ARE IN DEBT!!! YIKES")
        x=input("WOULD YOU LIKE TO DO SOMETHING ELSE? Y/N")
        if x=="N":
            print("BYE!")
            if current_balance<0:
                print("HAVE FUN WITH YOUR DEBT!")
            break
    elif user_response=="deposit money":
        deposit_response=input("HOW MUCH WOULD YOU LIKE TO DEPOSIT?")
        deposit_number=int(deposit_response)
        current_balance=current_balance+deposit_number
        if deposit_number<0:
            print("ERROR")
            break
        print(f"YOUR CURRENT BALANCE IS: {current_balance}")
        x=input("WOULD YOU LIKE TO DO SOMETHING ELSE? Y/N")
        if x=="N":
            print("BYE!")
            if current_balance<0:
                print("HAVE FUN WITH YOUR DEBT!")
            break
                


    

