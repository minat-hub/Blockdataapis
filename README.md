# Blockdataapis
This library allows you to easily access data from different blockchain data provders like exchanges, explorers and Nft Marketplaces.

Sample code on how to use the library using the pandas library:

    scanner = Explorer("0xb38ef143BA4CDE9e66B5f93E23315E979e886D04", API_TOKEN)
    data = scanner.etherscan_accounts("transactions")
    df = pd.DataFrame(data)
    df