from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap


def claim_starry(w, a1):
    contract_address = '0xE3bA0072d1da98269133852fba1795419D72BaF4'
    gas_gwei = w.w3.from_wei(40000, 'gwei')
    data = '0x9e4cda43'
    tx_param = w.build_tx_param(a1, contract_address, gas_gwei=gas_gwei, gas_price_gwei=1, data=data)
    (tx_id, rsp, balance) = w.tx_by_param(a1, tx_param)
    print('tx_id:', tx_id, 'rsp:', rsp['status'])



a1 = account_1
w = Web3Wrap.get_instance(block_chain=Block_chain.BSC_ANKR, gas_flag=False)

claim_starry(w, a1)