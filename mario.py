import re
import urllib.request
import os
import requests
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')
url = "https://voice.baidu.com/Page/soundmuseum"
queries = {"query": "超级玛丽音效", "srcid": "31354"}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/68.0.3440.106 Safari/537.36'}
data = requests.get(url, params=queries, headers=headers)


def main():
    it = re.finditer(r'http:\\/\\/.+?\.mp3', data.text)  # extract the url by regex
    string = []  # create a array to store the url
    n = 1
    path = "./music"  # file path
    if not os.path.exists(path):
        logging.debug("creating a new directory")
        os.makedirs(path)  # if there isn't such a file then create one

    for match in it:
        string.append(match.group())  # store the url to next position
    logging.debug("Have got all the urls,ready to download")
    for url in string:
        logging.debug("Downloading "+str(n).zfill(3) + ".mp3")
        clr_format = re.sub(r'\\', "", url)  # clear the "\"
        name = "music/" + str(n).zfill(3) + ".mp3"  # name the file
        urllib.request.urlretrieve(clr_format, name)  # access the http sources and name them
        n += 1


if __name__ == "__main__":
    main()
