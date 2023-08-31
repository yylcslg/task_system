
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap

a1 = account_1
proxy_ip_str = proxy_ip

w = Web3Wrap(block_chain=Block_chain.BSC_ANKR, proxy_ip=proxy_ip_str, gas_flag=False)
amount = float(w.get_balance(a1.address, unit='ether'))
#if amount< 0.0014:
print('address:', a1.address, 'balance:', amount)


