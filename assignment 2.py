def coke_machine():
    amount_due = 50
    coins = [25,10,5]
    while amount_due > 0:
        print("Amount due is:",amount_due)
        coin = int(input("Insert coin (25,10,5): "))
        if coin in coins:
            amount_due -= coin
    change = -amount_due
    print("change owed:",change)

coke_machine()