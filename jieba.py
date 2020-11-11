#做了一个简单的，用来进行标题分词分析的代码，用的jieba包（中文分词）需要安装记得百度，有一个指令后面跟了一个镜像网址，要快不少（pip install jieba 忘了的一个网址）

def analyse(resultlist):
    
    titlelist = []
    for i in resultlist:
        titlelist.append(i[3])
    title = ''.join(titlelist)
    clearlist = ['o(*￣︶￣*)o~','(*╹▽╹*)','【','】','）','（','(。-`ω´-)','(´；ω；`)','⭐️',' ','❣','！','…','.','·','☆','直播','测试','阿巴','直播间','今天','晚上','一起','什么','主播','24','小时','下饭']
    for i in clearlist:
        title = title.replace(i,'')  #对标题里面乱七八糟的玩意去除，整合成一个整的字符串

    words = jieba.lcut_for_search(title)            #用jieba进行分词
    counts = {}

    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1           #进行统计计数

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)     #对结果排序

    for i in range(len(items)):
        word, count = items[i]
        print("{0:<5}{1:>5}".format(word, count))
        
analyse(resultlist)
