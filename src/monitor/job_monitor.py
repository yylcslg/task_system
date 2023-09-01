import time

from src.monitor.job_process import JobProcess, jobProcess
from src.monitor.job_queue import jobQueue
from src.service.job_service import JobService
from src.utils.date_utils import DateUtils
from src.utils.threads.job_thread_pool import job_monitor_thread


class JobMonitor:
    job = JobService()
    jobProcess = JobProcess()

    def monitor_job(self):
        while(True):
            try:
                ts = DateUtils.get_timestamp_min()
                rs = self.job.query_job(ts + 11)
                filter_rs = self.filter_enable_job(rs)
                if len(filter_rs) > 0:
                    for j in filter_rs:

                        self.job.modify_job_exe_time(j, ts)
                        jobQueue.queue.put(j)
                        print('put after size:', jobQueue.queue.qsize())
                time.sleep(40)
            except Exception as e:
                print('error:', e)



    def filter_enable_job(self, rs):

        return rs


if __name__ == '__main__':
    job_monitor_thread.submit(JobMonitor().monitor_job)
    job_monitor_thread.submit(jobProcess.process)
    print('finish......')

