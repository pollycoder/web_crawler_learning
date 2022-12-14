# This is a sample of learning web crawling
# Adapted from a construction on C-language Chinese Net
# URL: http://c.biancheng.net/python_spider/the-first-spider.html

# Part 1: Get HTML info of one page
from urllib import request
## Open the web
response = request.urlopen('http://httpbin.org/')
print(response)
## Get the HTML code of the web
html = response.read().decode()
print(html)

# Part 2: User Agent
## Get UA info
response1 = request.urlopen('http://httpbin.org/get')
html1 = response1.read().decode()
print(html1)
## Reconstruct request headers, pretending to be the browser
url = 'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0'
}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
html2 = res.read().decode('utf-8')
print(html2)
## Create a UA pool
from fake_useragent import UserAgent
ua_list = [
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0'
]
### Substantialize an object
ua = UserAgent()
print(ua.firefox)


