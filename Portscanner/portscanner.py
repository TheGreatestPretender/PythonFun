import optparse
import socket
from socket import *

#available cli options
parser = optparse.OptionParser('usage %prog -h <target host> -p <target port>')
parser.add_option('-h', dest='tgtHost', type='string', help='specify  target host')
parser.add_option('-p', dest='tgtPort', type='int', help='specify target port')

#create instance of options parser
(options, args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort

#if user doesn't enter either target host or port, error and show usage
if (tgtHost == None) | (tgtPort == None):
    print parser.usage
    exit(0)



def connScan(tgtHost, tgtPort):
    try:
        #AF_INET: what type of addresses we are using
        #SOCK_STREAM: TCP socket
        #SOCK_DGRAM: UDP socket

        #create TCP socket that will read addresses
        connSoc = socket(AF_INET, SOCK_STREAM)
        #connect to target port using target host address
        connSoc.connect((tgtHost, tgtPort))

        print '[+]%d/TCP open' % tgtPort
        #always close socket
        connSock.close()

    #if port not open
    except:
        print '[-]%d/TCP closed' % tgtPort


def portScan(tgtHost, tgtPort):
    try:
        tgtIP = gethostbyname(tgtHost)

    except:
        print "[-] Cannot resolve '%s': Unknown host " % tgtHost
        return


    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: ' + tgtName[0]
    except:
        print '\n[+] Scan Results for: ' + tgtIP


    setdefaulttimeout(1)

    #for every port, print this and test connectivity
    for tgtPort in tgtPorts:
        print 'Scanning port ' + tgtPort
        connScan(tgtHost, int(tgtPort))

#still don't know what the point of this is
if __name__ == '__main__':
    main()
