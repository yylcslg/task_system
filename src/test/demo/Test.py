from src.task_core.tools.http_tools import HttpTools
from src.utils.date_utils import DateUtils

def test(num_ps = 3, num_worker=1, task_type='ps',task_index=2):
    ps_ports = [i for i in range(2220, 2220 + num_ps)]
    worker_ports = [i for i in range(2320, 2320 + num_worker)]

    host = "127.0.0.1"
    cluster = {"cluster": {"ps": [host + ":" + str(p) for p in ps_ports],
                           "worker": [host + ":" + str(p) for p in
                                      worker_ports]},
               "task": {"type": str(task_type), "index": str(task_index)}}
    print(cluster)
    s = [host + ":" + str(p) for p in ps_ports]
    print(s)



if __name__ == "__main__":
    test()