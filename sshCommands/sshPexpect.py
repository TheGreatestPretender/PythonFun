#have to download pexpect python module from interwebs
#pexpect is a module that gives us the ability to interact with programs, watch
# for expcted outputs and respond based on them

#!/usr/bin/python
import pexpect

#first prompts we get whenever starting cli
PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def connect(user, host, password):
    ssh_newkey = 'Are you sure you wnt to continue connecting?'
    connStr = 'ssh ' + user + '@' + host

    #make a child program with the input connStr
    child = pexpect.spawn(connStr)
    #three possible outcomes: timeout, ssh_newkey, or prompted for password
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,'[P|p]assword:'])

    #if the returned output is timeout throws error
    if ret == 0:
        print '[-] Error connecting'
        return
    #if the returned output is the new ssh key send in yes
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
        if ret == 0:
            print '[-] Error connecting'
            return

    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    host = 'localhost'
    user = 'root'
    password = 'toor'
    child = connect(user, host, password)
    send_command(child, 'cat passwords.txt | grep root')

if __name__ == '__main__':
    main()
