import random
from concurrent.futures import ThreadPoolExecutor

from src.service.proxy_service import Proxy_type, proxyService
from src.task_core.task_core import TaskCore
from src.utils.date_utils import DateUtils


class TaskCoreLocal:

    @staticmethod
    def local_run(template_txt,accounts_exp_1,accounts_exp_2='', parallelism_num =1,
                  proxy_ip_type=Proxy_type.LOCAL_PROXY.value, param_exp=''):
        try:
            taskCore = TaskCore()
            template_dict = {}

            proxy_ip_list = proxyService.query_by_type(proxy_type=proxy_ip_type)
            template_accounts_exp = accounts_exp_1.split(';')

            template_dict['accounts_exp_2'] = accounts_exp_2
            account_2 = taskCore.query_accounts_exp_2(template_dict)


            num = 0
            for account_exp in template_accounts_exp:
                job_dict = {}

                job_dict['instance_id'] = 'job_' + 'local' + '_' + DateUtils.date_str(format='%Y%m%d%H%M%S') + '_' + str(num)
                num = num + 1
                t = taskCore.query_accounts_exp_1(account_exp)
                account_1_lst = t[0]
                account_tuple = t[1]
                job_dict['batch_name'] = account_tuple[0]
                job_dict['batch_from'] = account_tuple[3]
                job_dict['account_total'] = len(account_1_lst)

                TaskCoreLocal.local_single(template_txt, account_1_lst, account_2, parallelism_num = parallelism_num,
                                           proxy_ip_list=proxy_ip_list, param_exp=param_exp, job_dict=job_dict)

        except Exception as e:
            print('local_run error...', e)


    def local_single(template_txt,accounts_1_lst,accounts_2, proxy_ip_list, parallelism_num =1,param_exp='', job_dict={}):
        print(job_dict)
        try:
            if parallelism_num > 1:
                with ThreadPoolExecutor(max_workers=parallelism_num) as executor:
                    num = 0
                    for a in accounts_1_lst:
                        proxy_ip = random.choice(proxy_ip_list)
                        executor.submit(TaskCore.run_single,
                                        template_txt,
                                        exe_num=num,
                                        account_1=a,
                                        account_2=accounts_2,
                                        proxy_ip=proxy_ip,
                                        param_exp=param_exp,
                                        job_dict=job_dict)
                        num = num + 1
            else:
                num = 0
                for a in accounts_1_lst:
                    proxy_ip = random.choice(proxy_ip_list)
                    TaskCore.run_single(template_txt,
                                        exe_num=num,
                                        account_1=a,
                                        account_2=accounts_2,
                                        proxy_ip=proxy_ip,
                                        param_exp=param_exp,
                                        job_dict=job_dict)
                    num = num + 1

        except Exception as e:
            print('local_single error...', e)
