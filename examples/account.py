
import logging
from stabilaapi import stabila

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

full_node = 'https://206.81.22.207'
solidity_node = 'https://206.81.22.207'
event_server = 'https://206.81.22.207/'
private_key = 'da146374a75310b9666e834ee4ad0866d6f4035967bfc76217c5a495fff9f0d0'

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

