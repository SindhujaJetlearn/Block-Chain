from web3 import Web3
#ganache URL
#web3=Web3(Web3.HTTPProvider(infura_url))
#ganache RPC server link can be used
w3=Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
print(w3.is_connected())
if w3.is_connected():
    print("Transaction Initiated!")


else:
    print("Please open your ganache to see the results")

def balance(address):
    balance=w3.eth.get_balance(address)
    balance_eth=w3.from_wei(balance,"ether")
    print("The balance of account " + address + " is " +str(balance_eth) +"ether")


#public key of acc1
acc1="0x2469Cac4503C6d04558B0Fb14c06ec4214100E3f"
#private key of acc1
acc1_pk="0xac5d601ecc554c0a762b165427114812fe5b6da39de239823f60f90beca8969d"
#public key of acc2
acc2="0xDFc23156f525b13F445cd541D395BCeeDFFeD1C9"
balance(acc1)
balance(acc2)

#transaction
#step 1

nonce=w3.eth.get_transaction_count(acc1)
tx={
    'nonce':nonce,
    'to': acc2,
    'value':w3.to_wei(10,'ether'),
    'gas':200000,
    'gasPrice':w3.to_wei(50,'gwei')
}
print(tx)


#step2
signed_tx=w3.eth.account.sign_transaction(tx,acc1_pk)


#step3
tx_hash=w3.eth.send_raw_transaction(signed_tx.rawTransaction)

print(w3.to_hex(tx_hash))

balance(acc1)
balance(acc2)