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
balance = 1000000
current_balance=1000000
a=True
b=True
print("HELLO THERE...")
while b==True:
    user_response=input("WOULD YOU LIKE TO: CHECK THE BALANCE OF YOUR ACCOUNT, WITHDRAW MONEY, OR DEPOSIT MONEY?")
    if user_response=="check the balance":
        while a==True:
            print(current_balance)
            x=input("WOULD YOU LIKE TO DO SOMETHING ELSE? Y/N")
            if x=="Y":
                a==False
                break
            elif x=="N":
                a==False
                break
        b==False
        print("BYE!")
        break
    elif user_response=="withdraw money":
        while a==True:
            response=input("HOW MUCH WOULD YOU LIKE TO WITHDRAW?")
            withdraw_number=int(response)
            current_balance=balance-withdraw_number
            if withdraw_number<0:
                    print("ERROR")
            print(f"YOUR CURRENT BALANCE IS: {current_balance}")
            x=input("WOULD YOU LIKE TO DO SOMETHING ELSE? Y/N")
            if x=="Y":
                a==False
                break
            elif x=="N":
                a==False
                break
        b==False
        print("BYE!")
        break
    elif user_response=="deposit money":
        while a==True:
            deposit_response=input("HOW MUCH WOULD YOU LIKE TO DEPOSIT?")
            deposit_number=int(deposit_response)
            current_balance=balance+deposit_number
            if deposit_number<0:
                print("ERROR")
                break
            print(f"YOUR CURRENT BALANCE IS: {current_balance}")
            x=input("WOULD YOU LIKE TO DO SOMETHING ELSE? Y/N")
            if x=="Y":
                a==False
                break
            elif x=="N":
                a==False
                break
        b==False
        print("BYE!")
        break
                


    

