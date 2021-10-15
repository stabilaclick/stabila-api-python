from stabilaapi import stabila
from stabilaapi import HttpProvider

full_node = HttpProvider('https://api.stabilascan.org')
solidity_node = HttpProvider('https://api.stabilascan.org')
event_server = HttpProvider('https://api.stabilascan.org')
stabila = stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)


print(stabila.address.to_hex('SSVezpwJh55m662o5MsyF85GPVTBD755WR'))
# result: 3F390CE574669E1DF7430B034DF85001EACD818032

print(stabila.address.from_hex('3f390ce574669e1df7430b034df85001eacd818032'))
# result: SSVezpwJh55m662o5MsyF85GPVTBD755WR
