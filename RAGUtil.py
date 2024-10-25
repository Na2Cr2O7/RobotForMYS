import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ollama

# 加载TXT文档
def load_documents(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return content.split('\n\n')

# 加载文档
file_path = 'notebook.txt'
ExtendFilePath='Knowledge.txt'
import os
if not os.path.exists(ExtendFilePath):
    o=open(ExtendFilePath,'w',encoding='utf-8')
    o.close()
if not os.path.exists(file_path):
    o=open(file_path,'w',encoding='utf-8')
    o.close()
o=open(ExtendFilePath,'r',encoding='utf-8')
ExtendContent=o.read()
o.close()
o=open(file_path,'r',encoding='utf-8')
content=o.read()
o.close()
content=ExtendContent+content
o=open('ExtendedNotebook.txt','w',encoding='utf-8')
o.write(content+ExtendContent)
o.close()

documents = load_documents('ExtendedNotebook.txt')
texts = [doc.strip() for doc in documents]

# 使用正则表达式进行分词处理
tokenized_texts = [' '.join(re.findall(r'\b\w+\b', text.lower())) for text in texts]

# 构建TF-IDF向量
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(tokenized_texts)

RevelentDocumentsCount=2
def retrieve_documents(query, tfidf_matrix, vectorizer, texts):
    # 分词处理查询
    query_tokens = ' '.join(re.findall(r'\b\w+\b', query.lower()))
    
    # 计算查询向量
    query_tfidf = vectorizer.transform([query_tokens])
    
    # 计算查询向量与文档向量的相似度
    similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()
    
    # 获取最相关的文档
    sorted_similarities = sorted(zip(similarities, range(len(similarities))), reverse=True)
    top_k = sorted_similarities[:RevelentDocumentsCount]
    
    # 返回最相关的文档片段
    relevant_texts = [texts[i] for _, i in top_k]
    return relevant_texts


def getRevelentTexts(query)->str:
    reverlentTexts= retrieve_documents(query, tfidf_matrix, vectorizer, texts)
    return "\n".join(reverlentTexts)

def generate_with_rag(prompt: str, retriever,Model):
    # 检索最相关的文档
    relevant_texts = retriever(prompt, tfidf_matrix, vectorizer, texts)
    #print(relevant_texts)
    # 构建上下文
    context = "\n".join(relevant_texts)
    
    # 生成回答
    query_with_context = f"{prompt}\n\nContext:\n{context}"
    
    # 使用Ollama模型生成回答
    # 初始化模型
    #model = app.model(model_name="qwen2.5:0.5b", history=[{"role": "user", "content": query_with_context}])
    
    # 生成回答
    response = ollama.chat(model=Model,stream=False,messages=[{"role": "user", "content": query_with_context}])#model.generate(max_tokens=200)
    
    return response['message']['content']
def getRag(question,model='qwen2:0.5b'):
    return generate_with_rag(question,retrieve_documents,model)
# 示例使用
from sys import argv
if __name__=='__main__':
    if len(argv)<2:
        query = "请告诉我关于人工智能的历史"

        # 使用示例模型生成回答
        generated_text = getRag(query)#generate_with_rag(query, retrieve_documents)
        print(generated_text)
    else:
        o=open('knowledge.txt','a',encoding='utf-8')
        o.write(' '.join(argv[1:]).replace('\n',';')+'\n\n')
        o.close()
