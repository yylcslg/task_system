from src.task_core.task_core_local import TaskCoreLocal
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap
from src.test.bnb.defi_page import sign_in, claim, get_user, add_address
from src.test.save_template_task import p
from src.utils.tools import msg_encode
from src.utils.wallet_account import Wallet


def read_local_file(dir_name, file_name):
    with open(p +dir_name+'/'+ file_name) as f:
        template_txt = msg_encode(f.read())
    return template_txt




def run_ants(dir_name, file_name, range_num = 1):
    template_txt = read_local_file(dir_name, file_name)
    #accounts_exp_1 = 'test[:];tinc_wallet_1[:]'
    accounts_exp_1 = 'test[1:2]'
    accounts_exp_2 = 'test[1:2]'
    parallelism_num = 5
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag=False)

if __name__ == "__main__":
    run_ants('pol', 'ants.py')
    print("finish...................")
