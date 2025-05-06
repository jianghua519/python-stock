import requests
from lxml import etree
import jieba
import pandas as pd
import re

# 定义一个简单的停用词表
stopwords = set(['的', '是', '了', '在', '我', '你', '他', '们', '有', '没有'])

def clean_text(text):
    # 去除HTML标签和多余空格
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_stopwords(text):
    words = jieba.lcut(text)
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)

# 示例数据集
news_data = [
    {
        'title': '【重大】公司宣布巨额回购计划！',
        'content': '近日，该公司宣布了一项巨额股份回购计划，市场反应热烈...'
    },
    {
        'title': '利空来袭：业绩不达预期',
        'content': '最新财报显示公司净利润同比下降，低于市场预期...'
    },
    {
        'title': '行业利好：政策支持行业发展',
        'content': '政府出台新政策，大力支持该行业发展，公司前景看好...'
    }
]

# 数据清洗和分词
cleaned_news = []
for item in news_data:
    title = clean_text(item['title'])
    print("1:" + title)
    content = clean_text(item['content'])
    print("2:" + content)
    text = f"{title} {content}"
    print("3:" + text)
    cleaned_text = remove_stopwords(text)
    print("4:" + cleaned_text)
    
    # 标注情感倾向
    if '利好' in text or '预计增长' in text:
        label = 1
    elif '利空' in text or '业绩不达预期' in text:
        label = -1
    else:
        label = 0
    
    cleaned_news.append({
        'text': cleaned_text,
        'label': label
    })

# 输出结果
df = pd.DataFrame(cleaned_news)
print(df)