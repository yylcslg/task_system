from src.task_core.task_core_local import TaskCoreLocal
from src.test.save_template_task import p
from src.utils.tools import msg_encode


def read_local_file(dir_name, file_name):
    with open(p +dir_name+'/'+ file_name) as f:
        template_txt = msg_encode(f.read())
    return template_txt


def run_mailzero(dir_name, file_name):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[0:1];tinc_wallet_1[:];tinc_wallet_2[:];tinc_wallet_3[:]'
    #accounts_exp_1 = 'test[0:1]'
    accounts_exp_2 = ''
    parallelism_num = 10
    TaskCoreLocal.local_run(template_txt, accounts_exp_1= accounts_exp_1, accounts_exp_2 = accounts_exp_2,
                            parallelism_num = parallelism_num, db_flag= False)


def run_unemeta(dir_name, file_name):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[0:1];tinc_wallet_1[:];tinc_wallet_2[:];tinc_wallet_3[:];tinc_wallet_4[:]'
    #accounts_exp_1 = 'tinc_wallet_4[:]'
    accounts_exp_2 = ''
    parallelism_num = 10
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag= False)


def run_alienswap(dir_name, file_name):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[0:1];tinc_wallet_1[:];tinc_wallet_2[:];tinc_wallet_3[:]'
    #accounts_exp_1 = 'tinc_wallet_3[:]'
    accounts_exp_2 = ''
    parallelism_num = 3
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag= False)


def run_maizero_mint(dir_name, file_name):
    template_txt = read_local_file(dir_name, file_name)
    accounts_exp_1 = 'test[0:3]'
    #accounts_exp_1 = 'tinc_wallet_3[:]'
    accounts_exp_2 = ''
    parallelism_num = 1
    #print('', template_txt)
    TaskCoreLocal.local_run(template_txt, accounts_exp_1=accounts_exp_1, accounts_exp_2=accounts_exp_2,
                            parallelism_num=parallelism_num, db_flag= False)

if __name__ == "__main__":

    #run_unemeta('bnb', 'unemeta.py')
    #run_mailzero('bnb', 'mailzero.py')
    run_alienswap('linea', 'alienswap.py')

    for i in range(1):
        #run_maizero_mint('zks', 'maizero_mint.py')
        pass

    print("finish...................")