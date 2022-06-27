import json, os
from utils import exec_command

DAEMON = os.getenv("DAEMON")
DENOM = os.getenv("DENOM")
CHAINID = os.getenv("CHAINID")
HOME = os.getenv("HOME")
DAEMON_HOME = os.getenv("DAEMON_HOME")
RPC = os.getenv("RPC")
DEFAULT_GAS = 2000000

# tx_unjail unjail validator previously jailed for downtime.
def tx_unjail(
    from_key,
    gas=DEFAULT_GAS,
    unsigned=False,
    sequence=None,
):
    try:
        if unsigned:
            command = f"{DAEMON} tx slashing unjail --from {from_key} --chain-id {CHAINID} --output json --node {RPC} --generate-only --gas {gas}"
            Tx, Txerr = exec_command(command)
            if len(Txerr):
                return False, Txerr
            return True, json.loads(Tx)
        else:
            if sequence != None:
                command = f"{DAEMON} tx slashing unjail --from {from_key} --chain-id {CHAINID} --keyring-backend test --home {DAEMON_HOME}-1 --node {RPC} --output json -y --sequence {sequence} --gas {gas}"

            else:
                command = f"{DAEMON} tx slashing unjail --from {from_key} --chain-id {CHAINID} --keyring-backend test --home {DAEMON_HOME}-1 --node {RPC} --output json -y --gas {gas}"
            Tx, Txerr = exec_command(command)
            Tx = json.loads(Tx)
            if len(Txerr):
                return False, Txerr
            elif Tx["code"] != 0:
                return False, Tx
            return True, Tx
    except Exception as e:
        return False, e
