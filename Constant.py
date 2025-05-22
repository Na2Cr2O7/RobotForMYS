'''
Constant.py
常量定义
'''
with open('account.txt','r',encoding='utf-8') as f:
    ACCOUNT,PASSWORD=f.read().strip().split() # 账号密码
MAXREPLYCOUNT=300 # 最大回复数

UID=str(442942193)
FANLIST="https://www.miyoushe.com/ys/accountCenter/fanList?id="+UID
FOLLOWLIST="https://www.miyoushe.com/ys/accountCenter/followList?id="+UID

NYANAME='2氯铂酸喵Nya2PtCl6' # 机器人昵称
VERSION='3.2A' # 版本号

TORCHPYTHONPATH=r'C:\RT\nYA\torch2\python.exe '
CHATTERBOTLAUNCH=TORCHPYTHONPATH+r' au3.py '

NOVALPKL='2N.pkl'
NORMALPKL='2.pkl'
POSTPKL='P.pkl'


URL= 'http://127.0.0.1:5000/predict'



def getAnswerIn(pkl,question):
    o=open('question.txt','w',encoding='utf-8')
    o.write(pkl+'.pkl' if '.pkl' not in pkl else pkl)
    o.write('\n')
    o.write(question)
    o.close()
def getAnswerIn2(pkl,question,tokenizer='tokeniser.pkl'):
    import requests
    params = {
    'modelFile': pkl,
    'tokenizerFile': tokenizer,
    'content': question
    }
    response = requests.get(URL, params=params)
    data = response.json()
    return data['response']
    
def waitForAnswer():
    import time
    import os
    while not os.path.exists('chatresponse.txt'):
        time.sleep(1)
    with open('chatresponse.txt','r',encoding='utf-8') as f:
        return f.read()
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
          '_(芙宁娜-好震惊！)','_(芙宁娜-好困难)'
          ,'_(芙宁娜-好无聊)','_(芙宁娜-乐)','_(香菱-好吃)',
          '_(香菱-大吉大利)','_(香菱-冒头)',] # 表情列表
VIDEOURL='https://space.bilibili.com/3546570641377347/video' # 视频地址

REPEATREPLYTIMES=4 # 生成回复的重复次数
POSTLIMIT=150 # 回复帖子上限
REPLYLIMIT=120 # 每次回复的最大回复数

SCROLLTOP='var q=document.documentElement.scrollTop=0'  # 滚动到顶部
SCROLLBOTTOM='var q=document.documentElement.scrollTop=10000'  # 滚动到底部
SCROLLTRIES=2
 # 滚动尝试次数

REPLACEDICT={'玉玉':'抑郁','紫砂':'自杀',NYANAME:'你好,'} # 被替换的词语
REPLACEDICTINREPLY={'#':'\n','人工智能模型':'猫娘','**':'','[NYANAME]':NYANAME
                    ,'AI语言模型':'猫娘','通义千问':'猫娘','Qwen':'猫娘'
                    ,'机器人':'猫娘','机器人回复':'猫娘回复','机器人翻译':'猫娘翻译','AI':'猫娘'} # 回复中被替换的词语

CHECKFOLLOWED=True # 检查关注状态



if __name__=='__main__':

    debugText='''一位离职的首相不过是夸夸其谈的演说家，一个退休的将军不过是胆小软弱的市井之徒。
艺术中最有趣的是艺术家的个性，如果这是独一无二的，那么即使他有一千个错，我也可以原谅。
3批评家如果对技术实践没什么知识，很难说出真正有价值的观点
制造神话，是人类的天性。像那些出类拔萃的名人，人们总是对他们生活中的意外或神秘紧抓不放，深信不疑，缔造传奇，无限狂热。这是对平凡生活的浪漫抗议。
'''
    getAnswerIn('2.pkl', debugText)
   # getAnswerIn(NOVALPKL, '以重要为标题写一篇小说的内容，只要内容!')
    
