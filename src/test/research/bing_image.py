import json
import os

import requests

from src.utils.date_utils import DateUtils
from src.utils.tools import msg_encode, URL_ENCODE

root_path = '/home/yinyunlong/output/'



def query_image_bing(word, page_num, gsm = '1e'):
    query_word = msg_encode(word, URL_ENCODE)
    ts = str(DateUtils.get_timestamp()) + '='

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
    }
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8882515950466578368&ipn=rj&ct=201326592&is=&fp=result&fr=&word=' \
          + query_word + '&queryWord=' + query_word \
          + '&cl=2&lm=&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=' \
          + str(page_num * 30) + '&rn=30&gsm=' + gsm + '&' + ts

    rsp = requests.request(method='get', url=url, headers=headers)



def save_pic(t, page_num, num, default_name = 'bing'):
    full_path = root_path + default_name + '/' + t[2]
    isExists = os.path.exists(full_path)

    # 判断是否存在图片格式
    if t[1].find('f=') >0:
        # 判断结果
        if not isExists:
            os.makedirs(full_path)
            print(full_path, 'create success......')

        file_name = 'img_' + str(page_num) + '_' + str(num)
        with open(full_path + '/' + file_name +'.text', 'w+') as f:
            f.write(t[0] + '\n')
            f.write(t[1])
            f.close()
        #print(t[1])

        img_type = t[1].split('f=')[1].split('?w')[0].lower()

        r = requests.request(method='get', url =t[1], stream=True)
        open(full_path + '/' + file_name +'.'+img_type, 'wb').write(r.content)


