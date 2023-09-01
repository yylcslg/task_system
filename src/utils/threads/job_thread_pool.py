
from concurrent.futures import ThreadPoolExecutor

from src.utils.Properties import pro

job_monitor_thread = ThreadPoolExecutor(max_workers=4)
job_process_thread = ThreadPoolExecutor(max_workers= int(pro.get('max_job_thread')))




