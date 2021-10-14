from stabilaapi import stabila
from stabilaapi import HttpProvider

full_node = HttpProvider('https://206.81.22.207')
solidity_node = HttpProvider('https://206.81.22.207')
event_server = HttpProvider('https://206.81.22.207')
stabila = stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)


stabila.address.to_hex('TT67rPNwgmpeimvHUMVzFfKsjL9GZ1wGw8')
# result: 41BBC8C05F1B09839E72DB044A6AA57E2A5D414A10

stabila.address.from_hex('41BBC8C05F1B09839E72DB044A6AA57E2A5D414A10')
# result: TT67rPNwgmpeimvHUMVzFfKsjL9GZ1wGw8
