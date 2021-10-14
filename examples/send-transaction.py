from stabilaapi import stabila
from stabilaapi import HttpProvider

full_node = HttpProvider('https://206.81.22.207')
solidity_node = HttpProvider('https://206.81.22.207')
event_server = HttpProvider('https://206.81.22.207')

stabila = stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)


stabila.private_key = 'private_key'
stabila.default_address = 'default address'

# added message
send = stabila.stb.send_transaction('to', 1)

print(send)
