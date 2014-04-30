#coding:utf-8
import requests
import io
from urlparse import urlsplit

def requests_image(image_url):
    suffix_list = ['jpg','gif','png','tif','svg']
    filename = urlsplit(image_url)[2].split('/')[-1]
    filename = 'C://' + filename
    file_suffix = filename.split('.')[1]
    r = requests.get(image_url)
    if file_suffix in suffix_list and r.status_code == requests.codes.ok:
        with io.open(filename,'wb') as file:
            file.write(r.content)
            file.flush()
            file.close()

def main():
    iamge_url = 'http://imglf0.ph.126.net/P-ZUcMfCEtje4c8K3ZlK4w==/1839720447881078946.jpg'
    requests_image(iamge_url)

if __name__ == '__main__':
    main()
