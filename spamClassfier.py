import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# 加载模型
with open('spamClassifier.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
     vectorizer = pickle.load(f)

# 假设 X_train 和 y_train 是训练数据
# X_train_vec = vectorizer.fit_transform(X_train)  # 在实际场景中需要加载训练数据
# 这里假设 vectorizer 已经拟合好
def isSpamDecisionTree(message):
    if not isinstance(message, list):
        message = [message]
    # 对新数据进行向量化
    new_messages_vec = vectorizer.transform(message)

    # 使用加载的模型进行预测
    predictions = loaded_model.predict(new_messages_vec)

    # 定义标签映射
    #label_map = {1: "垃圾信息", 0: "正常信息"}
    # 返回预测结果
    return predictions[0]
if __name__ == '__main__':
    message='这是你的问题，你没好好反思。你现。确保没有过度暴击的情况发生。每个人都有自己的强项和弱项，关键是要找到适合自己的平衡点。希望这些建议对你有所帮助！如果有更多具体我。祝你好运！'
    print(isSpamDecisionTree(message))