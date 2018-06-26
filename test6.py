# coding=utf-8
# 使用以上语句时，=前后不能有空格
# %d是数字的占位符
x = "There are %d types of people." % 10
# 对变量赋值
binary = "binary"
do_not = "don't"
# 有多个字符串占位符时，多个变量需放在括号里用逗号隔开
y = "Those who know %s and Those who %s." % (binary, do_not)
print x
print y
# %r会显示变量的原始数据
print "I said:%r." % x
print "I also said: '%s'." % y
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious
w = "This is the left side of ..."
e = "a string with a right side."
# 多字符串相加等同于拼接字符串
print w + e