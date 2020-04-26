import requests,response

def getHttpTextInfo(url):
    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
        r.raise_for_statuscd 
        print(r.status_code)
        
       
        return r.json()
    except requests.exceptions.HTTPError as identifier:
        return identifier.errno
    

if __name__ == "__main__":
    #url = 'https://2.baidu.com/'
    #url = 'https://api.github.com/events' 
    url = 'http://httpbin.org/status/404'
    print(getHttpTextInfo(url)) 
