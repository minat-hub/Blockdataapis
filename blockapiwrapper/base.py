import requests

class Block:
    def __init__(self, block_id, block_hash, block_size,token,address):
        self.block_id = block_id
        self.block_hash = block_hash
        self.block_size = block_size
        self.token = token
        self.address = address

class Marketplace(Block):
    pass

class Explorer(Block):
    super().__init__()

    def etherscan_accounts(self, action):
        if action == "transactions" or action not in ["internal_transactions", "balance"]:
            response = requests.get(f"https://api.etherscan.io/api?module=account&action=txlist&address={self.address}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={self.token}")

        elif action == "internal_transactions":
            response = requests.get(f"https://api.etherscan.io/api?module=account&action=txlistinternal&address={self.address}&startblock=0&endblock=2702578&page=1&offset=10&sort=asc&apikey={self.token}")

        else:
            response = requests.get(f"https://api.etherscan.io/api?module=account&action=balancemulti&address={self.address}&tag=latest&apikey={self.token}")

        return response.json()
    def etherscan_gastracker(self, action):
        if action == "gas_history":
            response = requests.post(f'https://eth-mainnet.alchemyapi.io/v2/${self.token}')
        else:
            response = requests.get(f"https://api.etherscan.io/api?module=gastracker&action=gasprice&apikey={self.token}")
#         https://api.etherscan.io/api
#    ?module=gastracker
#    &action=gasoracle
#    &apikey=YourApiKeyToken
        return response.json()
    def etherscan_price(self):
        """
        It takes the token from the class and uses it to make a request to the Etherscan API
        :return: A dictionary containing the latest price of 1 ETH.
        """

        response = requests.get(f"https://api.etherscan.io/api?module=stats&action=ethprice&apikey={self.token}")
        return response.json()


class Exchanges(Block):
    pass
