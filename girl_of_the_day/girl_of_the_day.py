#coding=utf-8
import requests
from io import open as iopen
from urlparse import urlsplit
import time
import shutil
import os

def requests_image(file_url):
    suffix_list = ['jpg', 'gif', 'png', 'tif', 'svg',]
    file_name =  urlsplit(file_url)[2].split('/')[-1]
    file_suffix = file_name.split('.')[1]
    i = requests.get(file_url)
    if file_suffix in suffix_list and i.status_code == requests.codes.ok:
        with iopen(file_name, 'wb') as file:
            file.write(i.content)
    else:
        return False

def move_pics(today):
    folder_name = today
    os.mkdir(folder_name)
    source = os.listdir('/home/yxj/Dropbox/Pics/girls/')
    destination = '/home/yxj/Dropbox/Pics/girls/' + folder_name + '/'
    for files in source:
        if files.endswith('.jpg'):
            shutil.move(files,destination)

def main():
    today = time.strftime('%Y-%m-%d')
    token = 'ddf08b6fede347238d43f78baa06b8df'

    r = requests.get('http://curator.im/api/girl_of_the_day/%s/?format=json&token=%s' %(today,token))

    for i in r.json():
        #print i.get('image')
        requests_image(i.get('image'))

    move_pics(today)
    print 'end'


if __name__ == '__main__':
    main()
