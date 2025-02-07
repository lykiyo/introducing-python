import requests as req
import json

def get_data(url):
    resp  = req.get(url)
    text = resp.text
    resp_json = json.loads(text)
    print(resp_json['code'])
    print(resp_json['msg'])

if __name__ == "__main__":
    url = "http://127.0.0.1:8080/hello/index"
    get_data(url)