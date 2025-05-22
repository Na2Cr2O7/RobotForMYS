from time import sleep,time
import torch
import torch.nn as nn
import jieba
import dill as pickle  # 导入 dill 并命名为 pickle
import tqdm
from sys import argv

topic=argv[1]
device='cuda' if torch.cuda.is_available() else 'cpu'
print(device)   
class Dictionary(object):
    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}
        self.idx = 0
    
    def __len__(self):
        return len(self.word2idx)
    
    def add_word(self, word):
        if not word in self.word2idx:
            self.word2idx[word] = self.idx
            self.idx2word[self.idx] = word
            self.idx += 1

class Corpus(object):

    def __init__(self):
        self.dictionary = Dictionary()

    def get_data(self, path, batch_size=20):
        # step 1
        with open(path, 'r', encoding="utf-8") as f:
            tokens = 0
            for line in f.readlines():
                words = jieba.lcut(line) + ['<eos>']
                tokens += len(words)
                for word in words:
                    self.dictionary.add_word(word)

        # step 2
        ids = torch.LongTensor(tokens)
        token = 0
        with open(path, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                words = jieba.lcut(line) + ['<eos>']
                for word in words:
                    ids[token] = self.dictionary.word2idx[word]
                    token += 1

        # step 3
        num_batches = ids.size(0) // batch_size
        ids = ids[:num_batches * batch_size]
        ids = ids.view(batch_size, -1)
        return ids
    def __len__(self):
            # 返回词汇表的大小
            return len(self.dictionary)
class LSTMmodel(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size, num_layers):
        super(LSTMmodel, self).__init__()
        self.embed = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, num_layers, batch_first=True)
        self.linear = nn.Linear(hidden_size, vocab_size)
    
    def forward(self, x, h):
        x = self.embed(x)
        out, (h, c) = self.lstm(x, h)
        out = out.reshape(out.size(0) * out.size(1), out.size(2))
        out = self.linear(out)
        return out, (h, c)
