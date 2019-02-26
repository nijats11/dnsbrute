#/usr/bin/python3

import os
from termcolor import colored

#url for tools whic our script uses
reconngUrl = 'https://bitbucket.org/LaNMaSteR53/recon-ng'
altdnsUrl = 'https://github.com/infosec-au/altdns'
sublisterUrl = 'https://github.com/aboul3la/Sublist3r'


def getPath():
    print(colored("Please specify installation path", "green"))
    path = str(input())
    path += "/dnsbrute"
    return path


def checkPath(path):
    if not os.path.exists(path+"/dnsbrute"):
        os.makedirs(path)


def installTools(path):
     os.chdir(path)
     os.system('git clone {}'.format(reconngUrl))
     os.system('git clone {}'.format(altdnsUrl))
     os.system('git clone {}'.format(sublisterUrl))
     os.system('gem install aquatone')

if __name__ == '__main__':
    path = getPath()
    checkPath(path)
    installTools(path)

