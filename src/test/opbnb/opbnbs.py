from time import sleep

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap


def mint_opbnbs(w, a1):
    contract_address = a1.address
    gas_gwei = w.w3.from_wei(34000, 'gwei')

    #42.54
    data = '0x646174613a2c7b2270223a226f70622d3230222c226f70223a226d696e74222c227469636b223a226f70626e6273222c22616d74223a2231303030227d'
    for i in range(100):
        try:
            tx_param = w.build_tx_param(a1, contract_address, gas_gwei=gas_gwei, gas_price_gwei=0.00000001, data=data)
            (tx_id, rsp, balance) = w.tx_by_param(a1, tx_param)
            print('opbnb tx_id:', tx_id, 'rsp:', rsp['status'])
            sleep(1)
        except Exception as e:
            sleep(10)
            print('发生错误：{0}'.format(e))


a1 = account_1
w = Web3Wrap.get_instance(block_chain=Block_chain.OPBNB, gas_flag=False)

mint_opbnbs(w, a1)