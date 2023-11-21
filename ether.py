from web3 import Web3
from eth_account import Account
import os

# Number of key pairs to generate
num_key_pairs = 10

# Initialize a Web3 instance connected to an Ethereum node or network
# You can use Infura or a local Ethereum node for this purpose
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Initialize an empty list to store the generated key pairs
key_pairs = []

for _ in range(num_key_pairs):
    # Generate a new Ethereum private key
    private_key = Web3.toHex(os.urandom(32))
    
    # Derive the Ethereum address from the private key
    account = Account.privateKeyToAccount(private_key)
    
    # Append the private key, public key, and address to the list
    key_pairs.append((private_key, account.address))

# Print the generated key pairs
for i, (private_key, ethereum_address) in enumerate(key_pairs):
    print(f"Key Pair {i + 1}")
    print(f"Private Key: {private_key}")
    print(f"Ethereum Address: {ethereum_address}")
    print(f"Public Key: {account.public_key.to_hex()}\n")
