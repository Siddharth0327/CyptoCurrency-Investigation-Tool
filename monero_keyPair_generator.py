from monero.wallet import Wallet

# Number of key pairs to generate
num_key_pairs = 10

# Initialize an empty list to store the generated key pairs
key_pairs = []

for _ in range(num_key_pairs):
    # Create a new Monero wallet
    wallet = Wallet()
    
    # Generate a new Monero address and view key
    address = wallet.get_address()
    view_key = wallet.view_key
    
    # Append the address and view key to the list
    key_pairs.append((address, view_key))

# Print the generated key pairs
for i, (address, view_key) in enumerate(key_pairs):
    print(f"Key Pair {i + 1}")
    print(f"Monero Address: {address}")
    print(f"Monero View Key: {view_key}\n")
