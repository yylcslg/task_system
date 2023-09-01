import base64
import hashlib
import math
import urllib
import pybyte as pybyte

MD5 = 'md5'
UTF_8 = 'utf-8'
BASE_64 = 'base64'
URL_ENCODE = 'url_encode'

def msg_encode(msg, type = BASE_64):
    encode_Str = msg
    if type == BASE_64:
        encode_Str = base64.b64encode(bytes(msg,UTF_8)).decode(UTF_8)
    elif type == MD5:
        hl = hashlib.md5()
        hl.update(msg.encode(encoding=UTF_8))
        encode_Str = hl.hexdigest()
    elif type == URL_ENCODE:
        encode_Str = urllib.request.quote(msg, safe='/:?=&', encoding='utf-8')
    return encode_Str


def msg_decode(msg, type =BASE_64):
    decode_Str = msg
    if type == BASE_64:
        decode_Str = base64.b64decode(bytes(msg,UTF_8)).decode(UTF_8)
    elif type == URL_ENCODE:
        decode_Str = urllib.request.unquote(msg)

    return decode_Str




def gb_human_read(size, dot=2):
    if 1 <= size < 1024:
        human_size = str(round(size , dot)) + 'MB'
    elif math.pow(1024, 1) <= size < math.pow(1024, 2):
        human_size = str(round(size / math.pow(1024, 1), dot)) + 'GB'
    elif math.pow(1024, 2) <= size < math.pow(1024, 3):
        human_size = str(round(size / math.pow(1024, 2), dot)) + 'TB'
    else:
        raise ValueError('{}() takes number than or equal to 0, but less than 0 given.'.format(pybyte.__name__))
    return human_size

def byte_human_read(size, dot=2):
    size = float(size)
    # 位 比特 bit
    if 0 <= size < 1:
        human_size = str(round(size / 0.125, dot)) + 'b'
    # 字节 字节 Byte
    elif 1 <= size < 1024:
        human_size = str(round(size, dot)) + 'B'
    # 千字节 千字节 Kilo Byte
    elif math.pow(1024, 1) <= size < math.pow(1024, 2):
        human_size = str(round(size / math.pow(1024, 1), dot)) + 'KB'
    # 兆字节 兆 Mega Byte
    elif math.pow(1024, 2) <= size < math.pow(1024, 3):
        human_size = str(round(size / math.pow(1024, 2), dot)) + 'MB'
    # 吉字节 吉 Giga Byte
    elif math.pow(1024, 3) <= size < math.pow(1024, 4):
        human_size = str(round(size / math.pow(1024, 3), dot)) + 'GB'
    # 太字节 太 Tera Byte
    elif math.pow(1024, 4) <= size < math.pow(1024, 5):
        human_size = str(round(size / math.pow(1024, 4), dot)) + 'TB'
    # 拍字节 拍 Peta Byte
    elif math.pow(1024, 5) <= size < math.pow(1024, 6):
        human_size = str(round(size / math.pow(1024, 5), dot)) + 'PB'
    # 艾字节 艾 Exa Byte
    elif math.pow(1024, 6) <= size < math.pow(1024, 7):
        human_size = str(round(size / math.pow(1024, 6), dot)) + 'EB'
    # 泽它字节 泽 Zetta Byte
    elif math.pow(1024, 7) <= size < math.pow(1024, 8):
        human_size = str(round(size / math.pow(1024, 7), dot)) + 'ZB'
    # 尧它字节 尧 Yotta Byte
    elif math.pow(1024, 8) <= size < math.pow(1024, 9):
        human_size = str(round(size / math.pow(1024, 8), dot)) + 'YB'
    # 千亿亿亿字节 Bront Byte
    elif math.pow(1024, 9) <= size < math.pow(1024, 10):
        human_size = str(round(size / math.pow(1024, 9), dot)) + 'BB'
    # 百万亿亿亿字节 Dogga Byte
    elif math.pow(1024, 10) <= size < math.pow(1024, 11):
        human_size = str(round(size / math.pow(1024, 10), dot)) + 'NB'
    # 十亿亿亿亿字节 Dogga Byte
    elif math.pow(1024, 11) <= size < math.pow(1024, 12):
        human_size = str(round(size / math.pow(1024, 11), dot)) + 'DB'
    # 万亿亿亿亿字节 Corydon Byte
    elif math.pow(1024, 12) <= size:
        human_size = str(round(size / math.pow(1024, 12), dot)) + 'CB'
    # 负数
    else:
        raise ValueError('{}() takes number than or equal to 0, but less than 0 given.'.format(pybyte.__name__))
    return human_size




def parse_exp(account_exp):
    start_offset = 0
    end_offset = 0
    batch_from = ''
    if account_exp.__contains__('['):
        array_1 = account_exp.split('[')

        batch_name = array_1[0].strip()
        batch_from = '[' + array_1[1]
        array_2 = array_1[1].replace(']' , '').split(':')
        start_str = array_2[0].strip()
        if start_str == '':
            start_offset = 0
        else:
            start_offset = int(start_str)

        end_str = array_2[1].strip()

        if end_str == '':
            end_offset = 0
        else:
            end_offset = int(end_str)
    else:
        batch_name = account_exp
    return (batch_name, start_offset, end_offset, batch_from)