import re
import urllib.request
import os

with open("mario.txt", "r", encoding='UTF-8') as f:  # open file
    data = f.read()  # read file
    f.close()  # close file
it = re.finditer(r'http:\\/\\/.+?\.mp3', data)  # extract the url by regex
string = []  # create a array to store the url
n = 1
path = "./music"  # file path
if not os.path.exists(path):
    os.makedirs(path)  # if there isn't such a file then create one

for match in it:
    string.append(match.group())  # store the url to next position

for url in string:
    clr_format = re.sub(r'\\', "", url)  # clear the "\"
    print(clr_format)
    name = "music/" + str(n).zfill(3) + ".mp3"  # name the file
    print(name)
    urllib.request.urlretrieve(clr_format, name)  # access the http sources and name them
    n += 1
