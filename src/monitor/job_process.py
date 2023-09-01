from src.monitor.job_queue import jobQueue
from src.service.template_service import templateService
from src.task_core.task_core import TaskCore
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
        template_name = job['template_name']
        rs = templateService.query_template_by_name(template_name)
        if len(rs) == 0:
            print('template_name:',template_name, ' no record.......')
            return

        template_dict = rs[0]
        template_accounts_exp = template_dict['accounts_exp_1'].split(';')

        num = 0
        for account_exp in template_accounts_exp:
            job['instance_id'] = 'job_' + str(job['id']) + '_' + DateUtils.date_str(format='%Y%m%d%H%M%S') + '_' + str(num)
            num = num + 1
            self.single_process(job, template_dict, account_exp)


    def single_process(self, job_dict, template_dict, account_exp):
        taskCore = TaskCore(job_dict, template_dict, account_exp)
        taskCore.run()
        JobProcess.job_instance_dict[job_dict['instance_id']] = taskCore


    def stop_job_instance(self, instance_id):
        if instance_id in JobProcess.job_instance_dict:
            taskCore = JobProcess.job_instance_dict[instance_id]
            taskCore.stop()
            del JobProcess.job_instance_dict[instance_id]



jobProcess = JobProcess()
