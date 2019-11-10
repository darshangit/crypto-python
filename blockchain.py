# Initializing blockchain list

blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[3]):
    """ Append a new value to the kast blockchian

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The previous transaction value
    """
    if last_transaction == None:
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


def get_transaction_value():
    """ Returns the transaction input by the user """
    return int(input('Your tarnsaction amount please: '))


def get_user_choice():
    user_input = input('Your Choice: ')
    return user_input


def print_blockchain_element():
    for block in blockchain:
        print(block)
    else:
        print('*' * 20)


def verify_chain():
    block_index = 0
    is_valid = True

    for block_index in range(len(blockchain)):
        if block_index == 0:
                continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break

        # for block in blockchain:
        #     if block_index == 0:
        #         block_index += 1
        #         continue
        #     elif block[0] == blockchain[block_index - 1]:
        #         is_valid = True
        #     else:
        #         is_valid = False
        #         break
        #     block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blocks')
    print('3: Manipulat the block chain')
    print('4: quit')
    user_choice = get_user_choice()

    if user_choice == 1:
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == 2:
        print_blockchain_element()
    elif user_choice == 3:
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 4:
        waiting_for_input = False
    else:
        print('Invalid input, please pick from the list')
    if not verify_chain():
        print_blockchain_element()
        print('Invalid blockchain')
        break
else:
    print('User Left')

print('!done')
