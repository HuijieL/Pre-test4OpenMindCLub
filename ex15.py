#coding: UTF-8 #

from sys import argv  # 从系统中引入变量argv

script, filename = argv #定义两个变量，一个是程序，一个是要读取的文件名

# txt = open(filename) #打开文件

# print "Here's your file %r:" % filename  #在屏幕上显示提示语：
# print txt.read()  #读取打开的文件，并打印出来

file_again = raw_input("> ")#从终端原始输入文件名，

txt_again = open(file_again)#打开这个文件

print txt_again.read()#读取打开的文件，并打印到屏幕上
