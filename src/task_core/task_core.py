import random
import copy
from concurrent.futures import ThreadPoolExecutor

from src.service.job_service import jobService
from src.service.proxy_service import proxyService
from src.service.wallet_service import walletService
from src.utils import tools
from src.utils.Properties import pro
from src.utils.tools import msg_decode


class TaskCore:

    def __init__(self, job_dict={}, template_dict={}, account_exp=''):
        self.job_dict = job_dict
        self.template_dict = template_dict
        self.account_exp = account_exp
        self.run_flag = True
        if 'instance_id' in job_dict:
            self.instance_id = job_dict['instance_id']


    #1： 创建 job instance 记录， 解析 exp 规则
    #2：获取 account1 所有wallet
    #3：遍历wallet
    #4：记录 执行记录
    #5: 异常处理
    #5.1: 抛出异常3次，任务停止执行 ：每次交易都需要gas， 如果开启重试 ，会导致 亏损
    #5.2 交易 失败状态连续3 次 任务停止
    def run(self):
        proxy_ip_list = proxyService.query_by_type(proxy_type= self.template_dict['proxy_ip_exp'])
        t = self.query_accounts_exp_1(self.account_exp)
        account_2 = self.query_accounts_exp_2(self.template_dict)
        account_1_lst = t[0]
        account_tuple = t[1]
        self.job_dict['batch_name'] = account_tuple[0]
        self.job_dict['batch_from'] = account_tuple[3]
        self.job_dict['account_total'] = len(account_1_lst)
        jobService.save_job_instance(self.job_dict)

        parallelism_num = self.job_dict['parallelism_num']
        max_thread_worker = int(pro.get('max_thread_worker'))

        if parallelism_num > 1 :
            worker_num = parallelism_num
            if parallelism_num > max_thread_worker:
                worker_num = max_thread_worker
            print('worker_num', worker_num)
            with ThreadPoolExecutor(max_workers = worker_num) as executor:
                num = 0
                for a in account_1_lst :
                    if self.run_flag:
                        deep_job_dict = copy.deepcopy(self.job_dict)
                        proxy_ip = random.choice(proxy_ip_list)
                        executor.submit(TaskCore.run_single,
                                        self.template_dict['template_txt'],
                                        exe_num = num,
                                        account_1 = a,
                                        account_2 = account_2,
                                        proxy_ip = proxy_ip,
                                        param_exp = self.template_dict['param_exp'],
                                        job_dict = deep_job_dict)
                        num = num + 1
        else:
            num = 0
            for a in account_1_lst:
                if self.run_flag:
                    deep_job_dict = copy.deepcopy(self.job_dict)
                    proxy_ip = random.choice(proxy_ip_list)
                    TaskCore.run_single(self.template_dict['template_txt'],
                                    exe_num=num,
                                    account_1=a,
                                    account_2=account_2,
                                    proxy_ip=proxy_ip,
                                    param_exp=self.template_dict['param_exp'],
                                    job_dict=deep_job_dict)
                    num = num + 1




    def query_accounts_exp_1(self, account_exp):
        if account_exp.strip().isspace():
            return []

        t = tools.parse_exp(account_exp.strip())
        return (walletService.query_wallet_by_param(t[0], t[1], t[2]), t)




    def query_accounts_exp_2(self, template_dict):
        try:
            template_accounts_exp = template_dict['accounts_exp_2'].split(';')
            rs = self.query_accounts_exp_1(template_accounts_exp[0])[0]
            if len(rs)>0 and rs !='':
                return rs[0]

        except Exception as e:
            print('error:', e)
        return None


    # 静态方法，方便后期 单个wallet 执行
    #
    #
    @staticmethod
    def run_single(template_txt, exe_num, account_1,  account_2, proxy_ip='', param_exp='', job_dict={}):
        try:
            if proxy_ip == '':
                proxy_ip = pro.get('local_default_proxy_ip')
            exec_param = {'account_1': account_1,
                          'proxy_ip': proxy_ip,
                          'account_2': account_2,
                          'param_exp': param_exp,
                          'job_dict': job_dict}

            job_dict['wallet_address'] = account_1.address
            print('--[start]-----[', job_dict['batch_name'], '] [', exe_num, '] address:', account_1.address,' ------------------------')
            exec(msg_decode(template_txt), exec_param)
            print('--[finish]-----[', job_dict['batch_name'], '] [', exe_num, '] address:', account_1.address,' ------------------------')
        except Exception as e:
            print('run_single error：',e)




    def stop(self):
        self.run_state = False
        print(self.instance_id, " stop.........")


#print(TaskCore.parse_exp('batch_name_1[ 3: ]'))