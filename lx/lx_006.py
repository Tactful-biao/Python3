#!/usr/bin/env python
#对于http://something.com形式的URL进行分割
url = input('请输入URL： ')
domain = url[11:-4]
print ("Domain name: "+domain)
