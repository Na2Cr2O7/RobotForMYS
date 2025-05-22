from LSTMConstant import *

def generate_article(model, corpus, num_samples=300,start=""):
    model.eval()  # 设置为评估模式
 # 明确指定使用CPU
    
    state = (torch.zeros(num_layers, 1, hidden_size).to(device),
             torch.zeros(num_layers, 1, hidden_size).to(device))
    
    prob = torch.ones(len(corpus)).to(device)
    _input = torch.multinomial(prob, num_samples=1).unsqueeze(1).to(device)
    
    article = start
    
    with torch.no_grad():  # 关闭梯度计算
        for i in range(num_samples):
            output, state = model(_input, state)
            prob = output.exp().squeeze().cpu()
            word_id = torch.multinomial(prob, num_samples=1).item()
            _input.fill_(word_id)
            word = corpus.dictionary.idx2word[word_id]
            word = '\n' if word == '<eos>' else word
            article += word
    newArticle=''
    for text in article.split('\n'):
        if text!='':
            newArticle+=text+'\n'
    return newArticle

if __name__ == "__main__":
    # 模型参数
    embed_size = 3000
    hidden_size = 1024
    num_layers = 1
    vocab_size = None  # 将根据实际语料库大小设置

    # 加载语料库
    with open('TITLEcorpus.pkl', 'rb') as f:
        corpus = pickle.load(f)

    # 初始化模型
    vocab_size = len(corpus.dictionary)
    model = LSTMmodel(vocab_size, embed_size, hidden_size, num_layers)
    model=torch.load('TitleLSTM.pkl',weights_only=False,map_location=torch.device(device))
    # 加载训练好的模型，并明确指定使用CPU
    #model.load_state_dict(torch.load('lstm_model.pth', map_location=torch.device('cpu')))
    model.to(device)
    generateTitle=topic
    generateTitle = generate_article(model, corpus, num_samples=8,start=generateTitle)
    with open('generateTitle.txt','w',encoding='utf8') as f:
        f.write(generateTitle)
    print(generateTitle)