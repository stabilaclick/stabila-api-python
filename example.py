import json
import logging

import stabilaapi.exceptions
from stabilaapi import stabila

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

full_node = 'https://api.stabilascan.org'
solidity_node = 'https://api.stabilascan.org'
event_server = 'https://api.stabilascan.org/'
private_key = '65b0799156e773d8d44d32769770d401d4c80f081ca3ee98fe137d46b16f9c17'

stabila = stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)


account = stabila.create_account
is_valid = bool(stabila.isAddress(account.address.hex))


logger.debug('Generated account: ')
logger.debug('- Private Key: ' + account.private_key)
logger.debug('- Public Key: ' + account.public_key)
logger.debug('- Address: ')
logger.debug('-- Base58: ' + account.address.base58)
logger.debug('-- Hex: ' + account.address.hex)
logger.debug('-- isValid: ' + str(is_valid))
logger.debug('-----------')

current_block = stabila.stb.get_current_block()
logger.debug('Current block: ')
logger.debug(json.dumps(current_block, indent=2))
logger.debug('-----------')

previous_block = stabila.stb.get_block(0)

logger.debug('Previous block #52: ')
logger.debug(json.dumps(previous_block, indent=2))
logger.debug('-----------')


genesis_block_count = stabila.stb.get_block_transaction_count('earliest')
logger.debug('Genesis Block Transaction Count: ')
logger.debug('Transactions:' + str(genesis_block_count))
logger.debug('-----------')

try:
    transaction = stabila.stb.get_transaction('757a14cef293c69b1cf9b9d3d19c2e40a330c640b05c6ffa4d54609a9628758c')

    logger.debug('Transaction: ')
    logger.debug('- Hash: ' + transaction['txID'])
    logger.debug('- Transaction: ' + json.dumps(transaction, indent=2))
    logger.debug('-----------')
except ValueError as ve:
    logger.debug('ID not found')

account_info = stabila.stb.get_account('SUSdSJMerVr1XezP7bjhSANWYkZkyJeQEs')

logger.debug('Account information: ')
logger.debug('- Address: SUSdSJMerVr1XezP7bjhSANWYkZkyJeQEs')
logger.debug('- Account:' + json.dumps(account_info, indent=2))
logger.debug('-----------')


balance = stabila.stb.get_account('SUSdSJMerVr1XezP7bjhSANWYkZkyJeQEs')

logger.debug('Account balance: ')
logger.debug('- Address: SUSdSJMerVr1XezP7bjhSANWYkZkyJeQEs')
logger.debug('- Account:' + json.dumps(balance, indent=2))
logger.debug('-----------')


band_width = stabila.stb.get_band_width('SUSdSJMerVr1XezP7bjhSANWYkZkyJeQEs')

logger.debug('Account bandwidth: ')
logger.debug('- Address: SUSdSJMerVr1XezP7bjhSANWYkZkyJeQEs')
logger.debug('- Bandwidth:' + json.dumps(band_width, indent=2))
logger.debug('-----------')


list_nodes = stabila.stb.list_nodes()

logger.debug('List of full nodes: ')
logger.debug('- Node Count:' + str(len(list_nodes)))
logger.debug('- Nodes:' + json.dumps(list_nodes, indent=2))
logger.debug('-----------')


block_ids = stabila.stb.get_block_range(30, 35)
block = list(map(lambda x: {'id': x['block_header']['raw_data']['number'] or 0}, block_ids))

logger.debug('Block IDs between 30 and 35: ')
logger.debug('- Block Range: [ 30, 35 ]')
logger.debug('- Blocks IDs:' + json.dumps(block, indent=2))
logger.debug('-----------')


# send = stabila.send_stb('TGEJj8eus46QMHPgWQe1FJ2ymBXRm96fn1', 10)
# logger.debug('Send STB transaction: ')
# logger.debug('- Result: ' + json.dumps(send, indent=2))
# logger.debug('-----------')

try:
    event_result = stabila.get_event_result('SUSdSJMerVr1XezP7bjhSANWYkZkyJeQEs', 0, 'Notify')

    logger.debug('Event result:')
    logger.debug('Contract Address: SUSdSJMerVr1XezP7bjhSANWYkZkyJeQEs')
    logger.debug('Event Name: Notify')
    logger.debug('Block Number: 32162')
    logger.debug('- Events: ' + json.dumps(event_result, indent=2))
except TypeError as ve:
    logger.debug('Please provide a valid contract address')

try:
    event_by_transaction_id = stabila.get_event_transaction_id('3d780e1ff5e5033ddf96b7a71fccfb13f88c787ec85c80b8c77e2252344c318c')

    logger.debug('Specific event result:')
    logger.debug('Transaction: 3d780e1ff5e5033ddf96b7a71fccfb13f88c787ec85c80b8c77e2252344c318c')
    logger.debug('- Events: ' + json.dumps(event_by_transaction_id, indent=2))
except stabilaapi.exceptions.TransportError as e:
    logger.debug('No event server setup')

first_transaction = stabila.stb.get_transaction_from_block(0, 0)

logger.debug('First transaction from block 0')
logger.debug('- Transaction: ' + json.dumps(first_transaction, indent=2))

