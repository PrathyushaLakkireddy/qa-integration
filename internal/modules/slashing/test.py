import time, logging
import unittest
from modules.slashing.tx import (
    tx_unjail,
)

logging.basicConfig(format="%(message)s", level=logging.DEBUG)

class TestStakingModuleTxsQueries(unittest.TestCase):

    def test_unjain_tx(self):
        # unjain tx
        status, send_tx = tx_unjail("validator1")
        self.assertTrue(status)
        time.sleep(3)

if __name__ == "__main__":
    logging.info("INFO: running slashing module tests")
    unittest.main()