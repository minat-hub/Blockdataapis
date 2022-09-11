import pytest
from decouple import config

from src.blockapiwrapper.base import Explorer

API_TOKEN = config("etherscan_token", default="")

def test_string_calculator_should_return_zero_on_empty_string():
    result = Explorer("0xb38ef143BA4CDE9e66B5f93E23315E979e886D04", API_TOKEN)
    data = result.etherscan_accounts("transactions")
    assert data is not None