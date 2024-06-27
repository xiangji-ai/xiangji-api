# xiangji-api
XiangJi AI API文档
* [xiangjifanyi.com](xiangjifanyi.com) 
* [xiangji.ai](xiangjiai.com)

## 1. 访问控制    

登录象寄官网 [www.xiangjifanyi.com/home](http://www.xiangjifanyi.com/home) ，手机号注册账户后，即可获取：

1.  **个人密钥（UserKey）**
   
2.  图⽚翻译**服务标识码（ImgTransKey）**
    
   * 图片翻译中目前支持的文本翻译引擎有：
    阿里云、百度、Google、Papago、DeepL
            
3.  文本翻译**服务标识码（TextTransKey）**
    
4.  一键抠图**服务标识码（ImgMattingKey）**
    
5.  视频翻译**服务标识码（VideoTransKey）**
    
6.  AIGC**服务标识码（AigcKey）**

## 2. 登录获取token接口
2.1 访问接口
- 请求地址: http://api.tosoiot.com
- 请求类型: GET

2.2 请求参数

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

2.3 返回参数

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


## 待添加...
  - 通用鉴权参数
- 额度查询接口
- 文本翻译接口
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