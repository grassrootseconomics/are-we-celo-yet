import logging

import pytest
from chainlib.eth.tx import (
    transaction,
    receipt,
    Tx
)
from chainlib.eth.block import (
    block_by_number,
    Block
)
from chainlib_eth_celo import CeloBlockDialectFilter

logg = logging.getLogger(__name__)

def test_fetch_tx():
    block = 15_237_555
    hash = '0xd50cff848bc7ee304bab4763d3dcc00e6c900e1bdb955bfa836ad1ba2d74dde2'

    block_query = block_by_number(block, include_tx=True)
    block_resp = pytest.conn.do(block_query)
    parsed_block = Block(block_resp, dialect_filter=CeloBlockDialectFilter())

    tx_query = transaction(hash)
    tx_resp = pytest.conn.do(tx_query)

    receipt_query = receipt(hash)
    tx_receipt_resp = pytest.conn.do(receipt_query)

    full_parsed_tx = Tx(tx_resp, rcpt=tx_receipt_resp, block=parsed_block)
    logg.debug('full_parsed_tx: \n{}'.format(full_parsed_tx.to_human()))

    assert full_parsed_tx != None
