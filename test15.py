# coding=utf-8
import codecs
# 从sys中导入argv模组
from sys import argv
# 将入参分别定义变量名
script, filename = argv
# 打开文件
txt = open(filename)
# 输出含文件名变量的字符串
print "Here's your file %r:" % filename
# 打印文件内容
print txt.read()
# 关闭文件
txt.close()
# 打印字符串
print "Type the filename again:"
# 等待输入
file_again = raw_input(">")
# 打开文件
txt_again = open(file_again)
# 打印文件内容
print txt_again.read().decode('utf-8')
# 关闭文件
txt_again.close()
