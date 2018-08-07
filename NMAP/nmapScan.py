#need to download both nmap/zenmap and nmap python module off of interwebs
#or you can use the following command: pip install python_nmap
#to install pip via cli use: sudo easy_install pip
#!/usr/bin/env python
import nmap
import optparse


def nmapScan(tgtHost, tgtPort):
    #creating scan object
    nmScan = nmap.PortScanner()
    #actually scanning when given host and port
    nmScan.scan(tgtHost, tgtPort)
    #gives the state of the current scan
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']

    print " [*] " + tgtHost + " TCP/" + tgtPort + " " + state

def main():
    #for the most part this is the same as the previous (portscanner.py) except
    # we added the nmScan into our for loop
        parser = optparse.OptionParser("usage%prog -H <target host> -p <target port>")

        #parsing available options
        parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host')
        parser.add_option('-p', dest = 'tgtPort', type = 'string', help = 'specify target port(s)')

        (options, args) = parser.parse_args()

        #for some reason will not split at , therefore only using first port written
        tgtHost = options.tgtHost
        tgtPorts = str(options.tgtPort).split(', ')

        if (tgtHost == None) | (tgtPorts[0] == None):
            print parser.usage
            exit(0)

        for tgtPort in tgtPorts:
            nmapScan(tgtHost, tgtPort)

#still dont know what this is used for
#i guess i'll find out eventually
if __name__ == '__main__':
    main()
