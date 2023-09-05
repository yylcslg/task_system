from src.service.proxy_service import Proxy_type
from src.service.template_service import templateService
from src.task_core.task_core import TaskCore
from src.utils.tools import msg_encode, msg_decode

p = '/home/yinyunlong/person/python_workspace/task_system/src/test/'


def run_spider(file_name, urls = None, proxy_ips={}, params = None):
    with open(p + file_name) as f:
        TaskCore.local_run(msg_encode(f.read()))


def save_file_to_code(file_name, urls = None, proxy_ips={}, params = None):
    with open(p + file_name) as f:
        template_name = 'mailzero'
        template_txt = msg_encode(f.read())
        accounts_exp_1 = 'tinc_wallet_2[:]'
        accounts_exp_2 = ''
        proxy_ip_exp = Proxy_type.LOCAL_PROXY.value
        param_exp = ''
        template_desc = ''

        #templateService.create_template(template_name, template_txt, accounts_exp_1,accounts_exp_2,proxy_ip_exp, param_exp, template_desc)
        msg_dict = {}
        msg_dict['id'] = 8
        #msg_dict['template_name'] = template_name
        msg_dict['template_txt'] = template_txt

        templateService.modify_template(msg_dict)
        # rs = templateService.query_template_by_name(template_name)
        #
        # for l in rs :
        #     print(msg_decode(l['template_txt']))


    pass



if __name__ == "__main__":
    save_file_to_code("mailzero.py")

    #run_spider('bnb_balance_echo.py')
    print("finish...................")
