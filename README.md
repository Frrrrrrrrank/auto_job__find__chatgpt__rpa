这是一个完全免费的脚本，只需要你们自己配置好openai的api即可
希望您能给我点个star
如果在这个寒冷的招聘季，这个脚本能给您一些帮助，带来一些温暖，将让我非常荣幸

希望不要有人拿着我的脚本去割韭菜，都已经被逼到用这种脚本投简历的地步了，身上也没啥油水可榨了吧。可当个人吧


请首先配置好openai的api，随后将pdf简历上传到文件夹auto_job_find里，命名为“my_cover".随后执行write_response.py即可
会自动生成openai的assistant，并在本地产生一个.json文件，只有第一次运行的时候才会产生，后面每次运行如果检测到这个json，就会调用已有的assistant


关于openai部分的包：
openai

About RPA
tutorial video about how to learn rpa: https://www.youtube.com/watch?v=65OPFmEgCbM&list=PLx4LEkEdFArgrdD_lvXe_hYBy8zM0Sp3b&index=1
Package of RPA
selenium
robotframework
robotframework-seleniumlibrary
robotframework-pythonlibcore

Plugin: Intellibot@Selenium Library

------------------下面是简单的教学视频---------------------

B站链接：【赛博投简历脚本教程】 https://www.bilibili.com/video/BV1UC4y1N78v/?share_source=copy_web&vd_source=b2608434484091fcc64d4eb85233122d

油管链接：https://youtu.be/TlnytEi2lD8?si=jfcDj2MZqBptziZc

## 运行方式
先将该项目clone到本地，然后在项目根目录下执行
```bash
pip install -r requirements.txt
```

### assistant方式运行
打开.env文件，在里面配置好OpenAI的API key
随后将pdf简历上传到文件夹auto_job_find里，命名为“my_cover".随后执行write_response.py即可
这种方式不支持使用自定义api，优势是执行速度更快
如果需要使用自定义api，请使用下面的方式运行

### langchain方式
同样打开.env文件，在里面配置好OpenAI的API key和你想要请求的api地址
随后将pdf简历放到文件夹resume里
最后执行write_response.py即可
