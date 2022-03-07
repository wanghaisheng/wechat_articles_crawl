# -*- coding: utf-8 -*-
import requests

url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
cookie = "appmsglist_action_3007676762=card; RK=Q4jMD2cO45; ptcz=4730884b1007d2f55882f54fec2edef0dd824147d8452b55ccc57fcff2e3fd19; pgv_pvid=5947674060; pgv_info=ssid=s9393064432; sd_userid=43081624498023120; sd_cookie_crttime=1624498023120; rewardsn=; wxtokenkey=777; fqm_sessionid=9a2d4559-ca73-427a-aade-168bb9c2ba09; fqm_pvqid=7fbfb07f-25ee-4cd9-a7d3-54e653c6f50b; wxuin=3423158297; lang=zh_CN; ua_id=niifMf68sUtmfWTaAAAAAP7WyzA3t0wzWRxEFZMwIlc=; mm_lang=zh_CN; nutty_uuid=fad4bf9d-425f-4425-af87-faf865e01eb9; tvfe_boss_uuid=73f62a846c38ae8c; mobileUV=1_17a7f5a55d2_716d; appmsg_token=1122_cjYAML0Y3fkS7ZWnQzgxvkDJyUqZm-ZCpOx6F_mpbF1u-F6e3eZNvE6pGaX7HzkfsouxSTteV6cHVWFb; _qpsvr_localtk=0.2790901404803561; login_type=1; vversion_name=8.2.95; o_cookie=3417947630; pac_uid=1_3417947630; video_omgid=84b3c8d595558e4a; uin=o3417947630; sig=h01e6a3deb6da3541923f98db6b90f87c84e89443ed3935265c2d2d0c13a0bba3a63fadd56a3239b297; skey=@43bptHCGi; devicetype=Windows11x64; version=6305002e; pass_ticket=o8HaKNtN4nFjv2J9AqopRK5iolaFE2tzTr61VcOo32FxAgyrFTrCyaS/E+m1hUF2; wap_sid2=CJmApeAMEnZ5X0hCbGw4M3N1Z3FtUV83SXkzaHNoVTlScTFwcEtObE9jUzVSeTQtUmQ0RGgwR1FNdkJXbmVweFBYQk8wM0xBTFA1ejZpSFVBZHpaZ3I5ZVJJMU54OWl1bzQ2aEthZEpmQlJEcUxqOHZJSUZfcllCSUFBQX5+MJS9/JAGOAxAlE4=; iip=0; uuid=473fb0645d02dfe4d1f137da1f8cb742; rand_info=CAESIASy2gvsoOUCYEAWs3a/xacwdf6gYwZ28C8dzdCEENFY; slave_bizuin=3007676762; data_bizuin=3007676762; bizuin=3007676762; data_ticket=n9HC7hQvnjhdiBgrSMXM1gMq7DsDkyFEI62Paw3R9VmMwxpNEZDYoLx88xVSkYq6; slave_sid=dkFkdWhuUmJmejlkajduZ3NQN05xbHJCRnlqa0h5MW1kWGxCS2hBQm9BOXRjcjJpOXVNd1Jqdmw2OWhXWUI3RkZOMlpZbGIyWG1RMTExTmZNWmZOWmRRWldwc1dIakR3Q0d3dGN3QTJWWm9aNnZXWmJYYjVQb0x1MlkwWUVjaWVQNGs1eDZyUHB1Z1JLckFs; slave_user=gh_722e74396b73; xid=4aa3d5f65340ea4362875a29a49dc267"
headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
}


def get_art_list(token, fakeid):
    data = {
        "token": token,  # token 登陆公众平台后获取
        "lang": "zh_CN",
        "f": "json",
        "ajax": 1,
        "action": "list_ex",
        "begin": 5,
        "count": 5,
        "query": "",
        "fakeid": fakeid,  # __biz
        "type": 9,
    }

    content_json = requests.get(url, headers=headers, params=data, verify=False).json()
    for item in content_json["app_msg_list"]:
        print(item)


get_art_list(token="1302571388", fakeid="MzIwNzE1MzA5Nw==")
