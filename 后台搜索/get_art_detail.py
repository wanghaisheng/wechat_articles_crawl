import time

import requests
import urllib3
from lxml import etree

from utils import MongoCore

urllib3.disable_warnings()
import config

M_ = MongoCore()

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "RK=Q4jMD2cO45; ptcz=4730884b1007d2f55882f54fec2edef0dd824147d8452b55ccc57fcff2e3fd19; pgv_pvid=5947674060; pgv_info=ssid=s9393064432; sd_userid=43081624498023120; sd_cookie_crttime=1624498023120; rewardsn=; wxtokenkey=777; fqm_sessionid=9a2d4559-ca73-427a-aade-168bb9c2ba09; fqm_pvqid=7fbfb07f-25ee-4cd9-a7d3-54e653c6f50b; wxuin=3423158297; lang=zh_CN; ua_id=niifMf68sUtmfWTaAAAAAP7WyzA3t0wzWRxEFZMwIlc=; mm_lang=zh_CN; nutty_uuid=fad4bf9d-425f-4425-af87-faf865e01eb9; tvfe_boss_uuid=73f62a846c38ae8c; mobileUV=1_17a7f5a55d2_716d; appmsg_token=1122_cjYAML0Y3fkS7ZWnQzgxvkDJyUqZm-ZCpOx6F_mpbF1u-F6e3eZNvE6pGaX7HzkfsouxSTteV6cHVWFb; _qpsvr_localtk=0.2790901404803561; login_type=1; vversion_name=8.2.95; o_cookie=3417947630; pac_uid=1_3417947630; video_omgid=84b3c8d595558e4a; uin=o3417947630; sig=h01e6a3deb6da3541923f98db6b90f87c84e89443ed3935265c2d2d0c13a0bba3a63fadd56a3239b297; skey=@43bptHCGi; devicetype=Windows11x64; version=6305002e; pass_ticket=o8HaKNtN4nFjv2J9AqopRK5iolaFE2tzTr61VcOo32FxAgyrFTrCyaS/E+m1hUF2; wap_sid2=CJmApeAMEnZ5X0hCbGw4M3N1Z3FtUV83SXkzaHNoVTlScTFwcEtObE9jUzVSeTQtUmQ0RGgwR1FNdkJXbmVweFBYQk8wM0xBTFA1ejZpSFVBZHpaZ3I5ZVJJMU54OWl1bzQ2aEthZEpmQlJEcUxqOHZJSUZfcllCSUFBQX5+MJS9/JAGOAxAlE4=; iip=0; uuid=473fb0645d02dfe4d1f137da1f8cb742; xid=4aa3d5f65340ea4362875a29a49dc267",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
}


def etree_(html):
    return etree.HTML(html)


def get_html(url):
    response = requests.get(url, headers=headers, verify=False)
    return response.text


def parse_text(html):
    doc = etree_(html)
    text_ = doc.xpath("//section//text()")
    text_ = "".join(text_)
    return text_


def parse_image(html, aid):
    doc = etree_(html)
    img_s = doc.xpath("//div[@id='page-content']//img/@data-src")
    for index, img_url in enumerate(img_s):
        save_image(img_url, f"{aid}_{index + 1}")


def save_image(url, aid):
    response = requests.get(url, headers=headers, verify=False)
    with open(f"./纯粹英雄/IMAGE/{aid}.jpg", "wb") as f:
        f.write(response.content)


def save_html(html, aid):
    with open(f"./纯粹英雄/HTML/{aid}.html", "w", encoding="utf-8") as f:
        html_ = html.replace("mmbiz.qpic.cn", "wximg.cccyun.cc")
        f.write(html_)


if __name__ == '__main__':
    for obj_ in M_.collection.find({}):
        print("正在抓取: ",obj_.get("title"), obj_.get("aid"))
        html_ = get_html(url=obj_.get("link"))
        parse_image(html=html_, aid=obj_.get("aid"))
        save_html(html=html_, aid=obj_.get("aid"))
        time.sleep(8)
