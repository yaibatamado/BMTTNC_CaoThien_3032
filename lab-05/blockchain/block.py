import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, proof):
        """
        Constructor cho một Block.
        :param index: ID của Block.
        :param previous_hash: Hash của Block trước đó.
        :param timestamp: Thời gian tạo Block.
        :param transactions: Danh sách các giao dịch trong Block.
        :param proof: Bằng chứng (Proof of Work).
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Tính toán hash SHA-256 cho Block.
        """
        data = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.transactions) + str(self.proof)
        
        return hashlib.sha256(data.encode()).hexdigest()