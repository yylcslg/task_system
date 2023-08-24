from src.task_core.task_core import TaskCore
from src.utils.tools import msg_encode

p = '/home/yinyunlong/person/python_workspace/task_system/src/test/'
def task_spider():
    with open(p + "task_core_test.py") as f:
        TaskCore(msg_encode(f.read())).setup()

def run_spider(file_name, urls = None, proxy_ips={}, params = None):
    with open(p + file_name) as f:
        TaskCore(msg_encode(f.read())).setup()


if __name__ == "__main__":
    run_spider("bnb_balance_echo.py")
    print("finish...................")
