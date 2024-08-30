from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
import json
from datetime import datetime, timedelta
from eth_account import Account

from src.utils.wallet_account import Wallet

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'



# https://app.infinityai.network?ref-code=78c3cc0cd6f368e6
def refer(w:Web3Wrap, a:Account):
    pass



a = account_1

w = Web3Wrap.get_instance(block_chain=Block_chain.Sepolia, gas_flag=False)
token = refer(w, a)
