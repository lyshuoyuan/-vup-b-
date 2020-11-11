#这个用来获取单个直播间的人气值，uid是使用者的uid用来验证不可不填，roomid是需要爬取的直播间id，不能不填，中间注释处补上cookie，这几个值会影响后面的key应该

def getpopularity(roomid,uid):
    import requests
    import json
    import websocket
    
    url = "https://api.live.bilibili.com/xlive/web-room/v1/index/getDanmuInfo?id="+str(roomid)+"&type=0"
    headers={
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
        "Connection": "keep-alive",
        "Cookie": "",#一定要填cookie，不然后面的key会少位数连接不上
        "Host": "api.live.bilibili.com",
        "Origin": "https://live.bilibili.com",
        "Referer": "https://live.bilibili.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"
    }

    r = requests.get(url=url,headers = headers)
    data = json.loads(r.text)
    key = data['data']['token']
    ws_url = "wss://"+data['data']['host_list'][0]['host']+'/sub'    
    msg = b'\x00\x00\x00\xfb\x00\x10\x00\x01\x00\x00\x00\x07\x00\x00\x00\x01{"uid":'+str.encode(str(uid))+b',"roomid":'+str.encode(str(roomid))+b',"protover":2,"platform":"web","clientver":"2.3.1","type":2,"key":"'+str.encode(key)+b'"}'
    data2 = [0x00, 0x00, 0x00, 0x1F, 0x00, 0x10, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x01, 0x5B, 0x6F, 0x62, 0x6A, 0x65, 0x63, 0x74, 0x20, 0x4F, 0x62, 0x6A, 0x65, 0x63, 0x74, 0x5D]
    ws = websocket.create_connection(ws_url,timeout=10)
    ws.send(msg)
    received = ws.recv()
    ws.send(bytes(data2))
    received = ws.recv()
    a=[]
    for i in received[:]:
        a.append(i)
    if len(a)==20:
        num = a[19]+a[18]*16**2+a[17]*16**4+a[16]*16**6
    ws.close()
    return num
