download images
=================

有些网站的图片限制了urlretrieve下载,但是可以用requests+io.open下载.比如:[小海严选](http://curator.im/)

***************************

urlretrieve 下载图片的方式

```
urllib.urlretrieve(image_url,filename)
```

**************************

requests 官网推荐的方式:


```
r = requests.get(image_url, stream=True)
if r.status_code == 200:
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
            f.flush()
        f.close()
```
