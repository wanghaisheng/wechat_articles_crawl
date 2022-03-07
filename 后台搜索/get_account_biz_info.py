# -*- coding: utf-8 -*-
import requests
import urllib3

urllib3.disable_warnings()
url = "https://newrank.cn/xdnphb/data/weixinuser/searchWeixinDataByCondition"
cookie = "tt_token=true;"
headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
}


def get_account_info():
    data = {
        "filter": "",
        "hasDeal": "false",
        "keyName": "三毛游",
        "order": "relation",
        "nonce": "8947c0828",
        "xyz": "1cdbe7f8df2e93137552a86335259861"
    }

    content_json = requests.post(url, headers=headers, data=data, verify=False).json()
    print(content_json)
    for item in content_json.get("value").get("result"):
        item_ = {}
        item_["名称"] = item.get("name").replace("@font", "").replace("#font", "")
        item_["账号"] = item.get("account")
        item_["微信id"] = item.get("wxId")
        item_["__biz"] = item.get("bizInfo")
        item_["城市"] = item.get("city")
        item_["简介"] = item.get("description").replace("@font", "").replace("#font", "")
        print(item_)


get_account_info()
