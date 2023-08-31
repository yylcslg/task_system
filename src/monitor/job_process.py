from concurrent.futures import ThreadPoolExecutor

from src.monitor.job_queue import jobQueue
from src.service.template_service import templateService
from src.utils.Properties import pro
from src.utils.threads.job_thread_pool import job_process_thread


class JobProcess:

    def process(self):
        while True:
            try:
                j = jobQueue.queue.get()
                job_process_thread.submit(self.multi_process, j)
                #time.sleep(1)
            except Exception as e:
                print('error:', e)
                #log_error.msg_error('error', e)


    def multi_process(self, job):
        parallelism_num = job['parallelism_num']
        template_name = job['template_name']

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
                for account_exp in template_accounts_exp:
                    executor.submit(JobProcess.single_process, job, template_dict, account_exp)
        else:
            for account_exp in template_accounts_exp:
                JobProcess.single_process(job, template_dict, account_exp)

        print('new process job:', job)
        pass

    @staticmethod
    def single_process(job, template_dict, account_exp):
        print(account_exp)
        pass



jobProcess = JobProcess()
