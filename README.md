# Blockdataapis
[![Deon badge](https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square)](http://deon.drivendata.org/)

Blockdataapis is a Python library to access data from different blockchain data provders like exchanges, explorers and Nft Marketplaces. This library enables you to manage blockchain data in your Python applications.
## Install
    $ pip install blockdataapis

Sample code on how to use the library using the pandas library:

    from blockdataapis import Explorer

    scanner = Explorer("0xb38ef143BA4CDE9e66B5f93E23315E979e886D04", API_TOKEN)
    data = scanner.etherscan_accounts("transactions")
    df = pd.DataFrame(data)
    df