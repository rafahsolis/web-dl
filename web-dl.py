#!/usr/bin/python
import os
import sys
import random
import json
import requests

def multipleUrldl(filename):
    '''
    Loads list of URLs from a file and downloads them.
    :param filename: Obtained through the call to the program as a parameter when.
    :return: Calls hackShop(EachLineOfFile)
    '''
    urlsFile = open(filename, 'r')
    for url in urlsFile:
        os.system("wget " + url)


def rnd1000(filename):
    newfilenamestd = "web-dl"
    exists = os.path.isfile("web-dl.json")
    counter = 0
    while exists:
        newfilename = newfilenamestd + str(counter)
        exists = os.path.isfile(newfilename + ".json")
        counter += 1
    if counter < 1:
        newfilename = newfilenamestd + ".json"
    else:
        newfilename = newfilename + ".json"

    sample = random.sample(range(0, 26909), 1000)
    counter = 0
    urlsfile = open(filename, 'r')

    with open(newfilename, 'w') as resultfile:
        data = json.load(urlsfile)
        resultfile.write("[")
        for i in data:
            if counter in sample:
                try:
                    web = requests.get(i['URL'])
                    i['html'] = web.text
                except Exception as e:
                    print e
                    continue

                finally:
                    json.dump(i, resultfile)
                    resultfile.write(',\n')
            counter += 1

        json.dump({"Primary Category": "", "Secondary Category": "", "Title": "", "URL": ""}, resultfile)
        resultfile.write(']')
        urlsfile.close()


def main():
    if len(sys.argv) == 2:
        multipleUrldl(sys.argv[1])
    if len(sys.argv) == 3 and sys.argv[2] == "--rnd1000":
            rnd1000(sys.argv[1])
    else:
        print "ussage: python web-dl filename {--rnd1000; this parameter will download a random 1000 pages from the " \
              "26900 contained in classification.json adding a json field html:value} "

if __name__ == '__main__':
    main()