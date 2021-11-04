import os
import time
import jieba

filelist = {}  # 文件名
dict_temp = {}  # 字典
is_ok = {}  # 交作业判断符

# 打开名单读取信息保存到字典和词库
def load_dict_from_file():
    global dict_temp, is_ok
    dict_temp.clear()
    is_ok.clear() 
    with open('list.txt', 'r', encoding = 'utf-8') as dict_file:  # 打开文件
        for line in dict_file.readlines():
            (key, value) = line.strip().split(':')
            dict_temp[key] = value  # 添加班级信息字典
            is_ok[key] = 0  # 交作业判断字典
            jieba.add_word(key)  # 保存名字到jieba词库

#找文件名
def get_file_list():
    global filelist
    rootdir = 'file' #作业文件路径
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        paths = os.path.join(rootdir, list[i])
        (key, value) = os.path.basename(paths).split('.')  # 每个文件的名字做一个列表元素
        filelist[key] = value

#work_name = input("请输入当前作业的名称：")

load_dict_from_file()
get_file_list()

m = len(filelist)  # 打印出目录下所有的文件
#del dict_temp['姓名']

for n in filelist:
    words = jieba.lcut(n)
    # print (word)  # 分词测试
    for key in dict_temp:
        for word in words:
            if word == key:
                oldname = './file/' + n + '.' + filelist[n]
                newname = './file/' + dict_temp[key] + key + '.' + filelist[n]
                # print (oldname)  # 测试语句
                # print (newname)  # 测试语句
                os.rename(oldname, newname)
                is_ok[key] = 1
                break


print ('目前共有{}人已交作业'.format(m))
time.sleep(2)

# 分辨没有交作业的
# print (is_ok.keys())
#del is_ok['姓名']

for key in is_ok:
    if is_ok[key] == 0:
            #print ("未交作业".format(key))
            print ("{}未交作业".format(key))
print ("---------------------")
print ("作业已处理完成")
time.sleep(3)
print ("作业提交检测 by ZH D")
time.sleep(3)
