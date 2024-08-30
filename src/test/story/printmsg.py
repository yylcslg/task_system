
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.utils.wallet_account import Wallet


def process():
    w = Web3Wrap(block_chain=Block_chain.Story, gas_flag=False)
    wallet = Wallet()

    print_msg(w, wallet)





def print_msg(w:Web3Wrap, wallet:Wallet):
    other_account = wallet.read_wallet_file(file_name='tinc_wallet_7.csv',
                                            file_path_prefix='../../../resource/')[:]  # 等待收集的账户

    for a in other_account:
        #balance = w.get_balance(a.address, unit='ether')
        print(a.address)





if __name__ == '__main__':
    process()

    print('finish.....')
    pass