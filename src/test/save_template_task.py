from src.service.proxy_service import Proxy_type
from src.service.template_service import templateService
from src.utils.tools import msg_encode, msg_decode

p = '/home/yinyunlong/person/python_workspace/task_system/src/test/'

def save_file_to_code(dir_name,file_name, template_name, accounts_exp_1,
                      accounts_exp_2='',
                      proxy_ip_exp = Proxy_type.LOCAL_PROXY.value,
                      param_exp='',
                      template_desc = ''):
    with open(p +dir_name+'/'+ file_name) as f:
        template_txt = msg_encode(f.read())
        templateService.create_template(template_name, template_txt, accounts_exp_1,accounts_exp_2,proxy_ip_exp, param_exp, template_desc)


def modify_template(dir_name, file_name, template_id =0, template_name = ''):
    with open(p +dir_name+'/'+ file_name) as f:
        msg_dict = {}
        msg_dict['id'] = template_id
        msg_dict['template_txt'] = msg_encode(f.read())
        if template_name != '':
            msg_dict['template_name'] = template_name

        templateService.modify_template(msg_dict)

def query_template(template_name):
    rs = templateService.query_template_by_name(template_name)
    for l in rs :
         print(msg_decode(l['template_txt']))


def mailzero_process():
    save_file_to_code(dir_name='bnb', file_name='mailzero.py', template_name='mailzero',
                      accounts_exp_1='tinc_wallet_1[:];tinc_wallet_2[:]',
                      accounts_exp_2='batch_name_1[0:1]')


if __name__ == "__main__":
    mailzero_process()

    print("finish...................")
