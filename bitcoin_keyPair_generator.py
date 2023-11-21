import bitcoin
import dataset_creation
# Number of key pairs to generate
num_key_pairs = 1000

# Initialize an empty list to store the generated key pairs
key_pairs = []
private_key_list = []
public_key_list = []
address_list = []
private_key_len = []
public_key_len = []
address_len = []

for _ in range(num_key_pairs):
    # Generate a new Bitcoin private key (in WIF format)
    private_key = bitcoin.random_key()
    
    # Derive the corresponding Bitcoin public key
    public_key = bitcoin.privkey_to_pubkey(private_key)
    
    # Derive the Bitcoin address from the public key
    bitcoin_address = bitcoin.pubkey_to_address(public_key)
    
    # Append the private key, public key, and address to the list
    key_pairs.append((private_key, public_key, bitcoin_address))

# Print the generated key pairs
for i, (private_key, public_key, bitcoin_address) in enumerate(key_pairs):
    print(f"Key Pair {i + 1}")
    private_key_list.append(private_key)
    public_key_list.append(public_key)
    address_list.append(bitcoin_address)
    private_key_len.append(len(private_key))
    public_key_len.append(len(public_key))
    address_len.append(len(bitcoin_address))

dataset_creation.appending(private_key_list,public_key_list,address_list,private_key_len,public_key_len,address_len)