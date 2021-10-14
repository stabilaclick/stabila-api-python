from stabilaapi import stabila
from stabilaapi import HttpProvider

full_node = HttpProvider('https://206.81.22.207')
solidity_node = HttpProvider('https://206.81.22.207')
event_server = HttpProvider('https://206.81.22.207')
stabila = stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)



stabila.toUnit(1)
# result: 1000000

stabila.fromUnit(1000000)
# result: 1


