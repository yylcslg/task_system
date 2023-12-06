from time import sleep

from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap


def mint_ipol(w, a1):
    to_address = a1.address
    gas_gwei = w.w3.from_wei(22024, 'gwei')

    #42.54
    data = '0x646174613a2c7b2270223a227072632d3230222c226f70223a226d696e74222c227469636b223a2269706f6c222c22616d74223a2231303030227d'
    for i in range(10):
        try:
            print('----------------------num:(' + str(i) + ') address:'+to_address+'--------------------------------')
            tx_param = w.build_tx_param(a1, to_address, gas_gwei=gas_gwei, gas_price_gwei=200, data=data)
            (tx_id, rsp, balance) = w.tx_by_param(a1, tx_param)
            print('tx_id:', tx_id, 'rsp:', rsp['status'])
            sleep(1)
        except Exception as e:
            sleep(10)
            print('发生错误：{0}'.format(e))



a1 = account_1
w = Web3Wrap.get_instance(block_chain=Block_chain.POLYGON, gas_flag=False)

mint_ipol(w, a1)