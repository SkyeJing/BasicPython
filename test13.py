# coding=utf-8
# argv is argument variable
# 使用argv时可以在程序运行时让用户输入参数
# 使用raw_input时可以在程序任意处让用户输入参数
from sys import argv
script, first, second, third = argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print raw_input("Input anything:")