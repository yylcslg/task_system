import random
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
        jobService.save_job_instance(t,self.job_dict)
        print('job_dict:', self.job_dict)

        parallelism_num = self.job_dict['parallelism_num']
        max_thread_worker = int(pro.get('max_thread_worker'))
        if parallelism_num > 1 :
            worker_num = parallelism_num
            if parallelism_num > max_thread_worker:
                worker_num = max_thread_worker

            with ThreadPoolExecutor(max_workers = worker_num) as executor:
                for a in account_1_lst :
                    if self.run_flag:
                        proxy_ip = random.choice(proxy_ip_list)
                        executor.submit(TaskCore.run_single,
                                        self.template_dict['template_txt'],
                                        account_1 = a.address,
                                        account_2 = account_2,
                                        proxy_ip = proxy_ip,
                                        param_exp = self.template_dict['param_exp'],
                                        job_dict = self.job_dict)
        else:
            for a in account_1_lst:
                if self.run_flag:
                    proxy_ip = random.choice(proxy_ip_list)
                    TaskCore.run_single(self.template_dict['template_txt'],
                                    account_1=a,
                                    account_2=account_2,
                                    proxy_ip=proxy_ip,
                                    param_exp=self.template_dict['param_exp'],
                                    job_dict=self.job_dict)




    def query_accounts_exp_1(self, account_exp):
        if account_exp.strip().isspace():
            return []

        tuple = tools.parse_exp(account_exp.strip())
        return (walletService.query_wallet_by_param(tuple[0], tuple[1], tuple[2]), tuple)




    def query_accounts_exp_2(self, template_dict):
        try:
            template_accounts_exp = template_dict['accounts_exp_1'].split(';')
            rs = self.query_accounts_exp_1(template_accounts_exp[0])
            if len(rs)>0:
                return rs[0]

        except Exception as e:
            print('error:', e)
        return None


    # 静态方法，方便后期 单个wallet 执行
    #
    #
    @staticmethod
    def run_single(template_txt, account_1, proxy_ip='', account_2=None, param_exp='', job_dict={}):
        if proxy_ip == '':
            proxy_ip = pro.get('local_default_proxy_ip')
        exec_param = {'account_1': account_1,
                      'proxy_ip' : proxy_ip,
                      'account_2' : account_2,
                      'param_exp' : param_exp,
                      'job_dict' : job_dict}
        print('exe ',exec_param)
        #exec(msg_decode(template_txt), exec_param)



    @staticmethod
    def local_run(template_txt):
        try:
            params = ''
            exec(msg_decode(template_txt), {"params": params})
        except Exception as e:
            print('error...', e)

    def stop(self):
        self.run_state = False
        print("stop...")


#print(TaskCore.parse_exp('batch_name_1[ 3: ]'))