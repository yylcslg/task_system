import json
import os
import time

from lxml import etree
import requests


root_path = '/home/yinyunlong/output/'



def parse_word(word, split_char='+'):
    array = word.split(' ')

    columns_str = split_char.join([x.strip() for x in array])
    return  columns_str




def save_pic(img_dic, name, default_name = 'bing'):
    full_path = root_path + default_name + '/' + parse_word(name, '_')
    isExists = os.path.exists(full_path)

    if not isExists:
        os.makedirs(full_path)
        print(full_path, 'create success......')

    num = 0
    for t in img_dic.values():
        print(t[0])

        # file_name = 'img_' + str(num)
        #
        # with open(full_path + '/' + file_name + '.text', 'w+') as f:
        #     f.write(t[1] + '\n')
        #     f.write(t[0])
        #     f.close()
        # num = num + 1
        #
        # if t[0].find('?') >0:
        #     array = t[0].split('?')[0].split('.')
        # else:
        #     array = t[0].split('.')
        # img_type = array[len(array) - 1].lower()
        #
        # r = requests.request(method='get', url=t[0], stream=True)
        # open(full_path + '/' + file_name + '.' + img_type, 'wb').write(r.content)

def query_image_bing(word, first, sfx):
    query_word = parse_word(word)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
    }

    url = 'https://cn.bing.com/images/async?q='+ query_word \
           + '&first='+str(first)+'&count=35&cw=1853&ch=426&relp=30&apc=0' \
           + '&datsrc=I&layout=RowBased_Landscape&mmasync=1'\
           + '&dgState=x*1661_y*574_h*180_c*6_i*62_r*9&IG=75280AACDFE34417A21983A0BF7BDABA'\
           + '&SFX='+str(sfx)+'&iid=images.5550'

    rsp = requests.request(method='get', url=url, headers=headers)
    h = etree.HTML(rsp.text)
    lst = h.xpath('//ul/li/div/div/a[@class="iusc"]')

    link_lst = []
    for l in lst:
        #print(l.attrib.get('m'))
        j = json.loads(l.attrib.get('m'))
        #print(j['murl'], j['t'],' desc:', j['desc'])
        pic_url = j['murl'].lower()
        if pic_url.find('.jpg') >0 or pic_url.find('.jpeg')>0 or pic_url.find('.png')>0 or pic_url.find('.gif') or pic_url.find('.webp'):
            link_lst.append((j['murl'], j['t'], j['desc']))
    count = len(lst)

    return (count, link_lst)

def bing():
    keys = ['hydraulic engineering', 'hydraulic junction', 'hydraulic structure','dam', 'concrete dam', 'earth and rock dam', 'earth dam', 'gravity dam', 'arch dam', 'sluice', 'ship lock','spillway', 'aqueduct', 'channe']
    for k in keys:
        count_num = 500
        first = 0
        sfx = 0
        img_dic = {}
        while first< count_num:
            t = query_image_bing(k,first, sfx)

            print('first:', first, 'count:',t[0])
            time.sleep(1)
            first = first + t[0] +1
            sfx = sfx + 1
            for tuple in t[1]:
                img_dic[tuple[0]] = tuple

            #break
        print(len(img_dic))
        save_pic(img_dic, k)
        break



bing()