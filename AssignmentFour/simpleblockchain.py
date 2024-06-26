
#import library
import hashlib

#create a Block class
class Block:
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    #Create method that calculates the hash using SHA-256
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()

# Create a Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    #Create a method that creates the first block in the blockchain also known as the 'Genesis Block'
    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    #Create a method that creates a new block and adds it to the blockchain (the list)
    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(data, prev_block.hash)
        self.chain.append(new_block)

# Test the Blockchain
blockchain = Blockchain()
blockchain.add_block("First Block after Genesis")
blockchain.add_block("Second Block after Genesis")

# Print out the blockchain
for block in blockchain.chain:
    print(f"Block Data: {block.data}")
    print(f"Block Hash: {block.hash}")
    print(f"Previous Hash: {block.prev_hash}")
    print("\n")
