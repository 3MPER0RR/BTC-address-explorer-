import requests

BASE_URL = "https://blockstream.info/api"
TIMEOUT = 10


def get_address_info(address: str) -> dict:
    r = requests.get(
        f"{BASE_URL}/address/{address}",
        timeout=TIMEOUT
    )
    r.raise_for_status()
    return r.json()


def get_address_txs(address: str) -> list:
    r = requests.get(
        f"{BASE_URL}/address/{address}/txs",
        timeout=TIMEOUT
    )
    r.raise_for_status()
    return r.json()


def get_address_utxo(address: str) -> list:
    r = requests.get(
        f"{BASE_URL}/address/{address}/utxo",
        timeout=TIMEOUT
    )
    r.raise_for_status()
    return r.json()