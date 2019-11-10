# Initializing blockchain list

blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=3):
    """ Append a new value to the kast blockchian

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The previous transaction value
    """
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


def get_user_input():
    """ Returns the transaction input by the user """
    return float(input('Your tarnsaction amount please: '))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(),
          transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())
