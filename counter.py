import os
import io
from collections import Counter
from multiprocessing import Pool

# 遍历文件夹，并取出文件夹下所有文件的路径
def file_name(path):
    # 创建一个空列表
    L = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            '''
            其中os.path.splitext()函数将路径拆分为文件名 + 扩展名，
            例如os.path.splitext(“E: / lena.jpg”)将得到”E: / lena“+”.jpg”。
            '''
            if os.path.splitext(file)[1] == '.txt':
                L.append(os.path.join(dirpath, file)) # 往L列表末尾添加新的对象，
    return L

def counter(path):
    word = []
    counter = {}
    with io.open(path) as f:
        for line in f:
            # 去掉每一行两边的空白
            line = line.strip()
            # 如果为空行则跳过该轮循环
            if len(line) == 0:
                continue

            for x in line:
                '''
                # 去掉标点符号以及空白符
                if x in [' ', '', '\t', '\n', '。', '.', ',', '，', '(', ')', '（', '）', '：', ':', '□', '？', '！', '《', '》', '、', '；',
                         '“', '”', '"', '=', '……', '·']:
                    continue
                # 去掉数字
                if x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    continue
                # 去掉大小写字母
                if x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                         'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                         'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']:
                    continue
                '''
                if not x in word:
                    word.append(x)
                if not x in counter:
                    counter[x] = 0
                else:
                    counter[x] += 1
    return counter

def main():
    path = "C:\Python\corpus\chinese"
    filepaths = file_name(path)
    print("Totally {} documents need to processed.". format(len(filepaths)))

    stat = {}
    i = 0
    for file_path in filepaths:
        i += 1
        print("Now the {}th document is processed. Waiting...". format(i))
        dic = counter(file_path)
        stat = dict(Counter(stat) + Counter(dic))
        print("Continue.")

    # lambda生成一个临时函数
    # d表示字典的每一对键值对，d[0]为key，d[1]为value
    # reverse为True表示降序排序
    # 按字符出现的频率排序，取前50个数据
    stat_list_1 = sorted(stat.items(), key=lambda d:d[1], reverse=True)
    print(stat_list_1[:50])
    file = open('counter.txt', 'w', encoding='utf-8')
    for data in stat_list_1[:50]:
        file.write(data[0] + ": " + str(data[1]) + "\n")
    file.close()

    # 取词频大于50000的数据
    stat_list_2 = {k:v for k,v in stat.items() if v>50000}
    stat_list_3 = sorted(stat_list_2.items(), key=lambda d: d[1], reverse=True)
    print(stat_list_3)
 #   print(stat_list_2)

if __name__ == '__main__':
    main()
