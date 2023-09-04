from src.monitor.job_log import JobLog
from src.task_core.tools.block_chain import Block_chain
from src.task_core.tools.web3_wrap import Web3Wrap

a1 = account_1
a2 = account_2
param = param_exp
job = job_dict
proxy_ip_str = proxy_ip

w = Web3Wrap(block_chain=Block_chain.BSC_ANKR, proxy_ip=proxy_ip_str, gas_flag=False)
amount = float(w.get_balance(a1.address, unit='ether'))
#if amount< 0.0014:

print('address 1:', a1.address, 'balance:', amount)
print('address 2:', a2.address, 'balance:', amount)

JobLog.job_log(job, {}, local_flag = False)


