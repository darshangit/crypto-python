# Initializing blockchain list
MINING_REWARD = 10

genesis_block = {'previous_hash': '',
                 'index': 0,
                 'transaction': []}
blockchain = [genesis_block]
open_transactions = []
owner = 'Dash'
participants = {'Max'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transaction']
                  if tx['sender'] == participant] for block in blockchain]

    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]

    tx_recipient = [[tx['amount'] for tx in block['transaction']
                     if tx['recipient'] == participant] for block in blockchain]

    amount_recieved = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_recieved += tx[0]

    return amount_recieved - amount_sent


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def verify_transaction(tranasction):
    sender_balance = get_balance(tranasction['sender'])
    return sender_balance >= tranasction['amount']

def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value to the kast blockchian

    Arguments:
        :sender: The sender of the coins
        :recipient: The recipeient
        :amount: The amount to be send(default = 1.0)
    """
    transaction = {'sender': sender,
                   'recipient': recipient,
                   'amount': amount}

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False

def mine_block():

    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)

    block = {'previous_hash': hashed_block,
             'index': len(blockchain),
             'transaction': copied_transactions}
    blockchain.append(block)
    return True


def get_transaction_value():
    """ Returns the transaction input by the user """
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount = float(input('Your tarnsaction amount please: '))
    return tx_recipient, tx_amount  # tuple


def get_user_choice():
    user_input = input('Your Choice: ')
    return user_input


def print_blockchain_element():
    for block in blockchain:
        print(block)
    else:
        print('*' * 20)


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue

        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


def verify_transactions():
   return all([verify_transaction(tx) for tx in open_transactions])

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new Block')
    print('3: Output the blocks')
    print('4: Print participants')
    print('5: check transaction validity')
    print('5: Manipulat the block chain')
    print('6: quit')
    user_choice = get_user_choice()

    if user_choice == 1:
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == 2:
        if mine_block():
            open_transactions = []
    elif user_choice == 3:
        print_blockchain_element()
    elif user_choice == 4:
        print(participants)
    elif user_choice == 5:
        if verify_transactions():
            print('Valid transactions')
        else:
            print('Invalid transactions')
    elif user_choice == 6:
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '',
                             'index': 0,
                             'transaction': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 20}]}
    elif user_choice == 7:
        waiting_for_input = False
    else:
        print('Invalid input, please pick from the list')
    if not verify_chain():
        print_blockchain_element()
        print('Invalid blockchain')
        break
    print(get_balance('Dash'))
else:
    print('User Left')

print('!done')
