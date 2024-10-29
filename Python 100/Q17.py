# Write a program that computes the net amount of a
# bank account based a transaction log from console input.

bank_balance = 0

transaction_log = []

while True:
    transaction = input('D/W Amount: ')
    if len(transaction.split(' ')) == 2:
        transaction_log.append(transaction)
    else:
        break

for transaction in transaction_log:
    split = transaction.split(' ')
    if split[0].upper() == 'D':
        bank_balance += int(split[1])
    elif split[0].upper() == 'W':
        bank_balance -= int(split[1])

print(bank_balance)