#coding:utf-8 
from urllib import urlretrieve
from os import path
'''
	作用:
		用于保存网页上的文件
		我是拿来下歌的,不知道下太大的东西会怎么样
	用法:
		比如从Network或者这么别的地方搞到类似https://xxx.xxxxx.com/xxx.xxx
		粘到Enter URL里
		手工输入地址什么的我没试过,好麻烦啊,在问Enter Location时回车默认保存到桌面
		名字要自己改
		以上,祝好!

'''

def rightIndex(url):
	i=len(url)-1
	while i>=0:
		if url[i]=='/':
			return i
		i-=1

def Schedule(a,b,c):#a:已经下载的数据块|b:数据块的大小|c:远程文件的大小
	per = 100.0 * a * b / c
	global time
	if per > 100 :
		per = 100
	if per>=time*10:
		time+=0.5
		print '%.2f%%' % per

time=0
url=raw_input('Enter URL:')
location=raw_input('Enter Location:')
name=url[rightIndex(url)+1:]
if location=='':
   location=path.join(path.expanduser("~"),"Desktop")+'\\'+str(name)

urlretrieve(url,location,Schedule)
print 'Done!'

