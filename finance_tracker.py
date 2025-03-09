def add_transaction():
    amount = float(input("Enter transaction amount: "))
    category = input("Enter category: ")
    trans_type = input("Is this income or expense? ").strip().lower()

    return {
        "amount": amount, 
        "category": category, 
        "type": trans_type
        }


def calculate_balance(transactions, starting_balance):
    balance = starting_balance
    for t in transactions:
        balance += t["amount"]
    return balance


transactions = []

print("Welcome to your Personal Finance Tracker!")
starting_balance = float(input(f"Enter your starting balance: "))

while True:
    transactions.append(add_transaction())
    cont = input(f"Do you want to add another transaction?(y/n): ").lower().strip()
    if cont == "n":
        break

final_balance = calculate_balance(transactions, starting_balance)
print(f"Initial balance: ${starting_balance:.2f} \nFinal balance: ${final_balance:.2f}")