import requests
from urlparse import urlsplit

def download_image(image_url):
    suffix_list = ['jpg','gif','png','tif','svg']
    filename = urlsplit(image_url)[2].split('/')[-1]
    file_suffix = filename.split('.')[1]
    r = requests.get(image_url, stream=True)
    if file_suffix in suffix_list and r.status_code == requests.codes.ok:
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
                f.flush()
            f.close()


def main():
    image_url = 'http://t.curator.im/8-auz6dK50HR1ayhQVCVzK9zreI=/544x0/filters:watermark(http://curator.im/static/images/watermark.png,-0,-0,0)/media.curator.im/images/488741714536577/609895439087870_10153137_609895439087870_1292745580_n.jpg'
    download_image(image_url)

if __name__ == '__main__':
    main()