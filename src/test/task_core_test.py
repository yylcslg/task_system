from src.service.code_service import codeService
from src.service.proxy_service import Proxy_type
from src.task_core.task_core import TaskCore
from src.utils.tools import msg_encode, msg_decode

p = '/home/yinyunlong/person/python_workspace/task_system/src/test/'


def run_spider(file_name, urls = None, proxy_ips={}, params = None):
    with open(p + file_name) as f:
        TaskCore(msg_encode(f.read())).setup()


def save_file_to_code(file_name, urls = None, proxy_ips={}, params = None):
    with open(p + file_name) as f:
        code_name = 'bnb_balance_echo'
        code_txt = msg_encode(f.read())
        accounts_exp_1 = 'batch_name_1[0:5];batch_name_2[3:6]'
        accounts_exp_2 = ''
        proxy_ip_exp = Proxy_type.LOCAL_PROXY.value
        param_exp = ''
        code_desc = ''

        #codeService.create_code(code_name, exec_txt, accounts_exp_1,accounts_exp_2,proxy_ip_exp, param_exp, code_desc)
        msg_dict = {}
        msg_dict['id'] = 2
        msg_dict['code_name'] = code_name
        msg_dict['code_txt'] = code_txt

        codeService.modify_code(msg_dict)
        rs = codeService.query_code_by_name(code_name)

        for l in rs :
            print(msg_decode(l['code_txt']))


    pass



if __name__ == "__main__":
    save_file_to_code("bnb_balance_echo.py")
    print("finish...................")
