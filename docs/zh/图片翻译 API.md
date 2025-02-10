# 图片翻译

## 图片翻译

识别和翻译图片中的文字，直接得到翻译结果图片，其中的文字被翻译成指定的语言，同时保留原图的排版和样式。

`POST` https://api.piclaza.com/task/v1/image/translate

### Request body

`Content-Type: application/json`

---

**image_url** <font color=Grey>string</font> <font color=LightCoral>required[[1]](#note1)</font>  
图片链接

---

**image_urls** <font color=Grey>array of string</font> <font color=LightCoral>required[[1]](#note1)</font>  
图片链接列表

---

**image_file_b64** <font color=Grey>string</font> <font color=LightCoral>required[[1]](#note1)</font>  
图片文件内容，[base64 编码](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data#encoding_data_into_base64_format)格式 (format: `data:[<mediatype>][;base64],<data>`)

---

**image_name** <font color=Grey>string</font>  
image_file_b64 对应的文件名

---

**source_language** <font color=Grey>string</font> <font color=LightCoral>required</font>  
源语言，目前支持
* `CHS`: 中文(简体)
* `CHT`: 中文(繁体)
* `ENG`: 英语
* `ESP`: 西班牙语
* `JPN`: 日语
* `KOR`: 韩语

---

**target_language** <font color=Grey>string</font> <font color=LightCoral>required</font>  
目标语言，支持语言列表见[支持语言代码](说明.md#支持语言代码)

---

**translation_vendor** <font color=Grey>string</font>  
使用的文本翻译引擎，目前支持
* `Google`: (默认) 广泛适用全球多种语言 
* `Papago`: 韩语翻译效果好
* `DeepL`: 适用[多种语言](https://developers.deepl.com/docs/resources/supported-languages)，在俚语、方言翻译方面表现优异
* `ChatGPT`: 使用目前最好的大语言模型(gpt-4o)，翻译准确
* `Aliyun`: 适合中文翻译

---

**qos** <font color=Grey>string</font>  
服务质量等级，目前支持
* `BestQuality`: (默认) 注重翻译效果
* `LowLatency`: 注重翻译速度

---

> <span id="note1">[1] image_url/image_urls/image_file_b64 是输入图片参数的三种形式，三个参数选择一个</span>

Example

```json
{
    "image_url": "https://m.media-amazon.com/images/I/71Y0duLL0jL._AC_SL1500_.jpg",
    "source_language": "ENG",
    "target_language": "KOR",
    "translation_vendor": "Google"
}
```

### Response body

`Content-Type: application/json`

---

**code** <font color=grey>integer</font>  
状态码，非 0 表示错误，具体含义见[响应状态码说明](说明.md#响应状态码说明)

---

**message** <font color=grey>string</font>  
错误信息

---

**data** <font color=grey>map</font>  
返回数据
> **results** <font color=grey>array of [Task](#the-task-object) object</font>

---

Example

```json
{
    "code": 0,
    "data": {
        "results": [
            {
                "code": 0,
                "task_id": "827e1d0a0a68771e",
                "type": "image-translation-google",
            }
        ]
    }
}
```

### The Task Object

---

**code** <font color=grey>integer</font>  
状态码，非 0 表示错误，具体含义见[响应状态码说明](说明.md#响应状态码说明)

---

**message** <font color=grey>string</font>  
错误信息

---

**task_id** <font color=grey>string</font>  
任务 id

---

**type** <font color=grey>string</font>  
任务类型

---


## 查询图片翻译结果

`POST` https://api.piclaza.com/task/v1/image/translate/result

### Parameters

`Content-Type: application/json`

- - -
**task_ids** <font color=Grey>string</font> <font color=LightCoral>required</font> \
任务 id 列表
- - -
**verbose** <font color=Grey>boolean</font> \
是否返回详细的 OCR 数据，默认 false
- - -

Example

```json
{
    "task_ids": ["863ab3836328f4ec"],
    "verbose": true
}
```

### Responses

`Content-Type: application/json`

- - -
**code** <font color=grey>integer</font>  
状态码，非 0 表示错误，具体含义见[响应状态码说明](说明.md#响应状态码说明)
- - -
**message** <font color=grey>string</font>  
错误信息
- - -
**data** <font color=grey>object</font>  
返回数据
> **results** <font color=grey>array of [Image Translatioin Result](#the-image-translation-result-object) object</font>  
- - -

Example

```json
{
    "code": 0,
    "data": {
        "results": [
            {
                "code": 0,
                "task_id": "863ab3836328f4ec",
                "request_id": "863ab3836328f4ec",
                "source_language": "ENG",
                "target_language": "KOR",
                "original_image": "https://i.tosoiot.com/1cbb77123add49a2.jpg",
                "translated_image": "https://i.tosoiot.com/1cbb77123add49a2-f.jpg",
                "text_removed_image": "https://i.tosoiot.com/1cbb77123add49a2-i.jpg",
                "ocr": [
                    {
                        "id": 1,
                        "source": "External function",
                        "target": "외부 기능",
                        "ori_bounding_box": "[[173,133], [617,133], [617,177], [173,177]]",
                        "bounding_box": "[[173,133], [617,133], [617,177], [173,177]]",
                        "font_size": 35,
                        "direction": "h",
                        "color": "255,255,255",
                        "stroke_color": "255,255,255",
                        "line_count": 1,
                        "align": "left"
                    },
                    {
                        "id": 5,
                        "source": "The watch comes with an external speaker, which can play the recording directly without other equipment.",
                        "target": "시계에는 외부 스피커가 있어서 다른 장비 없이도 녹음 내용을 직접 재생할 수 있습니다.",
                        "ori_bounding_box": "[[ 93,208], [697,208], [697,297], [ 93,297]]",
                        "bounding_box": "[[ 93,208], [697,208], [697,297], [ 93,297]]",
                        "font_size": 24,
                        "direction": "h",
                        "color": "255,255,255",
                        "stroke_color": "255,255,255",
                        "line_count": 2,
                        "align": "center"
                    }
                ]
            }
        ]
    }
}
```

### The Image Translation Result Object

---

**code** <font color=grey>integer</font>  
状态码，非 0 表示错误，具体含义见[响应状态码说明](说明.md#响应状态码说明)

---

**message** <font color=grey>string</font>  
错误信息

---

**task_id** <font color=grey>string</font>  
任务 id

---

**user_id** <font color=grey>integer</font>  
用户 id

---

**type** <font color=grey>string</font>  
任务类型

---

**status** <font color=grey>string</font>  
任务状态 (ok/running/failed)

---

**original_image** <font color=grey>string</font>  
原图链接

---

**translated_image** <font color=grey>string</font>  
翻译结果图片链接

---

**text_removed_image** <font color=grey>string</font>  
去除文字的图片链接

---

**ocr** <font color=grey>list of [Image OCR](#the-image-ocr-object) object</font>  
识别到的文本信息列表

---

### The Image OCR Object

数据中涉及坐标表示: 图片左上角为 (0, 0) 点; x 轴从左向右; y 轴从上向下

```
(0,0)---x--->
  |
  |
  y
  |
  |
  v
```

---

**id** <font color=grey>integer</font>  
编号

---

**source** <font color=grey>string</font>  
识别到的原文

---

**target** <font color=grey>string</font>  
译文

---

**ori_bounding_box** <font color=grey>string</font>  
原文文本框边界

---

**bounding_box** <font color=grey>string</font>  
译文文本框边界

---

**font_size** <font color=grey>integer</font>  
文字大小

---

**direction** <font color=grey>integer</font>  
文字书写方向 (h: 横向, v: 纵向)  
部分语言有纵向书写的习惯，比如中文、日文

---

**color** <font color=grey>string</font>  
文字颜色 (RGB)

---

**stroke_color** <font color=grey>string</font>  
文字描边颜色 (RGB)

---

**line_count** <font color=grey>integer</font>  
行数

---

**angle** <font color=grey>integer</font>  
旋转角度 (从x轴正方向顺时针旋转的角度, 默认0)

---

**align** <font color=grey>string</font>  
对齐方式 (left/right/center)

---
