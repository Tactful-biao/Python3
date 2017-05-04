#!/usr/bin/env python3
# 子进程

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)
