import zipfile

def extractingFile(zFile, password):
    try:
        zFile.extractall(pwd = password)
        return password
    except:
        return


def main():
    zFile = zipfile.ZipFile('evil.zip')
    dictFile = open('dictionary.txt')

    for line in passFile.readlines():
        psw = line.strip('\n') #only one password per line
        guess = extractingFile(zFile, password)
        if guess:
            print '[+] Password = ' + password + '\n'
            exit(0)

if __name__ == '__main__':
    main()
