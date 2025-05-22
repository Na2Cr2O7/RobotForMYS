import difflib
import dill
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from spamClassfier import isSpamDecisionTree


# 创建一个TF-IDF向量化器
vectorizer = TfidfVectorizer()

def cosineSimilarity(text1, text2):
    global vectorizer
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

    # 计算余弦相似度
    cosineSim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return cosineSim[0][0]


def jaccardSimilarity(text1, text2):
    # 使用jieba进行分词
    words1 = set(jieba.lcut(text1))
    words2 = set(jieba.lcut(text2))
    
    # 计算交集和并集
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    # 计算Jaccard相似度
    if len(union) == 0:
        return 0
    else:
        return len(intersection) / len(union)
    

def lavinsteinSimilarity(text1, text2):
    return difflib.SequenceMatcher(None, text1, text2).ratio()

LOG = True

class SpamFilter:
    def __init__(self, threshold=0.75):
        self.spamList = []
        self.threshold = threshold  # 相似度阈值，超过该阈值视为垃圾信息
    def saveSpamList(self, filename='spamList.pkl'):
        """保存垃圾信息列表到文件"""
        with open(filename, 'wb') as f:
            dill.dump(self.spamList, f)
        if LOG:
            print(f"垃圾信息列表已保存到 {filename}")

    def loadSpamList(self, filename='spamList.pkl'):
        """从文件加载垃圾信息列表"""
        try:
            with open(filename, 'rb') as f:
                self.spamList = dill.load(f)
            if LOG:
                print(f"垃圾信息列表已从 {filename} 加载")
        except FileNotFoundError:
            if LOG:
                print(f"文件 {filename} 不存在")
    def saveandLoad(self,filename='spamList.pkl'):
        self.saveSpamList(filename)
        self.loadSpamList(filename)


        
    def addSpam(self, spamText):
        """添加新的垃圾信息"""
        if spamText not in self.spamList:
            self.spamList.append(spamText)
            if LOG:
                print(f"已添加垃圾信息: {spamText}")
        else:
            if LOG:
                print("该垃圾信息已存在")

    def removeSpam(self, spamText):
        """删除垃圾信息"""
        if spamText in self.spamList:
            self.spamList.remove(spamText)
            if LOG:
                print(f"已删除垃圾信息: {spamText}")
        else:
            if LOG:
                print("未找到该垃圾信息")

    def isSpam(self, text, addintoList=True):
        """判断文本是否为垃圾信息"""
        try:
            flag=False
            if isSpamDecisionTree(text):
                flag=True
                if LOG:
                    print("决策树判断为垃圾信息")
            for spam in self.spamList:
                if not flag:
                    similarityDiff = difflib.SequenceMatcher(None, text, spam).ratio()
                    if similarityDiff >= self.threshold:
                        if LOG:
                            print(f"编辑距离相似度: {similarityDiff:.2f}")
                        flag=True
                if not flag:
                    similarityJaccard =jaccardSimilarity(text, spam)
                    if similarityJaccard >= self.threshold:
                        if LOG:
                            print(f"Jaccard相似度: {similarityJaccard:.2f}")
                        flag=True
                if not flag:
                    similarityCosine =cosineSimilarity(text, spam)
                    if similarityCosine >= self.threshold:
                        if LOG:
                            print(f"余弦相似度: {similarityCosine:.2f}")
                        flag=True

                #similarity = similarityDiff
                #similarity=min(similarityDiff,similarityCosine)
                #print(f"{spam}|余弦相似度:{similarityCosine:.2f}|Jaccard相似度:{similarityJaccard:.2f}|编辑距离相似度:{similarityDiff:.2f}",end='\r')
                
                if flag:
                    if addintoList:
                        self.addSpam(spam)
                        self.saveandLoad()
                    return True
            return False

        except:
            return False


    def cleanSpamList(self, newThreshold=0.98):
        for spam in self.spamList:
            for spam2 in self.spamList:
                if spam != spam2:
                    similarity = difflib.SequenceMatcher(None, spam, spam2).ratio()
                    if similarity >= newThreshold:
                        self.removeSpam(spam)
                        if LOG:
                            print(f"已清理垃圾信息: {spam}")
                        break

    def nowItisSpam(self, text):
        """添加一条垃圾信息"""
        self.isSpam(text, addintoList=False)
        self.addSpam(text)
        self.isSpam(text)
        self.saveSpamList()
        self.loadSpamList()

# 示例使用
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="垃圾信息过滤器命令行工具")
    parser.add_argument('-a', '--add', type=str, help='添加垃圾信息')
    parser.add_argument('-r', '--remove', type=str, help='删除垃圾信息')
    parser.add_argument('-i', '--is-spam', type=str, help='判断文本是否为垃圾信息')
    #parser.add_argument('-s', '--save', action='store_true', help='保存垃圾信息列表')
    #parser.add_argument('-l', '--load', action='store_true', help='从文件加载垃圾信息列表')
    parser.add_argument('-c', '--clean', action='store_true', help='清理垃圾信息列表')
    parser.add_argument('-n', '--now-it-is-spam', type=str, help='添加一条垃圾信息')
    parser.add_argument('-v','--view', action='store_true', help='查看垃圾信息列表')
    parser.add_argument('-H', '--html', action='store_true', help='在浏览器中查看')
    args = parser.parse_args()


    filter = SpamFilter()

    # 确保在增删垃圾信息之前加载垃圾信息列表
    filter.loadSpamList()

    if args.html:
        import HTMLPSR
        import webbrowser
        html=HTMLPSR.toHTMLList(filter.spamList,'Spam')
        filename=HTMLPSR.writeHTML(html)
        webbrowser.open(filename)
    if args.view:
        for spam in filter.spamList:
            print(spam)

    if args.add:
        filter.addSpam(args.add)

    if args.remove:
        filter.removeSpam(args.remove)

    if args.is_spam:
        is_spam = filter.isSpam(args.is_spam)
        if is_spam:
            print(f"'{args.is_spam}' 是垃圾信息")
        else:
            print(f"'{args.is_spam}' 不是垃圾信息")
    if args.now_it_is_spam:
        filter.nowItisSpam(args.now_it_is_spam)
    filter.saveSpamList()

