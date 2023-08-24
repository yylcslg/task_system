import time

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.utils.wallet_account import Wallet

# a = random.choice(list1)


#w = Web3Wrap(block_chain=Block_chain.BSC_ANKR, gas_flag=False)
start_num = 0
accounts_1 = Wallet.read_wallet_file(file_name='tinc_wallet_1.csv')[start_num:40]


num = start_num
for a in accounts_1:
    print('------------------------', num, ' echo balance--------------------------------------------')
    num = num + 1
    amount = float(w.get_balance(a.address, unit='ether'))
    #if amount< 0.0014:
    print('address:', a.address, 'balance:', amount)

