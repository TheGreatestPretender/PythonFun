import zipfile

from threading import Thread
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
        #threading allows us to test multiple cases of passwords
        t = Thread(target=extractingFile, args=(zFile, psw))
        t.start()

if __name__ == '__main__':
    main()
