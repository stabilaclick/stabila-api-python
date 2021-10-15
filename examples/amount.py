from stabilaapi import stabila
from stabilaapi import HttpProvider

full_node = HttpProvider('https://api.stabilascan.org')
solidity_node = HttpProvider('https://api.stabilascan.org')
event_server = HttpProvider('https://api.stabilascan.org')
stabila = stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)



stabila.toUnit(1)
# result: 1000000

stabila.fromUnit(1000000)
# result: 1


