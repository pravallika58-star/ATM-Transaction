# ATM-Transaction
# Case Study 13: ATM Transaction Sequence Simulation

## Python Activity-Based Learning

### Student Details
- **Name:**DURGA SURYA PRAVALLIKA
- **Roll Number:** N26V01A0383
- **Branch:** CSE
- **Section:** 5
- **Programming Language:** Python

---

## 1. Problem Statement

The ATM Transaction Sequence Simulation is a Python-based program that processes a sequence of deposits and withdrawals. It maintains the account balance, checks withdrawal limits, rejects invalid transactions and generates a transaction summary.

The system displays the total deposits, total withdrawals, successful transactions, rejected transactions and final account balance.

## 2. Objectives

- To simulate basic ATM operations.
- To process multiple deposits and withdrawals.
- To maintain the current account balance.
- To enforce withdrawal limits.
- To reject invalid transactions.
- To generate a transaction history and final summary.

## 3. Assumptions

1. The initial account balance must not be negative.
2. The transaction amount must be greater than zero.
3. The maximum withdrawal limit is Rs. 10,000 per transaction.
4. Withdrawals cannot exceed the available account balance.
5. Deposits and withdrawals are entered by the user.
6. Invalid transactions are rejected without changing the account balance.
7. The program supports deposit and withdrawal operations only.

## 4. Algorithm

1. Start the program.
2. Enter the initial account balance.
3. Set the withdrawal limit to Rs. 10,000.
4. Initialize transaction counters and totals.
5. Enter the number of transactions.
6. Display the transaction menu.
7. Read the transaction choice and amount.
8. Check whether the amount is valid.
9. If the choice is deposit, add the amount to the balance.
10. If the choice is withdrawal:
    - Check the withdrawal limit.
    - Check the available balance.
    - If valid, subtract the amount.
    - Otherwise, reject the transaction.
11. Store the transaction details.
12. Repeat until all transactions are completed.
13. Display the transaction summary.
14. Display the final account balance.
15. Stop the program.

## 5. Pseudocode

```text
START

INPUT initial_balance
SET withdrawal_limit = 10000

INITIALIZE:
    total_deposits = 0
    total_withdrawals = 0
    successful = 0
    rejected = 0

INPUT number_of_transactions

FOR each transaction:

    DISPLAY transaction menu

    INPUT choice
    INPUT amount

    IF amount <= 0:
        REJECT transaction
        INCREASE rejected count

    ELSE IF choice = 1:
        balance = balance + amount
        total_deposits = total_deposits + amount
        INCREASE successful count

    ELSE IF choice = 2:

        IF amount > withdrawal_limit:
            REJECT transaction

        ELSE IF amount > balance:
            REJECT transaction

        ELSE:
            balance = balance - amount
            total_withdrawals = total_withdrawals + amount
            INCREASE successful count

    ELSE:
        REJECT transaction

DISPLAY transaction history
DISPLAY total deposits
DISPLAY total withdrawals
DISPLAY successful transactions
DISPLAY rejected transactions
DISPLAY final balance

STOP
```

## 6. Python Source Code

**File name:** `atm_transaction.py`

The complete Python implementation is available in this file.

## 7. Test Cases

| Test Case | Initial Balance | Transaction | Amount | Expected Result |
|---|---:|---|---:|---|
| 1 | 5000 | Deposit | 2000 | Successful |
| 2 | 5000 | Withdrawal | 3000 | Successful |
| 3 | 5000 | Withdrawal | 12000 | Rejected: Limit exceeded |
| 4 | 2000 | Withdrawal | 3000 | Rejected: Insufficient balance |
| 5 | 5000 | Deposit | -500 | Rejected: Invalid amount |
| 6 | 5000 | Invalid choice | 1000 | Rejected: Invalid choice |

## 8. Expected Output

```text
ATM TRANSACTION SYSTEM

Initial Balance: Rs. 5000

Transaction 1:
Deposit successful!
Current Balance: Rs. 7000

Transaction 2:
Withdrawal successful!
Current Balance: Rs. 4000

Transaction 3:
Rejected: Withdrawal limit exceeded
Current Balance: Rs. 4000

Transaction 4:
Rejected: Insufficient balance
Current Balance: Rs. 4000

TRANSACTION SUMMARY

Initial Balance: Rs. 5000
Total Deposits: Rs. 2000
Total Withdrawals: Rs. 3000
Successful Transactions: 2
Rejected Transactions: 2

Final Account Balance: Rs. 4000

THANK YOU!
```

## 9. Conclusion

The ATM Transaction Sequence Simulation successfully performs basic banking operations using Python. It maintains the account balance, processes deposits and withdrawals, validates transactions and enforces withdrawal limits.

This project helps us understand Python variables, data types, operators, conditional statements, loops, lists and tuples. It also demonstrates how Python can be used to solve real-world problems.

---

**Project:** Python Activity-Based Learning  
**Case Study Number:** 13  
**Topic:** ATM Transaction Sequence Simulation
