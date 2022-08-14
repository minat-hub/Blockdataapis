from base import Explorer, Marketplace, Exchanges
import pandas as pd
import requests
from decouple import config

API_TOKEN = config("etherscan_token", default="")

def main():
    scanner = Explorer("0xb38ef143BA4CDE9e66B5f93E23315E979e886D04", API_TOKEN)
    data = scanner.etherscan_accounts("transactions")
    return pd.DataFrame(data)


if __name__ == "__main__":
    main()
   