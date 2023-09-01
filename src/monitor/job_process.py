from concurrent.futures import ThreadPoolExecutor

from src.monitor.job_queue import jobQueue
from src.service.template_service import templateService
from src.task_core.task_core import TaskCore
from src.utils.Properties import pro
from src.utils.date_utils import DateUtils
from src.utils.threads.job_thread_pool import job_process_thread


class JobProcess:
    job_instance_dict = {}

    def process(self):
        while True:
            try:
                j = jobQueue.queue.get()
                job_process_thread.submit(self.multi_process, j)
            except Exception as e:
                print('error:', e)
                #log_error.msg_error('error', e)


    def multi_process(self, job):
        parallelism_num = job['parallelism_num']
        template_name = job['template_name']

        job['pre_instance_id'] = 'job_' + str(job['id']) + '_' + DateUtils.date_str(format='%Y%m%d%H%M%S')

        rs = templateService.query_template_by_name(template_name)
        if len(rs) == 0:
            print('template_name:',template_name, ' no record.......')
            return

        template_dict = rs[0]
        template_accounts_exp = template_dict['accounts_exp_1'].split(';')
        account_batch_size = len(template_accounts_exp)
        max_thread_worker = int(pro.get('max_thread_worker'))
        if parallelism_num > 1 and  account_batch_size > 1:
            worker_num = parallelism_num
            if parallelism_num > max_thread_worker:
                worker_num = max_thread_worker

            with ThreadPoolExecutor(max_workers = worker_num) as executor:
                num = 0
                for account_exp in template_accounts_exp:
                    job['instance_id'] = job['pre_instance_id'] + '_' + num
                    num = num + 1
                    executor.submit(JobProcess.single_process, job, template_dict, account_exp, 'multi_thread')
        else:
            num = 0
            for account_exp in template_accounts_exp:
                job['instance_id'] = job['pre_instance_id'] + '_' + num
                num = num + 1
                JobProcess.single_process(job, template_dict, account_exp, 'local')

    @staticmethod
    def single_process(job_dict, template_dict, account_exp, desc):
        print('['+desc+']', account_exp)
        taskCore = TaskCore(job_dict, template_dict, account_exp)
        taskCore.run
        JobProcess.job_instance_dict[job_dict['instance_id']] = taskCore


    def stop_job_instance(self, instance_id):
        if instance_id in JobProcess.job_instance_dict:
            taskCore = JobProcess.job_instance_dict[instance_id]
            taskCore.stop()
            del JobProcess.job_instance_dict[instance_id]

jobProcess = JobProcess()
