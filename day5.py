import requests
import re

url="https://movie.douban.com/top250"
head={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
resp=requests.get(url,headers=head)
page_content=resp.text
obj=re.compile(r"",re.S)

resp.close()