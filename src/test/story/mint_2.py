
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.utils.wallet_account import Wallet


def process():
    w = Web3Wrap(block_chain=Block_chain.Story, gas_flag=False)
    wallet = Wallet()

    #mint(w,wallet)
    print_msg(w, wallet)



## 0---89---    150 ---250
def mint(w:Web3Wrap, wallet:Wallet):
    file_name='tinc_wallet_8.csv'
    num = 0
    end_num = 1
    other_account = wallet.read_wallet_file(file_name=file_name,
                                            file_path_prefix='../../../resource/')[num:end_num]  # 等待收集的账户

    gas_gwei = w.w3.from_wei(1361328, 'gwei')
    gas_price_gwei = 734.4

    for a in other_account:
        print('------------------------', file_name,'---',num, '--------------------------------------------')
        num = num + 1
        contract_address = '0xFaa402A8bc7C88D252cd4Bc64C154fcB8031d015'  # 合约地址

        func='0xab2a91c3'
        data = func + '0000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000042307830303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030000000000000000000000000000000000000000000000000000000000000'
        tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei =gas_price_gwei,data=data,nonce=0)
        (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)






def print_msg(w:Web3Wrap, wallet:Wallet):
    other_account = wallet.read_wallet_file(file_name='tinc_wallet_9.csv',
                                            file_path_prefix='../../../resource/')[298:]  # 等待收集的账户

    for a in other_account:
        balance = w.get_balance(a.address, unit='ether')
        print(a.address,'  ',balance)





if __name__ == '__main__':
    process()

    print('finish.....')
    pass