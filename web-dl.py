#!/usr/bin/python
import os
import sys

def multipleUrldl(filename):
    '''
    Loads list of URLs from a file and downloads them.
    :param filename: Obtained through the call to the program as a parameter when.
    :return: Calls hackShop(EachLineOfFile)
    '''
    urlsFile = open(filename, 'r')
    for url in urlsFile:
        os.system("wget " + url)


def main():
    if len(sys.argv) == 2:
        multipleUrldl(sys.argv[1])
    else:
        print "ussage: python web-dl filename"

if __name__ == '__main__':
    main()