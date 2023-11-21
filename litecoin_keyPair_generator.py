import ecdsa
import hashlib
import binascii
import base58
import dataset_creation

# Number of key pairs to generate
num_key_pairs = 990
key_pairs = []
private_key_list = []
public_key_list = []
address_list = []
private_key_len = []
public_key_len = []
address_len = []
# Define a function to perform Base58 encoding
def base58_encode(hex_string):
    return base58.b58encode(hex_string).decode()

# Initialize an empty list to store the generated key pairs
key_pairs = []

for _ in range(num_key_pairs):
    # Generate a new Litecoin private key
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    
    # Derive the Litecoin public key
    public_key = private_key.get_verifying_key()
    
    # Derive the Litecoin address from the public key
    public_key_bytes = public_key.to_string()
    sha256_hash = hashlib.sha256(public_key_bytes).digest()
    ripemd160_hash = hashlib.new('ripemd160')
    ripemd160_hash.update(sha256_hash)
    litecoin_address = ripemd160_hash.digest()
    litecoin_address_hex = binascii.hexlify(litecoin_address).decode()
    
    # Append the private key, public key, and address to the list
    key_pairs.append((private_key.to_string().hex(), public_key.to_string().hex(), litecoin_address_hex))

# Print the generated key pairs
for i, (private_key_hex, public_key_hex, litecoin_address_hex) in enumerate(key_pairs):
    print(f"Key Pair {i + 1}")
    private_key_list.append(private_key_hex)
    public_key_list.append(public_key_hex)
    private_key_len.append(len(private_key_hex))
    public_key_len.append(len(public_key_hex))
    base58_encoded_address = base58_encode(bytes.fromhex('30' + litecoin_address_hex))
    address_list.append(base58_encoded_address)
    address_len.append(len(base58_encoded_address))
dataset_creation.appending(private_key_list,public_key_list,address_list,private_key_len,public_key_len,address_len)
