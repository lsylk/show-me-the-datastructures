from typing import Optional
import hashlib
import datetime

class Block:
    """
    A class to represent a block in the blockchain.

    Attributes:
    -----------
    timestamp : datetime.datetime
        The timestamp when the block was created.
    data : str
        The data stored in the block.
    previous_hash : str
        The hash of the previous block in the chain.
    hash : str
        The hash of the current block.
    """

    def __init__(self, timestamp: datetime.datetime, data: str, previous_hash: str) -> None:
        """
        Constructs all the necessary attributes for the Block object.

        Parameters:
        -----------
        timestamp : datetime.datetime
            The timestamp when the block was created.
        data : str
            The data stored in the block.
        previous_hash : str
            The hash of the previous block in the chain.
        """
        self.timestamp: datetime.datetime = timestamp
        self.data: str = data
        self.previous_hash: str = previous_hash
        self.hash: str = self.calc_hash()

    def calc_hash(self) -> str:
        """
        Calculate the hash of the block using SHA-256.

        Returns:
        --------
        str
            The hash of the block.
        """
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self) -> str:
        """
        Return a string representation of the block.

        Returns:
        --------
        str
            A string representation of the block.
        """
        return (f"Block(\n"
                f"  Timestamp: {self.timestamp},\n"
                f"  Data: {self.data},\n"
                f"  Previous Hash: {self.previous_hash},\n"
                f"  Hash: {self.hash}\n"
                f")\n")
class Node:

    def __init__(self, val: Block) -> None:
        self.value = val
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return str(self.value)
            
class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.curr = None
    
    def append(self, block: Block) -> None:
        if self.head is None:
            self.head = Node(block)
            self.tail = self.head
        else:
            next =  Node(block)
            assert self.tail
            self.tail.next = next
            self.tail = next

    def __iter__(self):
        self.curr = self.head
        return self

    def __next__(self):
        if self.curr is None:
            raise StopIteration
        result = self.curr.value
        self.curr = self.curr.next
        return result

    def __len__(self) -> int:
        length = 0
        curr = self.head
        while curr is not None:
            length += 1
            curr = curr.next
        return length


class Blockchain:
    """
    A class to represent a blockchain.

    Attributes:
    -----------
    chain : list[Block]
        The list of blocks in the blockchain.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the Blockchain object.
        """
        self.chain: LinkedList = LinkedList()
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Create the genesis block (the first block in the blockchain).
        """
        # Genesis block has no previous hash and empty data
        genesis = Block(datetime.datetime.now(), "", "")
        if len(self.chain) == 0:
            self.chain.append(genesis)
        else:
            return


    def add_block(self, data: str) -> None:
        """
        Add a new block to the blockchain.

        Parameters:
        -----------
        data : str
            The data to be stored in the new block.
        """
        assert self.chain.tail
        self.chain.append(Block(datetime.datetime.now(), data, self.chain.tail.value.hash))

    def __repr__(self) -> str:
        """
        Return a string representation of the blockchain.

        Returns:
        --------
        str
            A string representation of the blockchain.
        """
        chain_str = ""
        for block in self.chain:
            chain_str += str(block) + "\n"
        return chain_str

if __name__ == "__main__":
    # Test cases
    # Test Case 1: Create a blockchain and add blocks
    print("Test Case 1: Basic blockchain functionality")
    blockchain = Blockchain()
    blockchain.add_block("Block 1 Data")
    blockchain.add_block("Block 2 Data")
    blockchain.add_block("Block 3 Data")
    print(blockchain)
    assert len(blockchain.chain) == 4

    # Test Case 2
    blockchain_test = Blockchain()
    assert len(blockchain_test.chain) == 1

    # Test Case 3
    blockchain_2 = Blockchain()
    assert blockchain_2.chain.head
    hash = blockchain_2.chain.head.value.hash
    blockchain_2.create_genesis_block()
    assert hash == blockchain_2.chain.head.value.hash
