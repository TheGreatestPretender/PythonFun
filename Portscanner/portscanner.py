import optparse
import socket
from socket import *

def connScan(tgtHost, tgtPort):
    try:
        #AF_INET: what type of addresses we are using
        #SOCK_STREAM: TCP socket
        #SOCK_DGRAM: UDP socket

        #create TCP socket that will read addresses
        connSoc = socket(AF_INET, SOCK_STREAM)
        #connect to target port using target host address
        connSoc.connect((tgtHost, tgtPort))
        connSoc.send('ViolentPython\r\n')

        #recv() returns the amount of data (in bits) available
        results = connSoc.recv(100)
        print '[+]%d/TCP open' % tgtPort
        print '[+] ' + str(results)
        #always close socket
        connSock.close()

    #if port not open
    except:
        print '[-]%d/TCP closed' % tgtPort


def portScan(tgtHost, tgtPorts):

    #try to get IP from host name if not cannot resolve
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host " % tgtHost
        return

    #try to get host name from IP else just get scan results for IP
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: ' + tgtName[0]
    except:
        print '\n[+] Scan Results for: ' + tgtIP

    #so process doesn't hang
    setdefaulttimeout(1)

    #for every port, print this and test connectivity
    for tgtPort in tgtPorts:
        print 'Scanning port ' + tgtPort
        connScan(tgtHost, int(tgtPort))


def main():
    parser = optparse.OptionParser("usage%prog -H <target host> -p <target port>")

    #parsing available options
    parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host')
    parser.add_option('-p', dest = 'tgtPort', type = 'string', help = 'specify target port(s)')

    #create instance of options
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    #if not host or ports given
    if (tgtHost == None) | (tgtPorts[0] == None):
        print '[-] You must specify a target host and port(s)'
        exit(0)

    #actually scan ports
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
