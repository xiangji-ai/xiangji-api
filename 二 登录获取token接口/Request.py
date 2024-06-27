import requests
import hashlib
import time

USER_KEY = "YOUR USER KEY"
IMG_TRANS_KEY = "YOUR IMG TRANS KEY"  # 
request_url="http://api.tosoiot.com"

def calc_sign(commit_time) -> str:
    # 签名⽅法: md5(CommitTime + "_" + UserKey + "_" + ImgTransKey) 小写
    str_to_sign = "{}_{}_{}".format(commit_time, USER_KEY, IMG_TRANS_KEY)
    _sign = hashlib.md5(str_to_sign.encode('utf-8')).hexdigest()
    return _sign

commit_time = int(time.time())
sign = calc_sign(commit_time)

payload = {
    "Action": "GetImageTranslate",
    "SourceLanguage": "CHS",
    "TargetLanguage": "ENG",
    "Url": "https://img2.baidu.com/it/u=3536397260,2925037283&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=676",
    "ImgTransKey": IMG_TRANS_KEY,
    "CommitTime": commit_time,
    "Sign": sign,
    "NeedWatermark": 0,
    "NeedRmUrl": 1,
    "Qos": "LowLatency"
}

result = requests.get(request_url, data=payload).json()