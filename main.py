from web3 import Web3
import os

def generate_eth_address():
    # Generate a random private key
    private_key = os.urandom(32).hex()
    # Create an account object from the private key
    account = Web3().eth.account.from_key(private_key)
    # Get the address from the account object
    address = account.address
    return {
        "private_key": private_key,
        "address": address
    }

# Generate 500 Ethereum addresses
eth_addresses = [generate_eth_address() for _ in range(500)]

# Write the private keys to a text file
with open('private_keys.txt', 'w') as file:
    for addr in eth_addresses:
        file.write(f"{addr['private_key']}\n")

# Write the addresses to a text file
with open('addresses.txt', 'w') as file:
    for addr in eth_addresses:
        file.write(f"{addr['address']}\n")

print("500 Ethereum private keys have been saved to private_keys.txt")
print("500 Ethereum addresses have been saved to addresses.txt")
