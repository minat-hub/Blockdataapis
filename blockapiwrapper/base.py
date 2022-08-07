import requests

class Block:
    def __init__(self, block_id, block_hash, block_size,token):
        self.block_id = block_id
        self.block_hash = block_hash
        self.block_size = block_size
        self.token = token

class Marketplace(Block):
    pass

class Explorer(Block):
    super().__init__()

    def etherscan(self, action):
        if action == "":
            response = requests.get(f"https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag={self.block_id}&apikey={self.token}")
        else:
            response = requests.get(f"https://api.etherscan.io/api?module=account&action=txlist&address=0xc5102fE9359FD9a28f877a67E36B0F050d81a3CC&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={self.token}")


class Exchanges(Block):
    pass
