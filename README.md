# xiangji-api
XiangJi AI API文档
* [xiangjifanyi.com](xiangjifanyi.com) 
* [xiangji.ai](xiangjiai.com)

## 访问控制 (各自密钥)   

登录象寄官网 [www.xiangjifanyi.com/home](http://www.xiangjifanyi.com/home) ，手机号注册账户后，即可获取：

1.  **个人密钥（UserKey）**
   
2.  图⽚翻译**服务标识码（ImgTransKey）**
    
   * 图片翻译中目前支持的文本翻译引擎有：
    阿里云、百度、Google、Papago、DeepL
            
3.  文本翻译**服务标识码（TextTransKey）**
    
4.  一键抠图**服务标识码（ImgMattingKey）**
    
5.  视频翻译**服务标识码（VideoTransKey）**
    
6.  AIGC**服务标识码（AigcKey）**



| API | 密钥 | 接口 |
| --- | --- | --- |
| 图片翻译 | ImageTransKey | [http://api.tosoiot.com](http://api.tosoiot.com) |
| 文本翻译 | TextTransKey | [http://api.tosoiot.com](http://api.tosoiot.com) |
|  |  |  |
|  |  |  |
*待添加。。。。。。

## 通用鉴权参数
### MD5 签名方式

MD5 签名方式视情况而定 每个API使用各自的密钥(KEY)  
签名⽅法: Sign=md5(CommitTime + "_" + UserKey + "_" + 【各自密钥】) // 注意:小写

| 字段名称 | 是否必选 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| Sign | 是 | String | "4f93f79edff764a7" | 签名，签名方法：  <br>例：图片翻译  <br>Sign=md5(CommitTime + "_"+ UserKey + "_" + ImgTransKey ) |
| input_string | 否 | String | "1234567891_6257867386_3570049829" | Sign=md5(input_string)  <br>  <br>input_string = str(CommitTime + "_" + UserKey + "_" + 【各自密钥】)) |

### 特别格式 (翻译额度查询 API)

签名⽅法: md5( 【Type】 + "_" + UserKey + "_" + 【各自密钥】) 小写

| 字段名称 | 是否必选 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| Type | 是 | Integer | 1 | 购买类型  <br>(1=阿里云图片翻译,  <br>2=文本翻译,  <br>3=谷歌图片翻译 等等 |
| Sign | 是 | String | 4f93f79edff764a7 | 签名，签名方法：Type=1 时 文本翻译额度查询，Sign=md5( Type + "_"+ UserKey + "_" + ImgTransKey ) 小写；  <br>  <br>Type=2 时，Sign=md5( Type + "_"+ UserKey + "_" + TextTransKey ) 以此类推 |

需要更清晰的解释请参考 【翻译额度查询】

### MD5 示例代码

```
import requests
import hashlib
import time
USER_KEY = "YOUR USER KEY"
IMG_MATTING_KEY = "YOUR IMAGE MATTING KEY"
request_url="http://api.tosoiot.com"
def calc_sign(commit_time) -> str:
    # 签名⽅法: md5(CommitTime + "_" + UserKey + "_" + ImgTransKey) 小写
    str_to_sign = "{}_{}_{}".format(commit_time, USER_KEY, IMG_MATTING_KEY)
    _sign = hashlib.md5(str_to_sign.encode('utf-8')).hexdigest()
    return _sign
commit_time = int(time.time())
sign = calc_sign(commit_time)

 ```


## 2. 登录获取token接口
##### 2.1 访问接口
- 请求地址: http://api.tosoiot.com
- 请求类型: GET

##### 2.2 请求参数

| 字段名称 | 是否必选 | 类型 | 示例值 | 描述 |
|:---:|:---:|:---:|:---:|:---:|
| Action | 是 | String | GetImageTranslate | 服务类型，GetImageTranslate 指“图⽚翻译”服务 |
| SourceLanguage | 是 | String | CHS | 来源语⾔，支持 中文(CHS/CHT)、英(ENG) 参考[语言列表] |
| TargetLanguage | 是 | String | KOR | 目标语言  参考[语言列表] |
| Url | 是 | String | https://img.xx.com/O107064055.jpg | 图⽚地址，注 ：文中url参数在传递时需要进行urlencode |
| ImgTransKey | 是 | String | 1234567890 | 图⽚翻译服务标识码 参照[访问控制] |
| CommitTime | 是 | String | 1653229753 | 秒级时间戳 |
| Sign | 是 | String | 044a0bdea4128bb46aa59214ca821d6b | 签名， 签名⽅法: md5(CommitTime + "_" + UserKey + "_" + ImgTransKey) 小写 |
| NeedWatermark | 否 | Integer | 0 | （非必需字段）是否添加水印，1=添加，0=不添加，默认为 1。需在 Web 端配置水印模板，否则不添加 |
| NeedRmUrl | 否 | Integer | 1 | （非必需字段）是否返回去文字图片链接。1=返回去文字图片链接，其它或无此字段，则不返回去文字图片链接 |
| Qos | 否 | String | LowLatency | （非必需字段）翻译速度与翻译质量的偏好选项。LowLatency=偏好速度而牺牲质量 ，BestQuality=偏好图片翻译的质量 |
|  |  |  |  |  |

NeedWatermark 设置为 1，则需要在网站账户后台配置好水印设置。 

##### 2.3 返回参数

| 字段名称 | 类型 | 示例值 | 描述 |  |
|:---:|:---:|:---:|:---:|---|
| Code | Integer | 200 | 状态码（详细列表见文末），200 代表正常 |  |
| Message | String | ok | 状态码的明文含义，正常 |  |
| RequestId | String | 4f93f79edff764a7 | 请求的唯一 id |  |
| Data | Json |  | 返回数据的 json 内容 |  |
| -- Url | String | http://i.tosoiot.com/r/5b135a6003a3075d/f-xxxx.jpg | 翻译后的目标图片地址（图片地址的默认有效期为80天，如需长时存储请联系客服） |  |
| -- SsUrl | String | https://i.tosoiot.com/r/5b135a6003a3075d/f-xxxx.jpg | 翻译后的目标图片 https 地址 |  |
| -- RmUrl | String | http://i.tosoiot.com/r/5b135a6003a3075d/ixx-xx.jpg | 去除文字后的目标图片地址 |  |
| -- SsRmUrl | String | https://i.tosoiot.com/r/5b135a6003a3075d/i-xxxx.jpg | 去除文字后的目标图片 https 地址 |  |
|  |  |  |  |  |

##### 2.4 示例代码

```
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
```

#### 2.5 完整返回参数的真实实例
```
{
    "Message":"ok",
    "RequestId":"bab123a12345a12d",
    "Data":{
       "Url":"http://i.tosoiot.com/bab123a12345a12d/20240426-15-3126-9cfb/u=3536397260,2925037283&fm=253&fmt=auto&app=138&f=JPEG-f.jpg",
       "SslUrl":"https://i.tosoiot.com/bab123a12345a12d/20240426-15-3126-9cfb/u=3536397260,2925037283&fm=253&fmt=auto&app=138&f=JPEG-f.jpg",
       "RmUrl":"http://i.tosoiot.com/bab123a12345a12d/20240426-15-3126-9cfb/u=3536397260,2925037283&fm=253&fmt=auto&app=138&f=JPEG-f.jpg",
       "SslRmUrl":"https://i.tosoiot.com/bab123a12345a12d/20240426-15-3126-9cfb/u=3536397260,2925037283&fm=253&fmt=auto&app=138&f=JPEG-f.jpg"
    },
    "Code":200
 }
```

### 3. 翻译额度查询接口

#### 3.1 访问接口
- 请求地址: http://www.tosoiot.com/open/user/amount-query
- 请求类型: POST


#### 3.2 请求参数
|      字段名称     | 是否必选 |   类型  | 示例值           |                                                                              描述                                                                             |
|:-----------------:|:--------:|:-------:|------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Type              |    是    | Integer | 1                | 购买类型 (1=阿里云图片翻译, 2=文本翻译, 3=谷歌图片翻译, 4=papago图片翻译, 5=百度图片翻译, 6=图片暂存, 7=DeepL图片翻译, 8=抠图, 9=视频翻译, 10=文本转语音)     |
| ImgTransKey       |    否    |  String | 参照[访问控制]   | 图⽚翻译服务标识码，当且仅当 Type=1 时需传递此参数                                                                                                            |
| TextTransKey      |    否    |  String | 参照[访问控制]   | 文本翻译服务标识码，当且仅当 Type=2 时需传递此参数                                                                                                            |
| ImgTransGoogleKey |    否    |  String | 参照[访问控制]   | 文本翻译服务标识码，当且仅当 Type=3 时需传递此参数                                                                                                            |
| ImgTransPapagoKey |    否    |  String | 参照[访问控制]   | 文本翻译服务标识码，当且仅当 Type=4 时需传递此参数                                                                                                            |
| ImgTransBaiduKey  |    否    |  String | 参照[访问控制]   | 文本翻译服务标识码，当且仅当 Type=5 时需传递此参数                                                                                                            |
| ImgTransDeeplKey  |    否    |  String | 参照[访问控制]   | 文本翻译服务标识码，当且仅当 Type=7 时需传递此参数                                                                                                            |
| ImgMattingKey     |    否    |  String | 参照[访问控制]   | 文本翻译服务标识码，当且仅当 Type=8 时需传递此参数                                                                                                            |
| VideoTransKey     |    否    |  String | 参照[访问控制]   | 视频翻译服务标识码，当且仅当 Type=9 时需传递此参数                                                                                                            |
| Sign              |    是    |  String | 4f93f79edff764a7 | 签名，签名方法：Type=1 时，Sign=md5( Type + "_"+ UserKey + "_" + ImgTransKey ) 小写；Type=2 时，Sign=md5( Type + "_"+ UserKey + "_" + TextTransKey ) 以此类推 |

1.3 返回参数
|   字段名称   |   类型  | 示例值  |               描述               |
|:------------:|:-------:|---------|:--------------------------------:|
| code         | Integer | 0       | 状态码，正常                     |
| msg          |  String | ok      | 状态码的明文含义，正常           |
| data         |   Json  |         | 返回数据的 json 内容             |
| -- type      | Integer | 1       | 购买类型                         |
| -- leftCount |  String | “80820” | 剩余的图片翻译额度或文本翻译额度 |

#### 3.4 示例代码
```
import requests
import hashlib
import time
import base64

USER_KEY = "YOUR USER KEY"
TEXT_TRANS_KEY = "YOUR TEXT TRANS KEY"
TYPE = 2
request_url="http://www.tosoiot.com/open/user/amount-query"

def calc_sign() -> str:
    # 签名⽅法: md5(Type + "_" + UserKey + "_" + TextTransKey) 小写
    str_to_sign = "{}_{}_{}".format(TYPE, USER_KEY, TEXT_TRANS_KEY)  # Update API KEY appropriately
    _sign = hashlib.md5(str_to_sign.encode('utf-8')).hexdigest()
    return _sign

sign = calc_sign()

payload = {
    "Type": TYPE,
    "TextTransKey": TEXT_TRANS_KEY,  # Update according to type
    "Sign": sign,

    # ImgTransKey  #Choose and implement one of the KEYs
    # TextTransKey
    # ImgTransGoogleKey
    # ImgTransPapagoKey
    # ImgTransBaiduKey
    # ImgTransDeeplKey
    # ImgMattingKey
    # VideoTransKey
}

result=requests.post(request_url, data=payload).json()
```

#### 3.5 完整返回参数的真实实例:
```
{
   "code":"0",
   "msg":"ok",
   "data":{
      "type":2,
      "leftCount":"9270"
   }
}
```

### 4. 文本翻译接口

#### 4.1 访问接口
- 请求地址: http://api.tosoiot.com
- 请求类型: GET

#### 4.2 请求参数
|    字段名称    | 是否必选 |   类型  |              示例值              |                                       描述                                       |
|:--------------:|:--------:|:-------:|:--------------------------------:|:--------------------------------------------------------------------------------:|
| Action         |    是    |  String | GetTextTranslate                 | 服务类型，GetTextTranslate 指“文本翻译”服务                                      |
| SourceLanguage |    是    |  String | CHS                              | 来源语⾔，支持 中文(CHS/CHT)、英(ENG) 参考[语言列表]                             |
| TargetLanguage |    是    |  String | KOR                              | 目标语言  参考[语言列表]                                                         |
| Text           |    是    |  String | 我是中国人                       | 需翻译的原文                                                                     |
| TextTransKey   |    是    |  String | 1234567890                       | 文本翻译服务标识码 参照[访问控制]                                                |
| CommitTime     |    是    |  String | 1653229753                       | 秒级时间戳                                                                       |
| Sign           |    是    |  String | 044a0bdea4128bb46aa59214ca821d6b | 签名， 签名⽅法: md5(CommitTime + "_" + UserKey + "_" + TextTransKey) 小写       |
| Type           |    否    | Integer | 2                                | （非必需字段）翻译引擎。Aliyun=0;Google=1;Papago=2;Baidu=3;DeepL=4;默认是 Aliyun |
#### 4.3 返回参数
|      字段名称     |   类型  |      示例值      |                  描述                  |                                       描述                                       |
|:-----------------:|:-------:|:----------------:|:--------------------------------------:|:--------------------------------------------------------------------------------:|
| Code              | Integer |        200       | 状态码（详细列表见文末），200 代表正常 | 服务类型，GetTextTranslate 指“文本翻译”服务                                      |
| Message           |  String |        ok        | 状态码的明文含义，正常                 | 来源语⾔，支持 中文(CHS/CHT)、英(ENG) 参考[语言列表]                             |
| RequestId         |  String | 4f93f79edff764a7 | 请求的唯一 id                          | 目标语言  参考[语言列表]                                                         |
| Data              |   Json  |                  | 返回数据的 json 内容                   | 需翻译的原文                                                                     |
| -- SourceLanguage |  String |        CHS       | 来源语⾔                               | 文本翻译服务标识码 参照[访问控制]                                                |
| -- TargetLanguage |  String |        ENG       | 目标语言                               | 秒级时间戳                                                                       |
| -- OriginText     |  String |    我是中国人    | 原文                                   | 签名， 签名⽅法: md5(CommitTime + "_" + UserKey + "_" + TextTransKey) 小写       |
| -- Text           |  String |   I am Chinese   | 译文                                   | （非必需字段）翻译引擎。Aliyun=0;Google=1;Papago=2;Baidu=3;DeepL=4;默认是 Aliyun |

#### 4.4 示例代码
```
Python
import requests
import hashlib
import time

USER_KEY = "YOUR USER KEY"
TEXT_TRANS_KEY = "YOUR TEXT TRANS KEY"
request_url="http://api.tosoiot.com"

def calc_sign(commit_time) -> str:
    # 签名⽅法: md5(CommitTime + "_" + UserKey + "_" + ImgTransKey) 小写
    str_to_sign = "{}_{}_{}".format(commit_time, USER_KEY, TEXT_TRANS_KEY)
    _sign = hashlib.md5(str_to_sign.encode('utf-8')).hexdigest()
    return _sign

source_string = "我是中国人"

commit_time = int(time.time())
sign = calc_sign(commit_time)

payload = {
    "Action": "GetTextTranslate",
    "SourceLanguage": "CHS",
    "TargetLanguage": "ENG",
    "Text": source_string,
    "TextTransKey": TEXT_TRANS_KEY,
    "CommitTime": commit_time,
    "Sign": sign,
    "Type": 0
}

result=requests.get(request_url, data=payload).json()
```

#### 4.5  完整返回参数的真实实例:
```
{
   "Message":"ok",
   "RequestId":"8102d026f753557f",
   "Data":{
      "SourceLanguage":"CHS",
      "TargetLanguage":"ENG",
      "OriginText":"我是中国人",
      "Text":"I am Chinese"
   },
   "Code":200
}
```

## 待添加...

- 图片翻译接口
  - 单次url请求
  - 单次文件请求
  - 批量请求
  - 翻译结果查询
    - 简单查询
    - 明细查询
  - 图片精修iframe对接
- 视频翻译接口 象寄视频翻译对接文档
  - 视频翻译API
  - 视频翻译iframe对接
  - 语音合成TTS服务
  - 语音识别STT服务
  - 人声提取/背景音乐提取服务（暂缺）
- 智能抠图
  - 智能抠图API
    - 本地图片请求
    - 图片URL请求
    - 抠图结果查询
  - 智能抠图iframe对接  象寄智能抠图iframe编辑器对接文档
- 智能擦除 
  - 智能擦除API 象寄智能擦除API对接文档
  - 智能擦除iframe对接 象寄智能擦除iframe编辑器对接文档
- 高清放大
  - 高清放大API AI 高清放大
  - 高清放大iframe对接
- 变图
  - 变图API
  - 变图iframe对接
- AI 生图 象寄 AIGC 编辑器对接文档
  - AIGC编辑器iframe对接
- 电商平台数据获取API
- 代理商功能API
- 其他
  - 错误码
  - 语言列表