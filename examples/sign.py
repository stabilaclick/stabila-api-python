from stabilaapi import Stabila
from stabilaapi import HttpProvider
from stabilaapi.stb import Stb

full_node = HttpProvider('https://api.stabilascan.org')
solidity_node = HttpProvider('https://api.stabilascan.org')
event_server = HttpProvider('https://api.stabilascan.org')

stabila = Stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)


stabila.private_key = 'private_key'
stabila.default_address = 'default address'



# create transaction
create_tx = stabila.transaction_builder.send_transaction('to', 1, 'from')

# offline sign
offline_sign = stabila.stb.sign(create_tx)


# online sign (Not recommended)
online_sign = stabila.stb.online_sign(create_tx)

