import pytest
from chainlib.eth.connection import (
    EthHTTPConnection
)
from chainlib_eth_celo import CeloUtil

def pytest_configure():
    pytest.conn = EthHTTPConnection(url='https://rpc.celo.grassecon.net', chain_spec=CeloUtil.CHAIN_SPEC)
