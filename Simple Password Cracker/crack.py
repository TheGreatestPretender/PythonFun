#creating password cracker with dictionary.txt and password.txt
#dictionary.txt contains

import crypt


def testPass(cryptPass, dname):
    salt = cryptPass[0:2]
    dictFile = open(dname, 'r')

    for word in dictFile.readlines():
        #one word on each line
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)

        if (cryptWord == cryptPass):
            print "[+] FOUND PASSWORD: " + word +"\n"
            return

    print "[-] Password not found :( \n)"
    return

def main():
    passFile = open('passwords.txt', 'r')

    for line in passFile.readlines():
        #generally password files have username: password type of format
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[*] cracking password for: " + user
            testPass(cryptPass, 'dictionary.txt')

#idk what this means yet but I was told to write it
if __name__ == "__main__":
    main()
