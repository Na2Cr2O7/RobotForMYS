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
TRANSLATE=DOTRANSLATE 

ModalWords=['呢','呢']#语气词
MODALWORDS=ModalWords
EMOTIONS=['_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)','_(香菱-诶嘿嘿)'] # 表情列表
VIDEOURL='https://space.bilibili.com/297786973' # 视频主页地址

REPEATREPLYTIMES=4 # 生成回复的重复次数
POSTLIMIT=150 # 回复帖子上限
REPLYLIMIT=120 # 每次回复的最大回复数

SCROLLTOP='var q=document.documentElement.scrollTop=0'  # 滚动到顶部
SCROLLBOTTOM='var q=document.documentElement.scrollTop=10000'  # 滚动到底部
SCROLLTRIES=12 # 滚动尝试次数

CHECKFOLLOWED=True # 检查关注状态