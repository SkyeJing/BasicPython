# coding=utf-8
# 定一个变量并赋值
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
# %s字符串占位符，%d数字占位符
# 多个占位符时，后面的变量要在括号中用逗号隔开
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
# this line is tricky, try to get it exactly right
print "If I add %d,%d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)