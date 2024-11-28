'''
Constant.py
常量定义
'''
with open('account.txt','r',encoding='utf-8') as f:
    ACCOUNT,PASSWORD=f.read().strip().split() # 账号密码
MAXREPLYCOUNT=300 # 最大回复数
NYANAME='氯铂酸喵Nya2PtCl6' # 机器人昵称
VERSION='2.0Pre' # 版本号


CHATTERBOTLAUNCH=r'C:\Users\16928\AppData\Local\Programs\Python\Python37\python.exe chat.py '
ANSWERPATH='chatresponse.txt'
MODELSBYDAY=['qwen2:0.5b'] # 日常模式模型'qwen2.5:1.5b','qwen2:1.5b','qwen:1.8b','qwen2.5:0.5b','qwen2:0.5b'
MODELSBYNIGHT=['qwen2:0.5b'] # 夜间模式模型'qwen2.5:0.5b',
MODELSATDAY=MODELSBYDAY 
MODELSATNIGHT=MODELSBYNIGHT

VISIONMODEL='moondream' # 视觉模型
DOTRANSLATE=True # 是否翻译
TRANSLATE=DOTRANSLATE # 是否翻译

ModalWords=['呢','哦','喵','呀']#语气词
MODALWORDS=ModalWords # 语气词
EMOTIONS=['_(香菱-诶嘿嘿)','_(香菱-星星眼)','_(香菱-新菜谱)',
          '_(芙宁娜-好震惊！)','_(芙宁娜-好困难)','_(芙宁娜-好好笑)'
          ,'_(芙宁娜-好无聊)','_(芙宁娜-乐)','_(香菱-好吃)',] # 表情列表
VIDEOURL='https://space.bilibili.com/3546570641377347/video' # 视频地址

REPEATREPLYTIMES=4 # 生成回复的重复次数
POSTLIMIT=150 # 回复帖子上限
REPLYLIMIT=120 # 每次回复的最大回复数

SCROLLTOP='var q=document.documentElement.scrollTop=0'  # 滚动到顶部
SCROLLBOTTOM='var q=document.documentElement.scrollTop=10000'  # 滚动到底部
SCROLLTRIES=2
 # 滚动尝试次数

REPLACEDICT={'玉玉':'抑郁','紫砂':'自杀',NYANAME:'你好,'} # 被替换的词语
REPLACEDICTINREPLY={'#':'\n','人工智能模型':'猫娘','**':''
                    
                    ,'AI语言模型':'猫娘','通义千问':'猫娘','Qwen':'猫娘'
                    ,'机器人':'猫娘','机器人回复':'猫娘回复','机器人翻译':'猫娘翻译','AI':'猫娘'} # 回复中被替换的词语

CHECKFOLLOWED=True # 检查关注状态

