from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap


def echo_zeta_balance(w, a1, a2):
    print('a1 address:', a1.address, w.get_balance(a1.address,unit = 'ether'))
    print('a2 address:', a2.address, w.get_balance(a2.address, unit='ether'))

    amount1 = float(w.get_balance(a1.address, unit='ether')) # zeta
    amount2 = float(w.get_balance(a2.address, unit='ether')) # zeta


    gas_gwei = w.w3.from_wei(21000, 'gwei')
    w.tx_amount(from_account=a1, to_address=a2.address, amount=0.01, gas_gwei=gas_gwei, gas_price_gwei=14)
    w.tx_amount(from_account=a2, to_address=a1.address, amount=0.01, gas_gwei=gas_gwei, gas_price_gwei=14)
    print('address:', a1.address, 'balance:', amount1, 'address2:', a2.address, 'balance:', amount2, )





a1 = account_1
a2 = account_2[0]

w = Web3Wrap(block_chain=Block_chain.ZETA, gas_flag=False)

echo_zeta_balance(w, a1, a2)
