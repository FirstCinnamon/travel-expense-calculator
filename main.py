# Initial setup
menu = None
name = ''
price = None
purchase_history = {}
purchase_avg = {}
payers = []
payees = []
transactions = {}

while True:
    # Main menu
    print('\n' + '=' * 15, 'Travel Expense Calculator', '=' * 15)
    print('1. Add (Direct Input)')
    print('2. Add (File Input)')
    print('3. Edit')
    print('4. Delete')
    print('5. Check Transactions')
    print('6. Calculate')
    print('7. Force Exit')
    print('=' * 47 + '\n')

    menu = input('Choose a menu: ')

    if menu == '1':  # Add transaction directly
        print('\n' + '=' * 10 + '1. Add (Direct Input)' + '=' * 10)
        print('Adding a transaction.')

        name = input('Enter the name of the person who paid: ')
        while True:
            price = input('Enter the amount paid (in won): ')
            if price.isdigit():
                price = int(price)
                break
            else:
                print('※ Error ※ Please enter a number.')

        purchase_history[name] = purchase_history.get(name, 0) + price

        print('\n' + name, ':', price, 'won added.')
        print('Current transactions: ', purchase_history)

    elif menu == '2':  # Add transaction from file
        print('Adding transactions from a file.')
        # Instructions for file format
        print('Create a file named list.txt in c:\ with the following format:')
        print('Name (enter)')
        print('Amount (enter)')

        while input('Press enter when ready...'):
            pass

        try:
            with open("C:/list.txt", 'rt', encoding='utf-8') as f:
                lines = f.readlines()
                while lines:
                    name = lines.pop(0).strip().replace(" ", "")
                    price = lines.pop(0).strip().replace(" ", "")
                    if price.isdigit():
                        purchase_history[name] = int(price)
                    else:
                        print('※ Error ※ The file format is incorrect. Transaction not saved.')
                        break
        except FileNotFoundError:
            print('The file does not exist in the specified path.')

        print('Current transactions: ', purchase_history)

    elif menu == '3':  # Edit transaction
        print('\n' + '=' * 10 + '2. Edit' + '=' * 10)
        print('Editing a transaction.')
        print('Current transactions: ', purchase_history)
        name = input('Enter the name of the person whose transaction you want to edit: ')

        if name in purchase_history:
            print(name, ': current amount ', purchase_history[name], 'won.')
            while True:
                price = input('Enter the new amount (in won): ')
                if price.isdigit():
                    price = int(price)
                    break
                else:
                    print('※ Error ※ Please enter a number.')
            purchase_history[name] = price
            print('\n' + name, ':', price, 'won after edit.')
        else:
            print('※ Error ※ The name you entered (' + name + ') is not in the list. Please check again.')

        print('Current transactions: ', purchase_history)


    elif menu == '4':  # Delete transaction
        print('\n' + '=' * 10 + '3. Delete' + '=' * 10)
        print('Deleting a transaction.')
        print('Current transactions: ', purchase_history)
        name = input('Enter the name of the         person whose transaction you want to delete: ')

        if name in purchase_history:
            del purchase_history[name]
            print('Deleted: ', name)
        else:
            print('※ Error ※ The name you entered (' + name + ') is not in the list. Please check again.')

        print('Current transactions: ', purchase_history)


    elif menu == '5':  # Check transactions
        print('\n' + '=' * 10 + '4. Check Transactions' + '=' * 10)
        print('Checking current transactions.')
        print('Current transactions: ', purchase_history)


    elif menu == '6':  # Calculate transactions
        if len(purchase_history) > 1:
            break
        else:
            print('Please enter more than one transaction.')

    elif menu == '7':  # Force exit
        exit()

    else:
        print('※ Error ※ Invalid input. Please try again.')

total = sum(purchase_history.values())  # Total amount
avg = total / len(purchase_history)  # Average amount

purchase_avg = purchase_history.copy()

for name, amount in purchase_avg.items():  # Adjust amounts by average
    purchase_avg[name] -= avg

for name, amount in purchase_avg.items():  # Separate payers from payees
    if amount > 0:
        payees.append([amount, name])
    elif amount < 0:
        payers.append([-amount, name])


def sort_payers_and_payees():
    payers.sort(reverse=True)
    payees.sort(reverse=True)


sort_payers_and_payees()

i, j = 0, 0

while i < len(payers) and j < len(payees):
    payer = payers[i]
    payee = payees[j]

    if payer[0] > payee[0]:
        transactions[payer[1] + '-->' + payee[1]] = str(int(payee[0])) + ' won'
        payer[0] -= payee[0]
        j += 1
    elif payer[0] < payee[0]:
        transactions[payer[1] + '-->' + payee[1]] = str(int(payer[0])) + ' won'
        payee[0] -= payer[0]
        i += 1
    else:
        transactions[payer[1] + '-->' + payee[1]] = str(int(payer[0])) + ' won'
        i += 1
        j += 1

    sort_payers_and_payees()

print('\n' + '=' * 20, 'Total Transactions', '=' * 20, '\n')
print(purchase_history)
print('\n' + '=' * 16, 'Transfer as follows', '=' * 16, '\n')
for key, value in transactions.items():
    print(key, value)
print('\n' + '=' * 52 + '\n')
