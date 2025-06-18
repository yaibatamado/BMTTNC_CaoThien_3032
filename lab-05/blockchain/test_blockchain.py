from blockchain import Blockchain

my_blockchain = Blockchain()

print("Adding transactions...")
my_blockchain.add_transaction('Alice', 'Bob', 10)
my_blockchain.add_transaction('Bob', 'Charlie', 5)
my_blockchain.add_transaction('Charlie', 'Alice', 3)

print("Mining a new block...")
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof

new_proof = my_blockchain.proof_of_work(previous_proof)

my_blockchain.add_transaction('Genesis', 'Miner', 1)

previous_hash = previous_block.hash
new_block = my_blockchain.create_block(new_proof, previous_hash)

print("\n--- Blockchain Details ---")
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transactions: {block.transactions}")
    print(f"Proof: {block.proof}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("----------------------------")

is_valid = my_blockchain.is_chain_valid(my_blockchain.chain)
print(f"Is Blockchain Valid: {is_valid}")