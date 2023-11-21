from eth_keys import keys
import os
import dataset_creation
# Number of key pairs to generate
num_key_pairs = 1000
key_pairs = []
private_key_list = []
public_key_list = []
address_list = []
private_key_len = []
public_key_len = []
address_len = []
# Initialize an empty list to store the generated key pairs
key_pairs = []

for _ in range(num_key_pairs):
    # Generate a random 32-byte private key
    private_key_bytes = os.urandom(32)
    
    # Create a PrivateKey instance from the bytes
    private_key = keys.PrivateKey(private_key_bytes)
    
    # Derive the Ethereum public key
    public_key = private_key.public_key
    
    # Derive the Ethereum address from the public key
    ethereum_address = public_key.to_checksum_address()
    
    # Append the private key, public key, and address to the list
    key_pairs.append((private_key.to_hex(), public_key.to_hex(), ethereum_address))

# Print the generated key pairs
for i, (private_key_hex, public_key_hex, ethereum_address) in enumerate(key_pairs):
    print(f"Key Pair {i + 1}")
    private_key_list.append(private_key_hex)
    public_key_list.append(public_key_hex)
    private_key_len.append(len(private_key_hex))
    public_key_len.append(len(public_key_hex))
    address_list.append(ethereum_address)
    address_len.append(len(ethereum_address))
dataset_creation.appending(private_key_list,public_key_list,address_list,private_key_len,public_key_len,address_len)