## 1、查分数
scores = {'name1':80,'name2':90,'name3':100}
name = input("please input your name:")
print(scores[name])

##2、数据库
text = "赵钱孙李、周吴郑王、冯陈褚卫、蒋沈韩杨、朱秦尤许、何吕施张、孔曹严华、金魏陶姜、戚谢邹喻、柏水窦章、云苏潘葛、奚范彭郎、鲁韦昌马、苗凤花方、俞任袁柳、酆鲍史唐、费廉岑薛、雷贺倪汤、滕殷罗毕、郝邬安常、乐于时傅、皮卞齐康、伍余元卜、顾孟平黄、和穆萧尹、姚邵湛汪、祁毛禹狄、米贝明臧、计伏成戴、谈宋茅庞、熊纪舒屈、项祝董梁、杜阮蓝闵、席季麻强、贾路娄危、江童颜郭、梅盛林刁、钟徐邱骆、高夏蔡田、樊胡凌霍、虞万支柯、昝管卢莫、经房裘缪、干解应宗、丁宣贲邓、郁单杭洪、包诸左石、崔吉钮龚、程嵇邢滑、裴陆荣翁、荀羊於惠、甄麴家封、芮羿储靳、汲邴糜松、井段富巫、乌焦巴弓、牧隗山谷、车侯宓蓬、全郗班仰、秋仲伊宫、宁仇栾暴、甘钭厉戎、祖武符刘"

import pypinyin
pinyin_list = pypinyin.pinyin(text,style=pypinyin.Style.NORMAL)
name_list = [item[0].title() for item in pinyin_list if item[0] != '、']
names = list(set(name_list))

import math

import random
score_template = {"physics":None,"math":None,"python":None}
scores = score_template.copy()

score_db = dict()
for name in names:
    score = math.ceil(random.gauss(75,20))
    if score > 100:score = 100
    if score < 0:score = 0
    scores["physics"] = score

    score = math.ceil(random.gauss(75,20))
    if score > 100:score = 100
    if score < 0:score = 0
    scores["math"] = score

    score = math.ceil(random.gauss(75,20))
    if score > 100:score = 100
    if score < 0:score = 0
    scores["python"] = score

    score_db[name] = scores

    print(score_db)

def get_random_score():
    score = math.ceil(random.gauss(75,20))
    if score > 100:score = 100
    if score < 0:score = 0
    return score

score_db = {name : {'pyhsics':get_random_score(),'math':get_random_score(),'python':get_random_score()}for name in names}

import json

with open("d:\\score_db.json",'w') as f:
    json.dump(score_db,f)

    import json

with open("d:\\score_db.json") as f:
    score_db = json.load(f)

##3、单词频率统计及绘图
text = '''
Google today released the open source version of the differential privacy library used in some its core products, such as Google Maps. Any organization or developer can now check out the library on GitHub.

Differential privacy limits the algorithms used to publish aggregate information about a statistical database. Whether you are a city planner, small business owner, or software developer, chances are you want to gain insights from the data of your citizens, customers, or users. But you don’t want to lose their trust in the process. Differentially private data analysis enables organizations to learn from the majority of their data without allowing any single individual’s data to be distinguished or re-identified.

“If you are a health researcher, you may want to compare the average amount of time patients remain admitted across various hospitals in order to determine if there are differences in care,” Google product manager Miguel Guevara explains. “Differential privacy is a high-assurance, analytic means of ensuring that use cases like this are addressed in a privacy-preserving manner.”
Differential privacy library features

Google promises its library is easy for developers to deploy. It can help you perform functions that are difficult to execute from scratch, “like automatically calculating bounds on user contributions,” Guevera says. Key features include:

    Statistical functions: Most common data science operations (counts, sums, averages, medians, and percentiles) are supported.
    Rigorous testing: Besides an extensive test suite, an extensible “Stochastic Differential Privacy Model Checker library” helps prevent mistakes.
    Ready to use: A PostgreSQL extension, along with common recipes, is included.
    Modular: The library can be extended to include other functionalities, such as additional mechanisms, aggregation functions, or privacy budget management.
    This isn’t Google’s first differential privacy rodeo, but the company has been particularly busy in the space this year. In March, Google released TensorFlow Privacy and TensorFlow Federated. In June, the company open-sourced Private Join and Compute, which gives companies data insights while preserving privacy. To learn more about Google’s approach, check out the team’s technical paper on arXiv.
'''

text = text.lower()
for sep in '\n.,"\',”“()':
    text = text.replace(sep," ")

words = text.split(' ')
words = [word for word in words if word != '']

count = {}
for word in words:
    count.setdefault(word,0)
    count[word] += 1

words_by_count = dict()
for word in count.keys():
    words_by_count.setdefault(count[word],[])
    words_by_count[count[word]].append(word)

for item in sorted(words_by_count.keys(),reverse = False):
    print(f"Count {item}:",end=" ")
    for word in words_by_count[item]:
        print(word,end="\t")
    print("\n")

words = [w for w in count.keys()]
count = [count[w] for w in words]
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,40))
ax = fig.subplots()
plt.barh(words,count)
plt.show()