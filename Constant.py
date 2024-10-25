'''
Constant.py
常量定义
'''

MAXREPLYCOUNT=300 # 最大回复数
NYANAME='' # 机器人昵称
VERSION='' # 版本号
with open('account.txt','r',encoding='utf-8') as f:
    ACCOUNT,PASSWORD=f.read().strip().split() # 账号密码

MODELSBYDAY=[] # 日常模式模型
MODELSBYNIGHT=['qwen2.5:0.5b',] # 夜间模式模型
MODELSATDAY=MODELSBYDAY
MODELSATNIGHT=MODELSBYNIGHT

VISIONMODEL='moondream' # 视觉模型
DOTRANSLATE=True # 是否翻译

ModalWords=['呢','呢']#语气词
MODALWORDS=ModalWords
EMOTIONS=['_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)'] # 表情列表
VIDEOURL='https://space.bilibili.com/297786973' # 视频主页地址