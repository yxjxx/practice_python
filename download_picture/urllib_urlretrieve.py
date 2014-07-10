#coding:utf-8

import urllib
from urlparse import urlsplit

def download_image(image_url):
    suffix_list = ['jpg','gif','png','tif','svg']
    # print urlsplit(image_url)
    filename = urlsplit(image_url)[2].split('/')[-1]
    file_suffix = filename.split('.')[1]
    if file_suffix in suffix_list :
        urllib.urlretrieve(image_url,filename)

def main():
    image_url = 'http://imglf2.ph.126.net/kuo9fZNo19Rfc1eUCJ8FkA==/1438055656114889126.jpg'
    download_image(image_url)

if __name__ == '__main__':
    main()
