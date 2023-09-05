from datetime import timedelta
from timeloop import Timeloop
from src.monitor.job_queue import jobQueue, logQueue
from src.service.job_service import jobService
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
                print('JobProcess error:', e)
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
        JobProcess.job_instance_dict[job_dict['instance_id']] = taskCore
        taskCore.run()



    def stop_job_instance(instance_id):
        if instance_id in JobProcess.job_instance_dict:
            taskCore = JobProcess.job_instance_dict[instance_id]
            taskCore.stop()
            del JobProcess.job_instance_dict[instance_id]
            print('instance_id:', instance_id, ' remove.....')

    def job_instance_detail_log(self):
        lst =[]
        start_time = DateUtils.get_timestamp()
        while True:
            try:
                current_time = DateUtils.get_timestamp()
                if current_time - start_time >=10000: # 超过10s
                    if len(lst)==0:
                        start_time = DateUtils.get_timestamp()
                    else:
                        start_time = DateUtils.get_timestamp()
                        jobService.save_job_instance_detail(lst)
                        lst = []

                if len(lst) >= 100:
                    start_time = DateUtils.get_timestamp()
                    jobService.save_job_instance_detail(lst)
                    lst = []

                j = logQueue.queue.get(timeout = 3) # 无数据等待3秒
                if 'instance_id' in j and len(j['instance_id']) > 0 :
                    lst.append(j)

            except Exception as e:
                pass
                #print('warn: job_instance_detail_log logQueue is empty', e)

tl = Timeloop()


#超过48小时的任务，自动删除
@tl.job(interval=timedelta(seconds=3600))
def clear_job_instance():
    date_str = int(DateUtils.date_str(day_num=2, format='%Y%m%d%H%M%S'))

    for k in JobProcess.job_instance_dict:
        array = k.split('_')
        if int(array[2]) > date_str:
            JobProcess.stop_job_instance(k)
            print('instance_id:', k, ' more then two day, stop task.......')


tl.start()
jobProcess = JobProcess()
