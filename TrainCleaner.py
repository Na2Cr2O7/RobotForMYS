import spamFilter
import tqdm

# 初始化过滤器
Filter = spamFilter.SpamFilter()
Filter.loadSpamList()

# 打开训练集文件
with open('trainingData.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 用于存储过滤后的行
filtered_lines = []

# 遍历每一行
i = 0
while i < len(lines):
    line = lines[i].strip()
    if line.startswith('Q'):
        # 收集问题的所有行
        question = []
        while i < len(lines) and lines[i].strip().startswith('Q'):
            question.append(lines[i].strip()[1:])  # 去掉开头的'Q'
            i += 1
        question = '\n'.join(question)  # 合并问题的行

        # 收集答案的所有行
        answer = []
        while i < len(lines) and lines[i].strip().startswith('A'):
            answer.append(lines[i].strip()[1:])  # 去掉开头的'A'
            i += 1
        answer = '\n'.join(answer)  # 合并答案的行

        # 检查问题是否为垃圾信息或答案是否为空
        if not Filter.isSpam(question, addintoList=False) and answer != '':
            filtered_lines.append('Q' + question + '\n')
            filtered_lines.append('A' + answer + '\n')
        else:
            pass
            # print('X', question)
    else:
        i += 1

# 将过滤后的行写入新的文件
with open('newTrainingData.txt', 'w', encoding='utf-8') as new_file:
    new_file.writelines(filtered_lines)
