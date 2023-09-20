import json
import os

import requests

from src.utils.date_utils import DateUtils

from src.utils.tools import URL_ENCODE, msg_encode

root_path = '/home/yinyunlong/output/'


def query_total_page(word, page_num, gsm = '1e'):
    query_word = msg_encode(word, URL_ENCODE)
    ts = str(DateUtils.get_timestamp()) + '='

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
    }
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8882515950466578368&ipn=rj&ct=201326592&is=&fp=result&fr=&word=' \
          + query_word + '&queryWord=' + query_word \
          + '&cl=2&lm=&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=' \
          + str(page_num * 30) + '&rn=30&gsm='+gsm+'&' + ts

    r = requests.request(method='get', url=url, headers=headers)
    j = json.loads(r.text.replace("\'","\""))

    displayNum = j['displayNum']

    return displayNum / 30



def query_image_baidu(word, page_num, gsm = '1e'):
    query_word = msg_encode(word, URL_ENCODE)
    ts = str(DateUtils.get_timestamp()) + '='

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
    }
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8882515950466578368&ipn=rj&ct=201326592&is=&fp=result&fr=&word=' \
          + query_word + '&queryWord=' + query_word \
          + '&cl=2&lm=&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=' \
          + str(page_num * 30) + '&rn=30&gsm='+gsm+'&' + ts

    rsp = requests.request(method='get', url=url, headers=headers)
    lst = parse_rsp_baidu(rsp.text, word)

    return lst

def parse_rsp_baidu(msg, word):
    #print(msg)
    titles = []
    title_array = msg.split('fromPageTitle":"')
    for s in title_array:
        if s.find('fromPageTitleEnc') > 0:
            temp_array = s.split('",')
            title = temp_array[0].replace('"','').replace(',','').strip()
            titles.append(title)
    #print('title size:', len(titles))
    urls = []
    url_array = msg.split('thumbURL":"')
    for s in url_array:
        if s.find('middleURL') > 0:
            temp_array = s.split('",')
            url = temp_array[0].replace('"', '').strip()
            urls.append(url)
    lst = []
    num = 0
    for t in titles:
        lst.append((t, urls[num], word))
        num = num + 1

    return lst


def save_pic(t, page_num, num, default_name = 'baidu'):
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




def baidu():
    #keys = ['大坝', '混凝土坝', '土石坝', '土坝', '重力坝', '拱坝', '水闸','船闸', '溢洪道', '渡槽', '渠道']
    keys = ['水利工程', '水利枢纽', '水工建筑物', '大坝', '混凝土坝', '土石坝', '土坝', '重力坝', '拱坝', '水闸','船闸', '溢洪道', '渡槽', '渠道']
    for k in keys:
        page_total = int(query_total_page(k, 0)) + 1
        print('key:',k,'page_total:', page_total)
        for i in range(page_total):
            lst = query_image_baidu(k, i)
            print('key:',k,'page num:', i, ' lst size:', len(lst))
            if len(lst) > 0:
                num = 0
                for t in lst:
                    save_pic(t, i, num)
                    #print(t)
                    num = num + 1
            else:
                break
                #time.sleep(1)




baidu()
#query_image_baidu('大坝', 0)

#u = 'https://img1.baidu.com/it/u=2655630315,2983712301&fm=253&fmt=auto&app=138&f=JPEG?w=640&h=358'

#img_type = u.split('f=')[1].split('?w')[0].lower()
#print(img_type)

