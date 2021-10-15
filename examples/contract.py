import solcx
from stabilaapi import stabila, HttpProvider
from solcx import compile_source

full_node = HttpProvider('https://api.stabilascan.org')
solidity_node = HttpProvider('https://api.stabilascan.org')
event_server = HttpProvider('https://api.stabilascan.org')


stabila = stabila(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)


# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.25;

contract Hello {
    string public message;

    function Hello(string initialMessage) public {
        message = initialMessage;
    }

    function setMessage(string newMessage) public {
        message = newMessage;
    }
}

'''
print(solcx.get_installable_solc_versions())
#solcx.install_solc('0.4.25', show_progress=False, solcx_binary_path="/hdd/PYCharm/stabila-api-python/solc/")
#solcx.compile_solc('0.4.0', show_progress=False, solcx_binary_path="/hdd/PYCharm/stabila-api-python/solc/")
solcx.set_solc_version('0.4.25', silent=False, solcx_binary_path="/hdd/PYCharm/stabila-api-python/solc/")

compiled_sol = compile_source(contract_source_code)

contract_interface = compiled_sol['<stdin>:Hello']

hello = stabila.stb.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin']
)

# Submit the transaction that deploys the contract
tx_data = hello.deploy(
    fee_limit=10**6,
    call_value=0,
    consume_user_resource_percent=1
)

sign = stabila.stb.sign(tx_data)
result = stabila.stb.broadcast(sign)
