from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.utils.wallet_account import Wallet


def eddy_fiance_swap(w, a):
    print('-----------------eddy_fiance_swap----------------------------------')
    contract_address = '0xDE3167958Ad6251E8D6fF1791648b322Fc6B51bD'
    gas_gwei = w.w3.from_wei(210000, 'gwei')
    gas_price_gwei = 16

    data = '0x148e6bcc0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000020000000000000000000000005f0b1a82749cb4e2278ec87f8bf6b618dc71a8bf00000000000000000000000048f80608b672dc30dc7e3dbbd0343c5f02c738eb'
    tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=gas_price_gwei, data=data, value_eth = 2)
    (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
    print('tx_id:', tx_id, 'rsp:', rsp['status'])





def zeta_swap_approvel(w, a):
    print('-----------------zeta_swap_approvel----------------------------------')
    contract_address = '0x48f80608B672DC30DC7e3dbBd0343c5F02C738Eb'
    gas_gwei = w.w3.from_wei(40000, 'gwei')
    gas_price_gwei = 14

    data = '0x148e6bcc0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000020000000000000000000000005f0b1a82749cb4e2278ec87f8bf6b618dc71a8bf00000000000000000000000048f80608b672dc30dc7e3dbbd0343c5f02c738eb'
    tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=gas_price_gwei, data=data)
    (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
    print('tx_id:', tx_id, 'rsp:', rsp['status'])
    pass


def zeta_swap_bsc_to_zeta(w, a):
    print('-----------------zeta_swap_bsc_to_zeta----------------------------------')
    contract_address = '0xc6f7a7ba5388bFB5774bFAa87D350b7793FD9ef1'
    gas_gwei = w.w3.from_wei(400000, 'gwei')
    gas_price_gwei = 18


def zeta_swap_zeta_to_eth(w, a):
    pass


def zeta_swap_zeta_to_btc(w, a):
    pass


#https://explorer.zetachain.com/evm/tx/0xbada7cc3f22b081df941de98f2d9f9640b8a9212357fac65f329dc00ba54283b
def add_pool(w, a):
    pass




def zeta_earn(w, a):
    print('-----------------zeta_earn----------------------------------')
    contract_address = '0x45334a5B0a01cE6C260f2B570EC941C680EA62c0'
    gas_gwei = w.w3.from_wei(300000, 'gwei')
    gas_price_gwei = 16

    data = '0x5bcb2fc6'
    tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=gas_price_gwei, data=data, value_eth=0.002)
    (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
    print('tx_id:', tx_id, 'rsp:', rsp['status'])
    pass



def accumulated_mint(w,a):
    print('-----------------accumulated_mint----------------------------------')
    contract_address = '0xcf1A40eFf1A4d4c56DC4042A1aE93013d13C3217'
    gas_gwei = w.w3.from_wei(80000, 'gwei')
    gas_price_gwei = 16

    data = '0xf340fa01'+ w.hex_zfill(a.address).lower()
    tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=gas_price_gwei, data=data,
                                value_eth=0.001)
    (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
    print('tx_id:', tx_id, 'rsp:', rsp['status'])
    pass



def accumulated_stake(w,a):
    print('-----------------accumulated_mint----------------------------------')
    contract_address = '0x7AC168c81F4F3820Fa3F22603ce5864D6aB3C547'
    gas_gwei = w.w3.from_wei(100000, 'gwei')
    gas_price_gwei = 16

    data = '0x6e553f6500000000000000000000000000000000000000000000000000005af3107a4000'+ w.hex_zfill(a.address).lower()
    tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=gas_price_gwei, data=data)
    (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
    print('tx_id:', tx_id, 'rsp:', rsp['status'])
    pass



a1 = account_1
w = Web3Wrap(block_chain=Block_chain.ZETA, gas_flag=False)
eddy_fiance_swap(w, a1)
zeta_earn(w, a1)
accumulated_mint(w, a1)
accumulated_stake(w,a1)


if __name__ == '__main__':
    w = Web3Wrap(block_chain=Block_chain.ZETA, gas_flag=False)
    accounts = Wallet.read_test_wallet(file_path_prefix='../../../resource/')
    a = accounts[2]

    #eddy_fiance_swap(w, a)

    print('finish.....')
    pass
