from stabilaapi import stabila
from stabilaapi import HttpProvider

full_node = HttpProvider('https://api.stabilagrid.io')
solidity_node = HttpProvider('https://api.stabilagrid.io')
event_server = HttpProvider('https://api.stabilagrid.io')
stabila = stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)



stabila.toSun(1)
# result: 1000000

stabila.fromSun(1000000)
# result: 1


