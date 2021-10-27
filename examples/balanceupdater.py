import csv
from stabilaapi import Stabila
from stabilaapi import HttpProvider
import requests
import json
import base58
import base64

full_node = HttpProvider('https://api.stabilascan.org')
solidity_node = HttpProvider('https://api.stabilascan.org')
event_server = HttpProvider('https://api.stabilascan.org')

stabila = Stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)



PATH = '/hdd/PYCharm/stabila-api-python/examples/list.csv'


def get_balance():
  balance = stabila.stb.get_balance()
  balance = stabila.fromUnit(balance)
  return balance

def balance_updater(path, size):
    header = ['address', 'hexaddress', 'pk', 'balance']
    with open('listupdated.csv', 'w', encoding='UTF8', newline='') as fw:
        writer = csv.writer(fw)
        writer.writerow(header)
        with open(path, newline='') as f:
            csv_reader = csv.reader(f)
            print(next(csv_reader))

            i = 1
            for row in csv_reader:
                print(i, ".", row)
                stabila.private_key = row[2]
                stabila.default_address = row[0]

                balance = get_balance()
                print("Address: ", row[0], "\nBalance: ", balance)
                row.append(balance)
                print(row)
                if balance > 0:
                    print("Saving balance")
                    writer.writerow(row)
                else:
                    print("Balance is 0. Skipping...")

                i = i+1
                if i > size: quit()



balance_updater(PATH, 15)

