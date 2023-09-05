import time


from src.monitor.job_process import JobProcess, jobProcess
from src.monitor.job_queue import jobQueue
from src.service.job_service import JobService
from src.utils import tools
from src.utils.date_utils import DateUtils
from src.utils.threads.job_thread_pool import job_monitor_thread



class JobMonitor:
    job = JobService()
    jobProcess = JobProcess()


    def monitor_job(self):
        exe_num = 0
        while(True):
            try:
                ts = DateUtils.get_timestamp_min()
                rs = self.job.query_job(ts)
                filter_rs = self.filter_enable_job(rs)
                exe_num = exe_num + 1
                if len(filter_rs) > 0:
                    for j in filter_rs:
                        self.job.modify_job_exe_time(j, ts)
                        jobQueue.queue.put(j)
                        print('put after size:', jobQueue.queue.qsize())
                time.sleep(40)
            except Exception as e:
                print('monitor_job error:', e)

    def filter_enable_job(self, rs):
        lst = []
        for job in rs :
            if job['job_cycle'] == 0:  # 仅一次
                if tools.job_by_only(job) : lst.append(job)
            elif job['job_cycle'] == 1: #小时级别
                if tools.job_by_hour(job) : lst.append(job)
            elif job['job_cycle'] == 2: #天级别
                if tools.job_by_day(job) : lst.append(job)
            elif job['job_cycle'] == 3: #周级别
                if tools.job_by_week(job) : lst.append(job)
            elif job['job_cycle'] == 5:  # 测试级别， 启动就执行
                lst.append(job)
            else:
                pass
        return lst



if __name__ == '__main__':
    job_monitor_thread.submit(JobMonitor().monitor_job)
    job_monitor_thread.submit(jobProcess.process)
    job_monitor_thread.submit(jobProcess.job_instance_detail_log)
    print('finish......')

