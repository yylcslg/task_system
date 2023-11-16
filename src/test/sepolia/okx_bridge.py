from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap


def sep_echo_dispatch(w, a1, a2):
    amount1 = float(w.get_balance(a1.address, unit='ether'))
    amount2 = float(w.get_balance(a2.address, unit='ether'))

    gas_gwei = w.w3.from_wei(29000, 'gwei')
    if amount1< 0.1:
        w.tx_amount(from_account=a2, to_address=a1.address, amount=0.1, gas_gwei=gas_gwei, gas_price_gwei=1)
    print('address:', a1.address, 'balance:', amount1, 'address2:', a2.address, 'balance:', amount2,)


#https://sepolia.etherscan.io/tx/0xf2fa6edf34aaac33ec593d9e8513a29676f91d7dc31e2fec27a2cdbe234fef22
def mint_okb(w, a):
    contract_address = '0xf875fEcfF122927E53C3b07F4258C690b026004b'
    gas_gwei = w.w3.from_wei(129000, 'gwei')
    data = '0x40c10f190000000000000000000000003f4b6664338f23d2397c953f2ab4ce8031663f800000000000000000000000000000000000000000000000008ac7230489e80000'
    tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=1.6, data=data)
    (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
    print('tx_id:', tx_id, 'rsp:', rsp['status'])


def okb_sep_approve(w, a):
    contract_address = '0x3F4B6664338F23d2397c953f2AB4Ce8031663f80'
    gas_gwei = w.w3.from_wei(90000, 'gwei')

    new_address = str.lower(a.address)[2:]
    old_address = '3141ccbcc38fecb363d52f3a03eec86ccdbe34eb'

    data = '0x095ea7b30000000000000000000000007a4ee6f9f0ab037fe771fc36d39c1e19bcc0fdb50000000000000000000000000000000000000000000000008ac7230489e80000'
    new_data = data.replace(old_address, new_address)
    tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=1.6, data=new_data)

    (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
    print('tx_id:', tx_id, 'rsp:', rsp['status'])

def okb_bridge_sep_x1(w, a):
    contract_address = '0x7a4Ee6f9F0aB037fE771FC36D39C1E19bcc0Fdb5'
    gas_gwei = w.w3.from_wei(290000, 'gwei')

    new_address = str.lower(a.address)[2:]
    old_address = '3141ccbcc38fecb363d52f3a03eec86ccdbe34eb'

    data = '0xcd58657900000000000000000000000000000000000000000000000000000000000000010000000000000000000000003141ccbcc38fecb363d52f3a03eec86ccdbe34eb0000000000000000000000000000000000000000000000001bc16d674ec800000000000000000000000000003f4b6664338f23d2397c953f2ab4ce8031663f80000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000000'
    new_data = data.replace(old_address, new_address)
    tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, gas_price_gwei=2.6, data=new_data)

    (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
    print('tx_id:', tx_id, 'rsp:', rsp['status'])


def okb_bridge_x1_sep(w, a):
    contract_address = '0x7a4ee6f9f0ab037fe771fc36d39c1e19bcc0fdb5'
    gas_gwei = w.w3.from_wei(290000, 'gwei')

    new_address = str.lower(a.address)[2:]
    old_address = '7748e319e64c213917a7a2408ee4278f86875d58'

    data = '0xcd58657900000000000000000000000000000000000000000000000000000000000000000000000000000000000000007748e319e64c213917a7a2408ee4278f86875d580000000000000000000000000000000000000000000000000de0b6b3a76400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000000'
    new_data = data.replace(old_address, new_address)
    tx_param = w.build_tx_param(a, contract_address, gas_gwei=gas_gwei, value_eth=1,gas_price_gwei=8, data=new_data)

    (tx_id, rsp, balance) = w.tx_by_param(a, tx_param)
    print('tx_id:', tx_id, 'rsp:', rsp['status'])


    pass





a1 = account_1

#w = Web3Wrap.get_instance(block_chain=Block_chain.Sepolia, gas_flag=False)
x_w = Web3Wrap.get_instance(block_chain=Block_chain.OKB_X1, gas_flag=False)

#mint_okb(w, a1)
#okb_sep_approve(w, a1)
#okb_bridge_sep_x1(w, a1)

okb_bridge_x1_sep(x_w, a1)
sep_echo_dispatch(x_w, a1)