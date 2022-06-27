import time, logging
from core.keys import keys_show
from modules.slashing.tx import (
    tx_unjail,
)

logging.basicConfig(format="%(message)s", level=logging.DEBUG)

# unjain tx
status, send_tx = tx_unjail("validator1")
if not status:
    logging.error(f"unjain tx status:: {status}")
else:
    logging.info(f"tx_hash of unjail :: {send_tx['txhash']}")

time.sleep(3)