# -*- coding: utf-8 -*-
import random
import time

import requests
import urllib3

from utils import MongoCore

M_ = MongoCore()
urllib3.disable_warnings()
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
cookie = ""
headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
}
name="纯粹英雄"
token="1028345084"
fakeid="MzI2MjA0MzMzMw=="

def save_mongodb(content_json):
    for item in content_json["app_msg_list"]:
        item_ = {}
        item_["__biz"] = fakeid
        item_["name"] = name
        item_["app_msg_cnt"] = content_json.get("app_msg_cnt")
        item_["aid"] = item.get("aid")
        item_["appmsgid"] = item.get("appmsgid")
        item_["cover"] = item.get("cover")
        item_["digest"] = item.get("digest")
        item_["link"] = item.get("link")
        item_["title"] = item.get("title")
        item_["create_time"] = item.get("create_time")
        item_["update_time"] = item.get("update_time")
        M_.save_to_mongodb(item_, update_key="aid")

def get_art_list(begin=0,count=5):
    data = {
        "token": token,  # token 登陆公众平台后获取
        "lang": "zh_CN",
        "f": "json",
        "ajax": 1,
        "action": "list_ex",
        "begin": begin,
        "count": count,
        "query": "",
        "fakeid": fakeid,  # __biz
        "type": 9,
    }

    content_json = requests.get(url, headers=headers, params=data, verify=False).json()
    save_mongodb(content_json)
    time.sleep(random.randint(15,30))
    begin += 5
    if begin < content_json.get("app_msg_cnt"):
        return get_art_list(begin)
    else:
        print("没有文章了 ...")


# get_art_list()
