# Image Translation API

## Translate Image

Recognize and translate the text in an image, directly return the translated image where the text is translated into the specified language, while preserving the original image's layout and style.

`POST` https://api.piclaza.com/task/v1/image/translate

### Request body

`Content-Type: application/json`

---

**image_url** <font color=Grey>string</font> <font color=LightCoral>required[[1]](#note1)</font>  
Image link

---

**image_urls** <font color=Grey>array of string</font> <font color=LightCoral>required[[1]](#note1)</font>  
List of image link

---

**image_file_b64** <font color=Grey>string</font> <font color=LightCoral>required[[1]](#note1)</font>  
Image file content, [base64 encoding](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data#encoding_data_into_base64_format) (format: `data:[<mediatype>][;base64],<data>`)

---

**image_name** <font color=Grey>string</font>  
Corresponding file name of image_file_b64

---

**source_language** <font color=Grey>string</font> <font color=LightCoral>required</font>  
Source language. Currently support:
* `CHS`: Chinese (Simplified)
* `CHT`: Chinese (Traditional)
* `ENG`: English
* `ESP`: Spanish
* `JPN`: Japanese
* `KOR`: Korean

---

**target_language** <font color=Grey>string</font> <font color=LightCoral>required</font>  
Target language. See [Supported languages](Notes.md#supported-languages) for more information.

---

**translation_vendor** <font color=Grey>string</font>  
The text translation engine, currently supported:
* `Google`: (Default) Widely used in multiple languages around the world
* `Papago`: Good Korean translation
* `DeepL`: Available in [multiple languages](https://developers.deepl.com/docs/resources/supported-languages), excellent in slang and dialect translation
* `ChatGPT`: Use the best Large Language Model(gpt-4o), with accurate translation
* `Aliyun`: Suitable for Chinese translation

---

**qos** <font color=Grey>string</font>  
Quality of Service, currently supported:
* `BestQuality`: (Default) Preference for good translation quality
* `LowLatency`: Preference for fast translation speed

---

> <span id="note1">[1] image_url/image_urls/image_file_b64 are three forms of input image parameters, and one of the three parameters should be set</span>

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
Status code, non-0 indicates an error. See [Response status code](Notes.md#response-status-code) for more information

---

**message** <font color=grey>string</font>  
Error message

---

**data** <font color=grey>map</font>  
Returned data
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
Status code, non-0 indicates an error. See [Response status code](Notes.md#response-status-code) for more information

---

**message** <font color=grey>string</font>  
Error message

---

**task_id** <font color=grey>string</font>  
Task id

---

**type** <font color=grey>string</font>  
Task type

---


## Query the results of image translation


`POST` https://api.piclaza.com/task/v1/image/translate/result

### Parameters

`Content-Type: application/json`

- - -
**task_ids** <font color=Grey>string</font> <font color=LightCoral>required</font> \
List of task ids
- - -
**verbose** <font color=Grey>boolean</font> \
Return detailed OCR data or not, default is false.
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

---

**code** <font color=grey>integer</font>  
Status code, non-0 indicates an error. See [Response status code](Notes.md#response-status-code) for more information

---

**message** <font color=grey>string</font>  
Error message

---

**data** <font color=grey>object</font>  
Returned data
> **results** <font color=grey>array of [Image Translatioin Result](#the-image-translation-result-object) object</font>  

---

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
Status code, non-0 indicates an error. See [Response status code](Notes.md#response-status-code) for more information

---

**message** <font color=grey>string</font>  
Error message

---

**task_id** <font color=grey>string</font>  
Task id

---

**user_id** <font color=grey>integer</font>  
User id

---

**type** <font color=grey>string</font>  
Task type

---

**status** <font color=grey>string</font>  
Task status (ok/running/failed)

---

**original_image** <font color=grey>string</font>  
Original image link

---

**translated_image** <font color=grey>string</font>  
Translated image link

---

**text_removed_image** <font color=grey>string</font>  
Text removed image link

---

**ocr** <font color=grey>list of [Image OCR](#the-image-ocr-object) object</font>  
List of recognized text information

---

### The Image OCR Object

Coordinates representation: the upper left corner of the image is (0, 0); the x-axis is from left to right; the y-axis is from top to bottom

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
id

---

**source** <font color=grey>string</font>  
Recognized original text

---

**target** <font color=grey>string</font>  
Translated text

---

**ori_bounding_box** <font color=grey>string</font>  
Original text box border

---

**bounding_box** <font color=grey>string</font>  
Translated text box border

---

**font_size** <font color=grey>integer</font>  
Text font size

---

**direction** <font color=grey>integer</font>  
Text writing direction (h: horizontal, v: vertical)
Some languages ​​have a tradition of vertical writing, such as Chinese and Japanese

---

**color** <font color=grey>string</font>  
Text color (RGB)

---

**stroke_color** <font color=grey>string</font>  
Text stroke color (RGB)

---

**line_count** <font color=grey>integer</font>  
Line count of text

---

**angle** <font color=grey>integer</font>  
Rotation angle (clockwise rotation from the positive direction of the x-axis, default 0)

---

**align** <font color=grey>string</font>  
Alignment (left/right/center)

---
