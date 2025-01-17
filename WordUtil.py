import jieba
import random
import re
def segSentence(sentence):
    """使用jieba分词并随机组合成两个句子的数组"""
    words = jieba.lcut(sentence)
    segment=random.randint(0,len(words)-1)
    segments=[''.join(words[:segment]),''.join(words[segment:])]
    if len(segments[0])<1:
        segments[0]="标题(必填)"
    if len(segments[1])<1:
        segments[1]="."
    return segments
def ensureLength(sentences,length=30):
    """确保sentences[0]的长度不超过length"""
    if len(sentences[0])>length:
        original=sentences[0]
        sentences[0]=original[:length]
        sentences[1]=original[length:]+sentences[1]
    return sentences

if __name__=="__main__":
    sentence="这是一个测试句指数大幅答复返回文件华为如何访问然后疯狂接吻和粉色儿科较为符合我司可防核辐射的肌肤科技和大家看是否实施科教返回户籍科好我和滴哦二位后我就去饿哦去哦入侵我i我uu请我是滴哦大窘阿伟  子。"
    segments=segSentence(sentence)
    print(segments)
    segments=ensureLength(segments)
    print(segments)
import re

def replaceAfter(text, replacement):
    pattern = r'我是(.*?)[，。]|我是(.*?)$'
    result = re.sub(pattern, lambda m: '我是' + replacement+'。', text)
    return result
