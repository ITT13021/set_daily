# coding:gbk
import os
import urllib
import time
import datetime
import pytesseract
from PIL import Image
import requests


def get_validate():
    val_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "23"
    validate_url = "xxxx={}".format(val_time)

    # ������֤��ͼƬ
    img_data = urllib.urlopen(validate_url).read()
    path = 'Login.jpg'
    with open(path, 'wb') as f:
        f.write(img_data)

    # ������֤��
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
    image = Image.open('F:\\python\\validate\\Login.jpg')
    code = pytesseract.image_to_string(image)
    postData.update({'txtValidate': code})


def set_daily():
    # ��ȡ��֤����Ϣ
    get_validate()

    # ��¼
    session = requests.session()
    login_res = session.post(login_url, data=postData, headers=headers)

    for i in xrange(20):
        if not login_res.history:
            if i == 19:
                print "д���ձ�ʧ�ܣ�"
                os._exit(0)
            set_daily()
        else:
            break

    # �ύ�ձ�
    daily_time = datetime.date(*map(int, datetime.datetime.now().strftime("%Y-%m-%d").split('-')))
    daily_data = {"xxxx"}

    daily_res = session.post(daily_url, data=daily_data, headers=headers)
    print daily_res


if __name__ == '__main__':
    postData = {"xxxx"}

    login_url = "http://xxxxx"
    daily_url = 'http://xxxxx'

    headers = {
        'Origin': 'xxxxxx',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    txtReport = raw_input("��������Ҫ��д���ձ����ݣ� ")
    set_daily()
