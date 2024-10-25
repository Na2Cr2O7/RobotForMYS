# RobotForMYS
### 用于米游社的机器人

## 功能
### 发图片帖
### 自动关注/取关
### 自动点赞/评论
### 自动回复评论
### @
### 写小说
### 上传B站视频
### markdown转图片


## 安装
### 下载完整的压缩包(Download ZIP)
### 下载Python
### 安装ollama
### 安装依赖库
```
    pip install -r requirements.txt
```
下载wkhtmltoimage并添加到环境变量
### 如果使用的视觉模型只能输出英文，请配置argostranslate
### 进入C:\Users\<username>\.local\cache\argos-translate
### 将index.json 复制进去
### 需要下载浏览器驱动，请自行搜索下载
### 在测试的时候使用的是Firefox浏览器，请自行下载对应版本的驱动
### 如果要换成其他的浏览器，请将修改Begin.py
```python
#Begin.py
...
401 try:
402     wd=webdriver.Firefox()# 换成其他浏览器webdriver.Chrome()
403 except:
404     restart()
...
```
### 请将chromedriver.exe或者geckodriver.exe放到项目根目录下
### 补充知识库:knowledge.txt
## 使用
### 安装需要的模型，用于文本生成和图片生成的模型
```
ollama run moondream 
ollama run qwen2.5:0.5b
```
### 配置Constant.py
### 运行Begin.py

```
    python Begin.py
```
### 发图片帖需要的图片需要存放在ImagesPost文件夹下

## 未能解决的问题
### 胡言乱语
### 异想天开
### 重复回复
### 创建合集

