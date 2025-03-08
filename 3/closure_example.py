
balance = 8000

def bank_account(starting_value: int):
    def deposit(amount: int):
        nonlocal starting_value
        
        starting_value += amount
        print(starting_value)

    def withdraw(amount: int):
        nonlocal starting_value
        
        if amount > starting_value:
            raise ValueError("Amount can not be greater than balance")
        starting_value -= amount
        print(starting_value)

    return deposit, withdraw


# my_sum = sum

# print(my_sum)
# print(sum)

# bank_account.starting_value = 3000

my_deposit, my_withdraw = bank_account(5000)
# my_deposit_two = bank_account(300)

# my_deposit_two(600)
my_deposit(500)
my_withdraw(100)

# print(sum([1, 2, 3]))
# print(my_sum([1, 2, 3]))


# deposit(7000)
# withdraw(500)
# balance -= 20000
# print(balance)
# withdraw(20000)


# print(balance)
