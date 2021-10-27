from stabilaapi import Stabila
from stabilaapi import HttpProvider

full_node = HttpProvider('https://api.stabilascan.org')
solidity_node = HttpProvider('https://api.stabilascan.org')
event_server = HttpProvider('https://api.stabilascan.org')

stabila = Stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)


stabila.private_key = 'bc9777881f421d1d22aaea1083c7796420061ab0de148aa3074350a8d'
stabila.default_address = 'SSVezpw62o5MsyF85GPVTBD755WR'

# added message
def get_balance():
    balance = stabila.stb.get_balance()
    print(stabila.fromUnit(balance))
    return balance

def sendcoin(toaddress, amount):
    send = stabila.stb.send_transaction(toaddress, amount)
    print(send)
