from src.monitor.job_monitor import JobMonitor
from src.monitor.job_process import jobProcess
from src.utils.threads.job_thread_pool import job_monitor_thread

if __name__ == '__main__':
    job_monitor_thread.submit(JobMonitor().monitor_job)
    job_monitor_thread.submit(jobProcess.process)
    job_monitor_thread.submit(jobProcess.job_instance_detail_log)


    print('finish......')

#git config --global http.https://github.com.proxy http://127.0.0.1:8889
#git config --global https.https://github.com.proxy https://127.0.0.1:8889

#git config --global http.proxy 'socks5://127.0.0.1:8889'
#git config --global https.proxy 'socks5://127.0.0.1:8889'