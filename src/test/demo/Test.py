from src.task_core.tools.http_tools import HttpTools
from src.utils.date_utils import DateUtils

t = DateUtils.date_str(format='%Y%m%d_%H%M%S')
print(t)


print(HttpTools.get_host_ip())