import requests
from decouple import config

API_TOKEN = config("etherscan_token", default="")


class Block:
    def __init__(
        self,
        address=None,
        token=None,
        block_id=None,
        block_hash=None,
        block_size=None,
    ):
        self.block_id = block_id
        self.block_hash = block_hash
        self.block_size = block_size
        self.token = token
        self.address = address


class Marketplace(Block):
    pass


class Explorer(Block):
    def __init__(self, address, token):
        """
        The function __init__ is a constructor that takes two parameters, address and token, and calls
        the superclass constructor with the same parameters.
        
        :param address: The address of the server
        :param token: The token of the bot you want to use
        """
        super(self.__class__, self).__init__(address, token)

    def etherscan_accounts(self, action):
        """
        It takes an action as a parameter and returns the result of the request
        
        :param action: The action you want to perform
        :return: A list of dictionaries.
        """
        if action == "transactions" or action not in [
            "internal_transactions",
            "balance",
        ]:
            response = requests.get(
                f"https://api.etherscan.io/api?module=account&action=txlist&address={self.address}&startblock=0&endblock=99999999&sort=asc&apikey={self.token}"
            )

        elif action == "internal_transactions":
            response = requests.get(
                f"https://api.etherscan.io/api?module=account&action=txlistinternal&address={self.address}&startblock=0&endblock=2702578&sort=asc&apikey={self.token}"
            )

        else:
            response = requests.get(
                f"https://api.etherscan.io/api?module=account&action=balancemulti&address={self.address}&tag=latest&apikey={self.token}"
            )

        if response.status_code == 404:
            raise Exception(f"Address {self.address} or Token {self.token} not found")
        else:
            return response.json().get("result")

    def etherscan_gastracker(self, action):
        """
        It takes in an action parameter, and if the action is "gas_history", it makes a POST request to
        the Alchemy API, otherwise it makes a GET request to the Etherscan API
        
        :param action: gas_history
        :return: The response.json() is being returned.
        """
        if action == "gas_history":
            response = requests.post(
                f"https://eth-mainnet.alchemyapi.io/v2/${self.token}"
            )
        else:
            response = requests.get(
                f"https://api.etherscan.io/api?module=gastracker&action=gasprice&apikey={self.token}"
            )

        return response.json().get("result")

    def etherscan_price(self):
        """
        It takes the token from the class and uses it to make a request to the Etherscan API
        :return: A dictionary containing the latest price of 1 ETH.
        """

        response = requests.get(
            f"https://api.etherscan.io/api?module=stats&action=ethprice&apikey={self.token}"
        )
        return response.json().get("result")


class Exchanges(Block):
    pass
