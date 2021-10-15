from stabilaapi import stabila
from stabilaapi import HttpProvider

full_node = HttpProvider('https://api.stabilascan.org')
solidity_node = HttpProvider('https://api.stabilascan.org')
event_server = HttpProvider('https://api.stabilascan.org')

# option 1
stabila = stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)

# option 2
stabila_v2 = stabila()

# option 3
stabila_v3 = stabila(
    default_address='TRWBqiqoFZysoAeyR1J35ibuyc8EvhUAoY',
    private_key='...'
)
