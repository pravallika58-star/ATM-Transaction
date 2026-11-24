
# Case Study 13: ATM Transaction Sequence Simulation

print("====================================")
print("       ATM TRANSACTION SYSTEM")
print("====================================")

# Initial account balance
balance = float(input("Enter initial balance: "))

# Withdrawal limit
withdrawal_limit = 10000

# Transaction details
transactions = []

total_deposits = 0
total_withdrawals = 0
successful = 0
rejected = 0

# Number of transactions
n = int(input("Enter number of transactions: "))

if balance < 0 or n < 0:
    print("Invalid input!")
else:

    # Process transactions
    for i in range(n):

        print("\nTransaction", i + 1)
        print("1. Deposit")
        print("2. Withdrawal")

        choice = input("Enter your choice: ")
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Rejected: Invalid amount")
            rejected += 1
            transactions.append(("Invalid", amount, "Rejected"))

        elif choice == "1":
            balance += amount
            total_deposits += amount
            successful += 1

            print("Deposit successful!")
            transactions.append(("Deposit", amount, "Successful"))

        elif choice == "2":

            if amount > withdrawal_limit:
                print("Rejected: Withdrawal limit exceeded")
                rejected += 1
                transactions.append(("Withdrawal", amount, "Rejected"))

            elif amount > balance:
                print("Rejected: Insufficient balance")
                rejected += 1
                transactions.append(("Withdrawal", amount, "Rejected"))

            else:
                balance -= amount
                total_withdrawals += amount
                successful += 1

                print("Withdrawal successful!")
                transactions.append(("Withdrawal", amount, "Successful"))

        else:
            print("Rejected: Invalid transaction choice")
            rejected += 1
            transactions.append(("Invalid", amount, "Rejected"))

        print("Current Balance: Rs.", round(balance, 2))

    # Final transaction summary
    print("\n====================================")
    print("       TRANSACTION SUMMARY")
    print("====================================")

    print("Initial Balance: Rs.", round(
        balance + total_withdrawals - total_deposits, 2))

    print("Total Deposits: Rs.", round(total_deposits, 2))
    print("Total Withdrawals: Rs.", round(total_withdrawals, 2))
    print("Successful Transactions:", successful)
    print("Rejected Transactions:", rejected)

    print("\nTransaction History")

    for transaction in transactions:
        print(transaction[0], "| Rs.",
              transaction[1], "|", transaction[2])

    print("\nFinal Account Balance: Rs.", round(balance, 2))

    print("====================================")
    print("       THANK YOU!")
    print("====================================")
