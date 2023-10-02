import os
import time
import json

import requests
from lxml import etree
from selenium import webdriver

from src.task_core.tools.http_tools import HttpTools

root_path = '/home/yinyunlong/output/'

def parse_word(word, split_char='+'):
    array = word.split(' ')

    columns_str = split_char.join([x.strip() for x in array])
    return  columns_str

def selenium_start(word):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-blink-features=AutomationControlled')

    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('detach', True)  # 不自动关闭浏览
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options,
                              executable_path="/home/yinyunlong/person/program/chromedriver/chromedriver")  # Chrome浏览器
    driver.maximize_window()
    # driver.implicitly_wait(30)
    url = 'https://cn.bing.com/images/search?q=' + word
    driver.get(url)
    for i in range(30):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        temp_h = etree.HTML(driver.page_source)
        temp_lst = temp_h.xpath('//ul/li/div/div/a[@class="iusc"]')
        print('execute num:', i, ' page size:', len(temp_lst))
        time.sleep(1)

    h = etree.HTML(driver.page_source)

    lst = h.xpath('//ul/li/div/div/a[@class="iusc"]')

    link_lst = []
    for l in lst:
        #print(l.attrib.get('m'))
        j = json.loads(l.attrib.get('m'))
        pic_url = j['murl'].lower()
        if pic_url.find('.jpg') > 0 or pic_url.find('.jpeg') > 0 or pic_url.find('.png') > 0 or pic_url.find(
                '.gif') or pic_url.find('.webp'):
            img_type = 'jpg'
            if pic_url.find('.jpg') > 0:
                img_type = 'jpg'
            elif pic_url.find('.jpeg') > 0:
                img_type = 'jpeg'
            elif pic_url.find('.png') > 0:
                img_type = 'png'
            elif pic_url.find('.gif') > 0:
                img_type = 'gif'
            elif pic_url.find('.webp') > 0:
                img_type = 'webp'

            link_lst.append(( j['t'],j['turl'],j['murl'], img_type))
        #link_lst.append((j['t'], j['turl'], j['murl'], 'jpg'))

    print('word  pic num :', len(lst))
    driver.close()
    return link_lst

def save_pic(lst, name, default_name = 'bing'):
    full_path = root_path + default_name + '/' + parse_word(name, '_')
    isExists = os.path.exists(full_path)

    if not isExists:
        os.makedirs(full_path)
        print(full_path, 'create success......')

    num = 0
    for t in lst:
        file_name = 'img_' + str(num)
        num = num + 1

        with open(full_path + '/' + file_name + '.text', 'w+') as f:
            f.write(t[0] + '\n')
            f.write(t[1] + '\n')
            f.write(t[2])

        for i in range(3):
            try:
                r = requests.request(method='get', url=t[1], stream=True)
                if r.status_code == 200:
                    with open(full_path + '/' + file_name + '.jpg', 'wb')  as f:
                        f.write(r.content)
                    break
                else:
                    print('file name :',file_name , ' status:',r.status_code)

            except Exception as e:
                print('error:', e)

        # for i in range(3):
        #     try:
        #         r = requests.request(method='get', url=t[2], stream=True, timeout = 60)
        #         if r.status_code == 200:
        #             with open(full_path + '/' + file_name + '_ori.' + t[3], 'wb') as f:
        #                 f.write(r.content)
        #             break
        #         else:
        #             print('ori file name :',file_name , ' status:',r.status_code)
        #     except Exception as e:
        #         print('error:', e)





def bing():
    keys = ['hydraulic engineering', 'hydraulic junction', 'hydraulic structure','dam', 'concrete dam', 'earth and rock dam', 'earth dam', 'gravity dam', 'arch dam', 'sluice', 'ship lock','spillway', 'aqueduct', 'channe']
    for word in keys:
        lst = selenium_start(word)
        save_pic(lst, word)

    print('finish....')


#bing()


def download():
    keys = ['hydraulic engineering', 'hydraulic junction', 'hydraulic structure', 'dam', 'concrete dam',
            'earth and rock dam', 'earth dam', 'gravity dam', 'arch dam', 'sluice', 'ship lock', 'spillway', 'aqueduct',
            'channe']
    for word in keys:
        dir_name = parse_word(word, '_')
        path = root_path + 'bing/' + dir_name
        files = os.listdir(path)
        for f in files:
            if f.find('.text') > 0:
                ori_img(dir_name, f, path)
        #break

def ori_img(dir_name, f, old_path, default_name = 'bing'):
    img_name = f.split('.')[0]

    full_path = root_path + default_name + '/' + dir_name
    isExists = os.path.exists(full_path)

    if not isExists:
        os.makedirs(full_path)
        print(full_path, 'create success......')
    #temp_lst = []
    with open(old_path + '/' + f) as f:
        temp_lst = f.readlines()
    pic_url = temp_lst[2]

    img_type = 'jpg'
    if pic_url.find('.jpg') > 0:
        img_type = 'jpg'
    elif pic_url.find('.jpeg') > 0:
        img_type = 'jpeg'
    elif pic_url.find('.png') > 0:
        img_type = 'png'
    elif pic_url.find('.gif') > 0:
        img_type = 'gif'
    elif pic_url.find('.webp') > 0:
        img_type = 'webp'
    print('dir_name:',dir_name,'file_name:', img_name, ' url :',pic_url)
    for i in range(3):
        try:
            r = requests.request(method='get', url = pic_url, stream=True, timeout = 10)
            #session = requests.Session()
            #session.proxies = HttpTools.build_proxy('127.0.0.1:8889')
            if r.status_code == 200:
                with open(full_path + '/' + img_name + '_ori.' + img_type, 'wb') as f:
                    f.write(r.content)
                break
            else:
                time.sleep(1)
                print('ori file name :',img_name , ' status:',r.status_code)
        except Exception as e:
            print('error:', e)


download()