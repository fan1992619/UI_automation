import json
import requests
def send_request(url):
    pass
    # r = requests.get(url).json()
    # return r
def visit_ustack():
    return send_request('https://api.at.top/v1/index?signature=0cb39ee3cf3a1651e863c3a1caecce91&timestamp=1540279449')
if __name__ == '__main__':
    content = visit_ustack()
    print(content)