import requests
import json
import base58
import base64
import csv
import time
import random
from stabilaapi import Stabila
from stabilaapi import HttpProvider

full_node = HttpProvider('https://api.stabilascan.org')
solidity_node = HttpProvider('https://api.stabilascan.org')
event_server = HttpProvider('https://api.stabilascan.org')

stabila = Stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)


stabila.private_key = 'bc9777881f405f421d1d22aaea1083cbe77796420061ab0de148aa3074350a8d'
stabila.default_address = 'SSVezpwJh55m662o5MsyF85GPVTBD755WR'

# added message
def get_balance():
    balance = stabila.stb.get_balance()
    balance = stabila.fromUnit(balance)
    return balance

def sendcoin(toaddress, amount):
    send = stabila.stb.send_transaction(toaddress, amount)
    print(send)


def create_csv(name):
  PATH='/hdd/PYCharm/stabila-api-python/examples/'+name
  with open(PATH, 'w') as f:
    # create the csv writer
    writer = csv.writer(f)


API_URL_BASE = "https://api.stabilascan.org"
ADDRESS = "3f4e6a98dab4a8dc6eb8e4ec162404d22b73d4089d"
CONTRACT = "3f34733cf41dba61ebc0dd75e182103aa488ff99c1"

METHOD_BALANCE_OF = 'balanceOf(address)'


def generate_account():
  url = API_URL_BASE + '/wallet/generateaddress'
  resp = requests.post(url)
  data = resp.json()
  return data


def write_address(b58, hex, pk):
  client=[b58, hex, pk]
  PATH='/hdd/PYCharm/stabila-api-python/examples/list.csv'
  with open(PATH, 'a') as f:
      writer = csv.writer(f)
      writer.writerow(client)

def create_accs(num):
  i = 0
  for i in range(num):
    data = generate_account()
    write_address(data['address'], data['hexAddress'], data['privateKey'])
    time.sleep(1)

def transact(size, amount, rnd, each):
  PATH = '/hdd/PYCharm/stabila-api-python/examples/list.csv'
  with open(PATH, newline='') as f:
      csv_reader = csv.reader(f)
      print(next(csv_reader))
      i = 1
      for row in csv_reader:
        print(i, ".", row, row[0])

        balance = get_balance()
        print("From address balance: ", balance)

        if rnd != 0: amount = random.uniform(amount-rnd, amount+rnd)

        print("Sending amount:", amount, "STB\nTo address:", row[0])

        #Attention: Live transaction
        sendcoin(row[0], amount)

        i = i+1
        if i > size: quit()




#transact(15,20,10,0)
print(get_balance())